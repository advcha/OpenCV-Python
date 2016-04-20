import numpy as np
import cv2

img=cv2.imread('images/messi5.jpg')
cv2.imshow('Original',img)
#split and merge
#b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))
#cv2.imshow('SPLIT MERGE',img)

#set RED value to zero OR REMOVE RED CHANNEL
img[:,:,2]=0
cv2.imshow('NO RED',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
