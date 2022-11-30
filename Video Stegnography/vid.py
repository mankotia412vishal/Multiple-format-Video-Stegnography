# import cv2
# import numpy as np
# import glob

# frameSize = (800, 1920)

# out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

# for filename in glob.glob('./tmp/*.png'):
#     img = cv2.imread(filename)
#     out.write(img)

# out.release()


# ************************
# import cv2
import os

# image_folder = 'tmp'
# video_name = 'video.avi'

# images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape

# video = cv2.VideoWriter(video_name, 0, 1, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()


def save():
    os.system("ffmpeg -r 1 -i ./tmp/%01d.png -vcodec mpeg4 -y movie.mp4")

save()