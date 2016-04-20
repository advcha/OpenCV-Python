import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('images/opencv_logo.png')
 
kernel = np.ones((5,5),np.float32)/25   #create 5x5 matrix with each value is one then divide 25 (add 25 pixel below)
dst = cv2.filter2D(img,-1,kernel)
#-1 is desired dept means the output image will have the same depth as the source. 
#ref:http://docs.opencv.org/3.1.0/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04&gsc.tab=0 
#ref:http://docs.opencv.org/3.1.0/d4/d86/group__imgproc__filter.html#filter_depths&gsc.tab=0. 
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
