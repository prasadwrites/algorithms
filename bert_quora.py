import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as tf_text
import tensorflow_datasets as tfds
from official.nlp.data import classifier_data_lib
from official.nlp.bert import tokenization
from official.nlp import optimization
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt

print("TF Version: ", tf.__version__)
print("Eager mode: ", tf.executing_eagerly())
print("Hub version: ", hub.__version__)
print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#########################
#getting dataset
#########################
print("Downloading datasets ...")
df = pd.read_csv('https://archive.org/download/fine-tune-bert-tensorflow-train.csv/train.csv.zip', compression='zip', low_memory=False)



#slicing dataset
train_df, remaining = train_test_split(df, random_state=42, train_size=0.0075, stratify=df.target.values)
valid_df , _ = train_test_split(remaining, random_state=42,train_size=0.00075, stratify=remaining.target.values)
train_df.shape, valid_df.shape

with tf.device('/cpu:0'):
  train_data = tf.data.Dataset.from_tensor_slices((train_df.question_text.values, train_df.target.values))
  valid_data = tf.data.Dataset.from_tensor_slices((valid_df.question_text.values,valid_df.target.values))

  for text, label in train_data.take(1):
    print(text)
    print(label)


label_list = [0, 1] # Label categories
max_seq_length= 128 # maximum length of (token) input sequences
train_batch_size = 32

###################################################################################
# Get BERT layer and tokenizer:
# More details here: https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2
###################################################################################
bert_layer = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2", trainable=True)
vocab_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
do_lower_case = bert_layer.resolved_object.do_lower_case.numpy()

tokenizer = tokenization.FullTokenizer(vocab_file, do_lower_case)

#testing tokenizer
print(tokenizer.wordpiece_tokenizer.tokenize('testing the tokenizer'))
tokenizer.convert_tokens_to_ids(tokenizer.wordpiece_tokenizer.tokenize('hi, how are you doing?'))

############################################
#convert row to input features and label
#############################################
def to_feature(text, label, label_list=label_list, max_seq_length=max_seq_length, tokenizer=tokenizer):
  example = classifier_data_lib.InputExample(guid=None,text_a=text.numpy(),text_b=None,label=label.numpy())
  feature = classifier_data_lib.convert_single_example(0, example, label_list,max_seq_length, tokenizer)
  return (feature.input_ids, feature.input_mask, feature.segment_ids, feature.label_id)


########################################################
#handling graph<->eager conversions for tf.data.map
######################################################
def to_feature_map(text, label):
  input_ids, input_mask, segment_ids, label_id = tf.py_function(to_feature, inp=[text,label],
                                                                 Tout=[tf.int32,tf.int32,tf.int32,tf.int32])
  input_ids.set_shape([max_seq_length])
  input_mask.set_shape([max_seq_length])
  segment_ids.set_shape([max_seq_length])
  label_id.set_shape([])

  x={
     'input_word_ids' : input_ids,
     'input_mask' : input_mask,
     'input_type_ids': segment_ids
    }

  return(x, label_id)

#########################################
#creating TF input pipeline with tf.data
########################################
with tf.device('/cpu:0'):
  # train
  train_data = (train_data.map(to_feature_map,
                               num_parallel_calls=tf.data.experimental.AUTOTUNE)
  .shuffle(1000)
  .batch(32, drop_remainder= True)
  .prefetch(tf.data.experimental.AUTOTUNE))
  

  # valid
  valid_data = (valid_data.map(to_feature_map,
                               num_parallel_calls=tf.data.experimental.AUTOTUNE)
  
  .batch(32, drop_remainder= True)
  .prefetch(tf.data.experimental.AUTOTUNE))

##################
# check train data spec
##################
print(train_data.element_spec)

######################
# valid data spec
###################
print(valid_data.element_spec)


##########################
# Building the model
#########################
def create_model():
  input_word_ids = tf.keras.layers.Input(shape=(max_seq_length,), dtype=tf.int32,
                                       name="input_word_ids")
  input_mask = tf.keras.layers.Input(shape=(max_seq_length,), dtype=tf.int32,
                                   name="input_mask")
  input_type_ids = tf.keras.layers.Input(shape=(max_seq_length,), dtype=tf.int32,
                                    name="segment_ids")
  
  pooled_output, sequence_output = bert_layer([input_word_ids, input_mask, input_type_ids])

  drop = tf.keras.layers.Dropout(0.4)(pooled_output)
  output = tf.keras.layers.Dense(1,activation='sigmoid', name='output') (drop)

  model = tf.keras.Model(
      {
     'input_word_ids' : input_word_ids,
     'input_mask' : input_mask,
     'input_type_ids': input_type_ids
    },
    outputs=output)
  return model


####################
#Fine tuning BERT
####################
model = create_model()
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy()])

#####################
#print model summary
####################
print(model.summary())

#####################
#plot model for juypter /ipynb 
####################
print(tf.keras.utils.plot_model(model=model, show_shapes=True, dpi=768))

###############
# Train model
###############
epochs = 1
history = model.fit(train_data, validation_data=valid_data, epochs=epochs, verbose=1)

############################
#Evaluvate model benchmarks for ipynb/juypter
############################


def plot_graphs(history, metric):
  plt.plot(history.history[metric])
  plt.plot(history.history['val_'+metric], '')
  plt.xlabel("Epochs")
  plt.ylabel(metric)
  plt.legend([metric, 'val_'+metric])
  plt.show()


plot_graphs(history, 'binary_accuracy')