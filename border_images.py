import numpy as np
import cv2
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt    --> SAME AS ABOVE

BLUE=[255,0,0]

img1=cv2.imread('/home/teddy/opencv/samples/data/opencv-logo.png')
img1=cv2.resize(img1,None,fx=0.5,fy=0.5)

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
 
plt.show()  #NOT WORKING??? WORKING FINE NOW!!!

#cv2.imshow('Original resized half',img1)
#cv2.imshow('replicate',replicate)
#cv2.imshow('reflect',reflect)
#cv2.imshow('reflect101',reflect101)
#cv2.imshow('wrap',wrap)
#cv2.imshow('constant',constant)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
