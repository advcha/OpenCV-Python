import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('images/star.jpg',0)   #white rectangle over black background and convert to gray
ret,thresh=cv2.threshold(img,127,255,0) #apply threshold to the gray image
im2,contours,hierarchy=cv2.findContours(thresh,1,2)   #get contours

cnt = contours[0]
M = cv2.moments(cnt)
#print(M)
#{'m20': 224951289.91666666, 'm11': 225898240.4583333, 'm03': 41461396222.9, 'nu03': 0.0003117907381246693, 'mu03': 5305710.780441284, 'm02': 261116335.75, 'mu21': -7359098.804995537, 'm10': 1607978.1666666665, 'm30': 33382219903.050003, 'nu12': 3.99595900714717e-06, 'mu20': 15921516.322204947, 'm01': 1737746.0, 'mu30': 137846.20304107666, 'nu02': 0.11102109065061784, 'm21': 31595031899.13333, 'mu02': 16986729.822840452, 'm00': 12369.5, 'm12': 33943779712.1, 'nu30': 8.100548856205404e-06, 'nu20': 0.10405911704830025, 'nu21': -0.00043245833466842176, 'nu11': -4.936021676545615e-06, 'mu11': -755.2336779236794, 'mu12': 67998.82161331177}

#find centroid (center of gravity???) cx and cy
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#print(cx,cy)
#129 140

#find area
area = cv2.contourArea(cnt)
#print(area)
#12369.5

#find perimeter or arc length
perimeter = cv2.arcLength(cnt,True)
#print(perimeter)
#796.9087181091309
