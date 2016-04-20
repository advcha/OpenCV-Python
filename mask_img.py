import numpy as np
import cv2

#load the images
#img=cv2.imread('images/messi5.jpg')
img = cv2.imread('images/john_dory-zeus_faber.jpg')
#img = cv2.imread('images/Temperate 09 - Small_clean.png')

imgtogray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Result',ret)
#threshold for remove noise
ret,mask=cv2.threshold(imgtogray,250,255,cv2.THRESH_BINARY) #mask value 250 is perfect to create the mask for the fish images
#print('ret:'+str(ret))
#ret:10.0
#cv2.imshow('Result Mask',mask)
mask_inv=cv2.bitwise_not(mask)
#cv2.imshow('Result Mask Inv',mask_inv)
blur = cv2.GaussianBlur(mask_inv,(5,5),0)

thresh = 250
max_thresh = 255

edges = cv2.Canny(blur,thresh,thresh*2)
#cv2.imshow('Result Blur',edges)
drawing = np.zeros(mask_inv.shape,np.uint8)             # Image to draw the contours
im2,contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(str(contours))
for cnt in contours:
    moments = cv2.moments(cnt)                          # Calculate moments
    if moments['m00']!=0:
        cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
        cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
        moment_area = moments['m00']                    # Contour area from moment
        contour_area = cv2.contourArea(cnt)             # Contour area using in_built function
        
        #cv2.drawContours(mask_inv,[cnt],0,(0,255,0),1)   # draw contours in green color
        cv2.drawContours(img,[cnt],0,(0,255,0),1)   # draw contours in green color
        #cv2.circle(drawing,(cx,cy),5,(0,0,255),-1)      # draw centroids in red color
#cv2.imshow('output',mask_inv)
cv2.imshow('output',img)
#cv2.imshow('input',img)

# Now black-out the area of logo in ROI
#error: (-215) (mtype == CV_8U || mtype == CV_8S) && _mask.sameSize(*psrc1) in function binary_op
#img2 has bigger size than img1???
#img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
#cv2.imshow('Result',img1)

# Take only region of logo from logo image.
#img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
#cv2.imshow('Result',img2_fg)

# Put logo in ROI and modify the main image
#dst=cv2.add(img1_bg,img2_fg)
#img1[0:rows,0:cols]=dst

#cv2.imshow('Result',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
