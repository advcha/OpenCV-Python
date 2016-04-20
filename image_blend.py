import numpy as np
import cv2

img1=cv2.imread('images/fruits.jpg')
#img2=cv2.imread('images/messi5.jpg')
img2=cv2.imread('images/fruits_gray.jpg')

#Image blend MUST BE SAME SIZE (PIXELS)!! blend fruits.jpg (512x480) with messi5.jpg (548x342) IS NOT WORKING!! 
res=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('Result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
