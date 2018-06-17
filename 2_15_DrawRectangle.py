import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(image, (100, 100), (300,250), (127, 50, 127), 5 )
cv2.imshow("Rectangle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()