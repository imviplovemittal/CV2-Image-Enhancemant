import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg',0)
hist, bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()

def make_plot(img,legend):
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend((legend,), loc = 'upper left')
    plt.show()

make_plot(img,"unequalised")

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
cv2.imwrite('img2.png',img2)

res1 = np.hstack((img,img2))
cv2.imwrite('res1.png',res1)

make_plot(img2,"equalised")
