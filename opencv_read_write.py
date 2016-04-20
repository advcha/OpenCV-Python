import numpy as np
import cv2

#load a color image in grayscale
img=cv2.imread('images/fruits.jpg',0)

#display an image
cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
k=cv2.waitKey(0) & 0xFF

if k==27:   #wait for ESC key to exit
    cv2.destroyALlWindows()
elif k==ord('s'):   #wait 's' key to save and exit
    cv2.imwrite('images/fruits_gray.jpg',img)
    cv2.destroyAllWindows()
