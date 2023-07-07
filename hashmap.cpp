#include <iostream>
#include <string>

using namespace std;

int TABLE_SIZE = 10000;

template <typename K, typename V>
class HashNode
{

public:
    HashNode(K _key, V _value)
    {
        key = _key;
        value = _value;
        next = NULL;
    }

    void setKey(K _key) 
    {
        key = _key;
    }

    K getKey() 
    {
        return key;
    }

    void setValue(V _value) 
    {
        value = _value;
    }

    V getValue() 
    {
        return value;
    }

    HashNode *getNext() 
    {
        return next;
    }

    void setNext(HashNode *_next)
    {
        next = _next;
    }

    void printHashNode()
    {
        cout << key << ":" << value << endl;
    }

private:
    K key;
    V value;
    HashNode *next;
};

template <typename K, typename V>
class HashTable
{
private:
    HashNode<K, V> *hash_table;

public:
    HashTable()
    {
        hash_table = (HashNode<K, V> *)malloc(TABLE_SIZE * sizeof(HashNode<K, V>));
    }

    ~HashTable()
    {

        free(hash_table);
    }

    unsigned long int _keyhash(string str)
    {
        unsigned long int strsum = 0;
        for (char i : str)
        {
            strsum = strsum + (int)i;
        }
        return strsum;
    }

    void addEntry(HashNode<K, V> hash_node)
    {

        int index = _keyhash(hash_node.getKey()) % TABLE_SIZE;
        if (hash_table[index].getNext() == NULL)
        {
            HashNode<string, string> lastNode("", "");
            hash_node.setNext(&lastNode);
            hash_table[index] = hash_node;
        }
        else
        {
            HashNode<K, V> *recurse = (HashNode<K, V> *)hash_table + index;
            HashNode<K, V> *lastRealNode;
            while (recurse->getNext() != NULL)
            {
                lastRealNode = recurse;
                if (recurse->getKey() == hash_node.getKey()){
                	
                	cout << "Key already present : " <<  recurse->getKey() << endl;
                	recurse->setValue(hash_node.getValue());
                	cout << "new Value  : " <<  recurse->getValue() << endl;
                	return;
                }
                recurse = recurse->getNext();
            }

            lastRealNode->setNext(&hash_node);
            HashNode<string, string> lastNode("", "");
            hash_node.setNext(&lastNode);
        }
        return;
    }

    V getValue(const K key) {
    int index = _keyhash(key) % TABLE_SIZE;
	    if (hash_table[index].getNext() == NULL ) {

		    cout << "key hash not found \n" << endl;

		}
		else {
		   	for (HashNode<K, V> *recurse = hash_table+index; recurse->getNext() != NULL ; recurse = recurse->getNext()  ){
		   		if (recurse->getKey() == key) return recurse->getValue();
		    }
		    cout << "key hash was found , key not found \n";
		    return NULL;

	    }

    }

    

    void printHashTable()
    {

        for (int i = 0; i < TABLE_SIZE; i++)
        {

            if (hash_table[i].getNext() != NULL)
            {
                HashNode<K, V> *entry = (HashNode<K, V> *)(hash_table + i);
                cout << entry->getKey() << endl;
                for (HashNode<K, V> *recurse = entry; recurse->getNext() != NULL; recurse = recurse->getNext())
                {
                    cout << "key:" << recurse->getKey() << " value:" << recurse->getValue() << endl;
                }
            }
        }
    }
};

int main(int argc, char *argv[])
{

    HashNode<string, string> hn1("semiconductor1", "intel");
    HashNode<string, string> hn2("pertroleum2", "chevron");
    HashNode<string, string> hn3("semiconductor2", "nvidia");
    HashNode<string, string> hn4("pertroleum2", "exxon");

    HashTable<string, string> ht;
    ht.addEntry(hn1);
    ht.addEntry(hn2);
    ht.addEntry(hn3);
    ht.addEntry(hn4);
 
    
    cout << ht.getValue("pertroleum2") << endl;
    ht.printHashTable();
}