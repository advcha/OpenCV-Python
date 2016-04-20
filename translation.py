import cv2
import numpy as np

img = cv2.imread('images/messi5.jpg',0)
#rows,cols = img.shape --> SAME WITH THE BELOW BUT THE BELOW BETTER?
rows,cols = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('original',img)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
