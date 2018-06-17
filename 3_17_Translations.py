import cv2
import numpy as np

image = cv2.imread("images/input.jpg")

height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#     | 1 0 Tx |
# T = | 0 1 Ty |

# T is our translation matrix
T = np.float32([
    [ 1, 0, quarter_width],
    [ 0, 1, quarter_height],
])
print(T)

img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow("Traslation", img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()