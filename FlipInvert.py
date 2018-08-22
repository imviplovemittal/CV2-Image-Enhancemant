import cv2
import numpy as np

img=cv2.imread('m.jpg')
h,v,b=img.shape[:3]
img1=np.zeros((h,v,b),np.uint8)
img2=np.zeros((h,v,b),np.uint8)
#to flip the image
for i in range(0,h):
    for j in range(0,v):
        img1[i,j]=img[h-1-i,v-j-1]
#to invert the image
for i in range(0,h):
    for j in range(0,v):
        img2[i,j]=255-img[i,j]
cv2.imshow('img2',img2)
cv2.imshow('img1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
