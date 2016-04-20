import cv2
import numpy as np
 
img = cv2.imread('images/messi5.jpg')
 
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
#lower_blue = np.array([110,50,50])
#lower_blue = np.array([110,100,100])
#upper_blue = np.array([130,255,255])
lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])

lower1_red = np.array([160,100,100])
upper1_red = np.array([180,255,255])

# Threshold the HSV image to get only blue colors
#mask = cv2.inRange(hsv, lower_blue, upper_blue)
mask = cv2.inRange(hsv, lower_red, upper_red)
mask = cv2.inRange(hsv, lower1_red, upper1_red)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('original',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
