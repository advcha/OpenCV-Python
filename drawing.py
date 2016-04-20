import numpy as np
import cv2

#create a black image
img=np.zeros((512,512,3),np.uint8)

#draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

#draw a green rectangle at the top right of our image with thickness 3 px
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#draw a red-filled (thickness: -1) circle in the above rectangle
cv2.circle(img,(447,63), 63, (0,0,255), -1)

#draw a half of blue ellipse at the center of the image with thickness -1 (filled with blue color)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#draw a polygon with four vertices in yellow color
#create an array 4x2=8 represent the four coordinates of the vertices. it should be of type of int32
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#change/reshape the array. 'missing' -1 value n is calculated so that nx1x2=8, so n=4
#ref:http://scipy.github.io/old-wiki/pages/Numpy_Example_List.html#reshape
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#draw a text at the bottom-left corner
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('Drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
