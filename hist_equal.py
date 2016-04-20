import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('images/uss_arizona.jpg',0)
equ = cv2.equalizeHist(img)
#res = np.hstack((img,equ)) #stacking images side-by-side

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(equ,cmap = 'gray')
plt.title('Histogram Equalization'), plt.xticks([]), plt.yticks([])

plt.show()
