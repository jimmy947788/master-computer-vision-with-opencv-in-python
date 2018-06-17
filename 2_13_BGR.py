import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

B, G, R = cv2.split(image)
print(B.shape)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

merged = cv2.merge([B + 100, G, R])
cv2.imshow("Merged with Blue Amplified", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()