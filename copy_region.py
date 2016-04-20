import numpy as np
import cv2

img=cv2.imread('images/messi5.jpg')
cv2.imshow('Original',img)
#get the ball at this pixel. we can use gimp to open this image then find out the exact position
#at gimp, we can select the pixel position from X:330 and Y:280 with size 60x60, so it'll end to X:390,Y:340
#at matrix, the format is row (Y) x column (X), so we write like this:  img[280:340,330:390]
ball=img[280:340,330:390]
#override this pixel value by the ball value
img[273:333,100:160]=ball

cv2.imshow('Copy Ball',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
