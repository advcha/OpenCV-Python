import cv2
import numpy as np

img = cv2.imread('images/messi5.jpg',0)
#rows,cols = img.shape --> SAME WITH THE BELOW BUT THE BELOW BETTER?
rows,cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('original',img)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
