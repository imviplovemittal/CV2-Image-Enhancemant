import cv2
import numpy as np

img=cv2.imread('m.jpg')
h,v,b=img.shape[:3]
mask=np.zeros((h,v,b),np.uint8)
res=np.zeros((h,v,b),np.uint8)
#defining color range
lo=np.array([0,0,0])
hi=np.array([125,125,125])

# code to filter the color range varying from lo to hi
#if color lies in given range then mask equal to that pixel value else it is black
for i in range(0,h):
    for j in range(0,v):
        z=img[i,j]
        if z[0]>=lo[0] and z[1]>=lo[1] and z[2]>=lo[2] and z[0]<=hi[0] and z[1]<=hi[1] and z[2]<=hi[2]:
            mask[i,j]=img[i,j]
cv2.imshow('img2',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
