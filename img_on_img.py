import numpy as np
import cv2

#load two images
img_main=cv2.imread('images/messi5.jpg')
img_logo=cv2.imread('/home/teddy/opencv/samples/data/opencv-logo.png')

rows_main,cols_main,channels_main=img_main.shape
#print('rows_main:'+str(rows_main)+', cols_main:'+str(cols_main)+', channels_main:'+str(channels_main))
#rows_main:342, cols_main:548, channels_main:3

# I want to put logo on top-left corner, So I create a ROI on the main image 
#resize the logo first because it too large
img_logo=cv2.resize(img_logo,None,fx=0.2,fy=0.2)
rows_logo,cols_logo,channels_logo=img_logo.shape
#print('rows_logo:'+str(rows_logo)+', cols_logo:'+str(cols_logo)+', channels_logo:'+str(channels_logo))
#before img_logo resize -> rows_logo:555, cols_logo:599, channels_logo:3
#after img_logo resize -> rows_logo:111, cols_logo:120, channels_logo:3

roi=img_main[0:rows_logo,0:cols_logo]
#print('roi:'+str(roi))
#roi:[[[ 39  43  44]
#  [ 42  46  47]
#  [ 44  47  52]
#  ...,
# ..., 
#  [ 49 124  86]
#  [ 52 125  87]
#  [ 51 124  86]]]
# Now create a mask of logo and create its inverse mask also
img_logotogray=cv2.cvtColor(img_logo,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Result',ret)
ret,mask_logo=cv2.threshold(img_logotogray,10,255,cv2.THRESH_BINARY)
#print('ret:'+str(ret))
#ret:10.0
#cv2.imshow('Result',mask_logo)
mask_logo_inv=cv2.bitwise_not(mask_logo)
#cv2.imshow('Result',mask_logo_inv)

# Now black-out the area of logo in ROI
#error: (-215) (mtype == CV_8U || mtype == CV_8S) && _mask.sameSize(*psrc1) in function binary_op
#img_logo has bigger size than img_main??? YEAH. RESIZE IT FIRST (ABOVE DONE)
img_main_bg=cv2.bitwise_and(roi,roi,mask=mask_logo_inv)
#cv2.imshow('Result',img_main_bg)

# Take only region of logo from logo image.
img_logo_fg=cv2.bitwise_and(img_logo,img_logo,mask=mask_logo)
#cv2.imshow('Result',img_logo_fg)

# Put logo in ROI and modify the main image
dst=cv2.add(img_main_bg,img_logo_fg)
img_main[0:rows_logo,0:cols_logo]=dst

cv2.imshow('Result',img_main)
cv2.waitKey(0)
cv2.destroyAllWindows()
