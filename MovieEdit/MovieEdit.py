from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("filename").subclip(10, 20) #take from second 10 to second 20
clip2 = VideoFileClip("filename2").subclip(10, 20)
clip3 = VideoFileClip("filename3").subclip(20, 30)