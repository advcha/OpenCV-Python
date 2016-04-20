import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('images/bolt.png')   #white bolt shape black background
#img_or=img #this copy is not working, img_or still be overriden by drawContours anyway. pls use below
img_rect=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_rect=cv2.cvtColor(img_rect,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_rect,127,255,0) #apply threshold to the gray image
im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   #get contours

cnt = contours[0]

#straight bounding rectangle
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img_rect,(x,y),(x+w,y+h),(0,255,0),3)

img_rotated=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_rotated=cv2.cvtColor(img_rotated,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_rotated,127,255,0) #apply threshold to the gray image
#rotated rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img_rotated,[box],0,(0,0,255),2)

img_circle=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_circle=cv2.cvtColor(img_circle,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_circle,127,255,0) #apply threshold to the gray image
#enclosing circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img_circle,center,radius,(0,255,0),2)

img_ellipse=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_ellipse=cv2.cvtColor(img_ellipse,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_ellipse,127,255,0) #apply threshold to the gray image
#fitting ellipse
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img_ellipse,ellipse,(0,255,0),2)

img_line=img.copy()   #make a shallow copy of the original image. IS IT BETTER THAN copyTo()???
img_gray_line=cv2.cvtColor(img_line,cv2.COLOR_BGR2GRAY)   #convert to gray scale
ret,thresh=cv2.threshold(img_gray_line,127,255,0) #apply threshold to the gray image
#fitting a line
rows,cols = img_line.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img_line,(cols-1,righty),(0,lefty),(0,255,0),2)

plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(img_rect,cmap = 'gray')
plt.title('Straight Bounding Rect'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(img_rotated,cmap = 'gray')
plt.title('Rotated Rect'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(img_circle,cmap = 'gray')
plt.title('Enclosing Circle'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(img_ellipse,cmap = 'gray')
plt.title('Fitting Ellipse'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(img_line,cmap = 'gray')
plt.title('Fitting Line'), plt.xticks([]), plt.yticks([])
 
plt.show()
