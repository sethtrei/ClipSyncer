import os
from moviepy.editor import *

# create array for clips
videos = []
# assign directory
directory = 'clips'

# iterate over files in
# that directory
for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        videos.append(f)


print(videos)

start = os.path.getmtime(videos[0])
concated = []

for path in videos:
    print(path)
    print(os.path.getmtime(path) - start)
    concated.append(VideoFileClip(path, audio=True).set_start(
        os.path.getmtime(path) - start))

output = CompositeVideoClip(concated)

output.write_videofile("output.mp4", codec='libx264',
                       audio_codec='aac',
                       temp_audiofile='temp-audio.m4a',
                       remove_temp=True)

