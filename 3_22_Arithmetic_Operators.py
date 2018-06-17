import cv2
import numpy as np

image = cv2.imread("images/input.jpg")

# 建構一個矩陣大小和原始圖片一樣，裡面的值都為1
# 乘上75讓菌鎮裡面都為75
M = np.ones(image.shape, dtype = "uint8") * 75
print(M)

added = cv2.add(image, M)
cv2.imshow("Added", added)

subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey()
cv2.destroyAllWindows()

