import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

B, G, R = cv2.split(image)

print("image.shape=", image.shape)
zeros = np.zeros(image.shape[:2], dtype = 'uint8')

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()