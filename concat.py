import cv2
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips,CompositeVideoClip
from PIL import Image


list_of_candidates = []
for (dirpath, dirnames, filenames) in os.walk("."):
            for filename in filenames:
                if (filename.endswith('.png') or filename.endswith('.jpg')):
                    list_of_candidates.append(os.sep.join([dirpath, filename]))


print(list_of_candidates)

video_path = "base_final.MP4"
for image_path in list_of_candidates:
    print(image_path)
    video_image_path = image_path+ ".mp4"
    frame = cv2.imread(image_path)
    frame_resized = cv2.resize(frame , (1080,1920))
    height, width, layers = frame_resized.shape
    print(height)
    print(width)
    video = cv2.VideoWriter(video_image_path, 0x00000021, 1, (width, height))
    for i in range(15):
        video.write(frame_resized)
    video.release()

    image_clip = VideoFileClip(video_image_path)
    orig_video_clip = VideoFileClip(video_path, target_resolution= (height,width))
    final_clip= concatenate_videoclips([orig_video_clip, image_clip], method='compose')
    final_clip.write_videofile(image_path + '_final.mp4')