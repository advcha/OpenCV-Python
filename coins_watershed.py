import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/water_coins.jpg')
img_ori=img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#use OTSU BINARIZATION TO ESTIMATE THE COINS
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
#use morphological opening to remove any small white noises in the image
#use morphological closing to remove any small white holes in the image
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
#since they are touching each other, another good option would be to find the distance transform and apply a proper threshold. Next we need to find the area which we are sure they are not coins. For that, we dilate the result. Dilation increases object boundary to background.
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
#In the thresholded image, we get some regions of coins which we are sure of coins and they are detached now.
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
#The remaining regions are those which we don't have any idea, whether it is coins or background. Watershed algorithm should find it. These areas are normally around the boundaries of coins where foreground and background meet (Or even two different coins meet). We call it border. It can be obtained from subtracting sure_fg area from sure_bg area. 
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
#Now we know for sure which are region of coins, which are background and all. So we create marker (it is an array of same size as that of original image, but with int32 datatype) and label the regions inside it.
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
#labels background of the image with 0, then other objects are labelled with integers starting from 1.
markers = markers+1

# Now, mark the region of unknown with zero
#we will mark unknown region, defined by unknown, with 0.
markers[unknown==255] = 0

#Now our marker is ready. It is time for final step, apply watershed. Then marker image will be modified. The boundary region will be marked with -1. 
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

plt.subplot(121),plt.imshow(img_ori,cmap='gray',interpolation='bicubic')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.title('Watershed'), plt.xticks([]), plt.yticks([])

plt.show()
