import cv2
import numpy as np
from matplotlib import pyplot as plt

#img=cv2.imread('images/messi5.jpg')    #not white and black image, hard to find contours???
#img=cv2.imread('images/rect.jpg')   #white rectangle over black background
img=cv2.imread('images/john_dory-zeus_faber.jpg')   #white rectangle over black background
#img_or=img #this copy is not working, img_or still be overriden by drawContours anyway. pls use below
img_or=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray,127,255,0) #apply threshold to the gray image
im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   #get contours
#print(str(contours))

#cnt=contours[:4]
#cv2.drawContours(img,[cnt],0,(0,255,0),3)

#draw all contours (the rectangle) with green color and thickness 3px
cv2.drawContours(img, contours, -1, (0,255,0), 3)

plt.subplot(2,2,1),plt.imshow(img_or,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(thresh,cmap = 'gray')
plt.title('Threshold'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(im2,cmap = 'gray')
plt.title('Find Contour'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(img,cmap = 'gray')
plt.title('Draw Contour'), plt.xticks([]), plt.yticks([])
 
plt.show()
