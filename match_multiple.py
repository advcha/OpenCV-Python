import cv2
import numpy as np
from matplotlib import pyplot as plt
 
#img_rgb = cv2.imread('images/mario.jpg')
img_rgb = cv2.imread('images/more_coins.png')
img_ori=img_rgb.copy()
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/mario_coin1.png',0)   #MATCH
#template = cv2.imread('images/mario_coin.png',0)   #NOT MATCH, THE SIZE IS DIFFERENT WITH ON THE IMAGE
w, h = template.shape[::-1]
 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

#cv2.imwrite('res.png',img_rgb)
plt.subplot(121),plt.imshow(img_ori,cmap='gray',interpolation='bicubic')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_rgb,cmap='gray',interpolation='bicubic')
plt.title('Match Multiple'), plt.xticks([]), plt.yticks([])

plt.show()
