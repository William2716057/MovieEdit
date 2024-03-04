from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

clip1 = VideoFileClip("filename").subclip(10, 20) #take from second 10 to second 20
clip2 = VideoFileClip("filename2").subclip(10, 20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip3 = VideoFileClip("filename3").subclip(20, 30)
clip4 = VideoFileClip("filename4").subclip(10, 20)

combined = concatenate_videoclips([clip1, clip2, clip3])
combined.write_videofile("combined.mp4")
