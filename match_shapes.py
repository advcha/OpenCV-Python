import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img1 = cv2.imread('images/star.jpg',0)
img2 = cv2.imread('images/star2.jpg',0)
img3 = cv2.imread('images/bolt.png',0)
img4 = cv2.imread('images/rect.jpg',0)
img5 = cv2.imread('images/approx.jpg',0)
img6 = cv2.imread('images/hand.jpg',0)
 
ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
ret, thresh3 = cv2.threshold(img3, 127, 255,0)
ret, thresh4 = cv2.threshold(img4, 127, 255,0)
ret, thresh5 = cv2.threshold(img5, 127, 255,0)
ret, thresh6 = cv2.threshold(img6, 127, 255,0)
im1,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
im1,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
im1,contours,hierarchy = cv2.findContours(thresh3,2,1)
cnt3 = contours[0]
im1,contours,hierarchy = cv2.findContours(thresh4,2,1)
cnt4 = contours[0]
im1,contours,hierarchy = cv2.findContours(thresh5,2,1)
cnt5 = contours[0]
im1,contours,hierarchy = cv2.findContours(thresh6,2,1)
cnt6 = contours[0]
 
ret12 = cv2.matchShapes(cnt1,cnt2,1,0.0)
ret13 = cv2.matchShapes(cnt1,cnt3,1,0.0)
ret14 = cv2.matchShapes(cnt1,cnt4,1,0.0)
ret15 = cv2.matchShapes(cnt1,cnt5,1,0.0)
ret16 = cv2.matchShapes(cnt1,cnt6,1,0.0)
#print ret
plt.subplot(2,3,1),plt.imshow(img1,cmap = 'gray')
plt.title('Match this with...'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(img2,cmap = 'gray')
plt.title('M is '+str(ret12)[:5]), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(img3,cmap = 'gray')
plt.title('M is '+str(ret13)[:5]), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(img4,cmap = 'gray')
plt.title('M is '+str(ret14)[:5]), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(img5,cmap = 'gray')
plt.title('M is '+str(ret15)[:5]), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(img6,cmap = 'gray')
plt.title('M is '+str(ret16)[:5]), plt.xticks([]), plt.yticks([])
 
plt.show()
