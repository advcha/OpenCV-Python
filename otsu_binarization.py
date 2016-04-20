import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('images/dave.png',0) #FIRST, image should be CONVERTED TO GRAY SCALE
#img = cv2.imread('images/dave.jpg',0) #FIRST, image should be CONVERTED TO GRAY SCALE
img = cv2.imread('images/noisy2.png',0) #FIRST, image should be CONVERTED TO GRAY SCALE
 
# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
 
# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)   #pass 0 as a threshold value
 
# Otsu's thresholding after Gaussian filtering
#blur it first (add some noise???), why? pls read:https://blog.drecks-provider.de/why-you-should-blur-an-image-before-processing-it-using-opencv-and-python/
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)   #pass 0 as a threshold value
 
# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)','Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

#for i in xrange(3):
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()
