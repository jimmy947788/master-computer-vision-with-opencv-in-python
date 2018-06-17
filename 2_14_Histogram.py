import cv2
import numpy as np

from matplotlib import pyplot as plt

image = cv2.imread('./images/tobago.jpg')

#image:
#channel:BGR影像的B2第一個圖層image[0]
#mask
#histSize:
#range:
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.hist(image.ravel(), 256, [0, 256])
plt.show()

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0, 256])

plt.show()

cv2.imshow("Tabogo", image)
cv2.waitKey(0)