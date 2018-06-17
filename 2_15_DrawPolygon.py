import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

pts = np.array([
    [10, 50],
    [400, 50],
    [90, 200],
    [50, 500],
], np.int32)

pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True, (0,0,255), 3)
cv2.imshow("Polygon", image)

cv2.waitKey(0)
cv2.destroyAllWindows()