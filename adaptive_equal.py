import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('images/clahe.jpg',0)
equ = cv2.equalizeHist(img)
#res = np.hstack((img,equ)) #stacking images side-by-side

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
    
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(equ,cmap = 'gray')
plt.title('Histogram Equalization'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(cl1,cmap = 'gray')
plt.title('Adaptive Hist Equalization'), plt.xticks([]), plt.yticks([])

plt.show()
