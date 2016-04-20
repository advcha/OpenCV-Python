#ref:http://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv

import cv2
import numpy as np

src     = cv2.imread("images/messi5.jpg")     # Load a source image
overlay = cv2.imread("/home/teddy/opencv/samples/data/opencv-logo.png",-1)     # Load an image to overlay. IMPORTANT: -1=CV_LOAD_IMAGE_UNCHANGED   SO KEEP THE ALPHA/TRANSPARENCY CHANNEL
overlay=cv2.resize(overlay,None,fx=0.3,fy=0.3)  #resize it so the logo would be smaller than the main src

o_height,o_width=overlay.shape[:-1] #get just height and width the logo
#we'd put the logo at the top left of the main src. offset: 0,0
src_r_offset=0
src_c_offset=0

#loop for each channel, there are 4 channels: B (0), G (1), R (2) and Alpha (3)
for c in range(0,3):
    src[src_r_offset:o_height, src_c_offset:o_width, c] =  overlay[:,:,c] * (overlay[:,:,3]/255.0) +  src[src_r_offset:o_height, src_c_offset:o_width, c] * (1.0 - overlay[:,:,3]/255.0)

cv2.imshow('Overlay', src)

cv2.waitKey(0)
cv2.destroyAllWindows()
