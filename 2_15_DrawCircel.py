import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

cv2.circle(image, (350,350), 100, (15,75,50), -1)
cv2.imshow("Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()