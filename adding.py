import cv2
import numpy as np

img=cv2.imread('m.jpg')
h,v,b=img.shape[:3]
img1=np.zeros((h,v,b),np.uint8)
# assigning the color to each and every pixel of the image
img1[0:h,0:v]=[166,225,166]
add=img+img1
cv2.imshow('add',add)
cv2.imshow('new',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
