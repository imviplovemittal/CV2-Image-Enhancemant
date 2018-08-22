import cv2
import numpy

img = cv2.imread('m.jpg',0)
img1 = cv2.imread('m.jpg')

cv2.imshow('image',img)
cv2.imshow('image1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
