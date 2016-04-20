import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('images/opencv_logo.png')
 
blur=cv2.blur(img,(5,5))    #kernel 5x5 size 

#Gaussian blur
gaussian_blur=cv2.GaussianBlur(img,(5,5),0)    
#sigmaX = 0 

#Median blur
median_blur=cv2.medianBlur(img,5)    

#bilateral
bilateral = cv2.bilateralFilter(img,9,75,75)    
#9 = Diameter of each pixel neighborhood that is used during filtering
#75 = sigmaColor    Filter sigma in the color space.
#75 = sigmaSpace    Filter sigma in the coordinate space.

titles=['Original','Averaging','Gaussian','Median','Bilateral']
images=[img,blur,gaussian_blur,median_blur,bilateral]

#plt.subplot(121),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
#plt.xticks([]), plt.yticks([])

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
