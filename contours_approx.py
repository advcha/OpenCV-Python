import cv2
import numpy as np
from matplotlib import pyplot as plt

#img=cv2.imread('images/approx.jpg')   #white unregular shape over black background
#img=cv2.imread('images/star.jpg')   #white star shape black background
img=cv2.imread('images/john_dory-zeus_faber.jpg')   #white star shape black background
#img_or=img #this copy is not working, img_or still be overriden by drawContours anyway. pls use below
img_contour=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_contour=cv2.cvtColor(img_contour,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_contour,127,255,0) #apply threshold to the gray image
im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   #get contours

#draw all contours with green color and thickness 3px
cv2.drawContours(img_contour, contours, -1, (0,255,0), 3)

img_approx=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_approx=cv2.cvtColor(img_approx,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_approx,127,255,0) #apply threshold to the gray image
im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   #get contours

cnt = contours[0]
epsilon=0.1*cv2.arcLength(cnt,True)
approx=cv2.approxPolyDP(cnt,epsilon,True)
#print(approx)
#[[[130  33]]
# [[ 70 227]]
# [[190 227]]]

#draw approximation contours (most simple contours. it just 4 points. FASTER & SAVING MEMORY) with green color and thickness 3px
cv2.drawContours(img_approx, approx, -1, (0,255,0), 3)
#cv2.line(img_approx,(70,227),(190,227),(0,255,0), 3) #it draw line outside. not connect the points. why???
#SOLUTION: USE cv2.boundingRect BELOW!!!
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img_approx,(x,y),(x+w,y+h),(0,255,0),3)

#plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,2),plt.imshow(img_contour,cmap = 'gray')
#plt.title('Contours'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,3),plt.imshow(img_approx,cmap = 'gray')
#plt.title('Contours Approx'), plt.xticks([]), plt.yticks([])
 
#plt.show()

cv2.imshow('approx',img_approx)
cv2.waitKey()
cv2.destroyAllWindows()
