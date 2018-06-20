import cv2
import numpy as np

image = cv2.imread('images/Sunflowers.jpg')

# opencv 2.x
# Set up the detector with default parameters.
#detector = cv2.SimpleBlobDetector() 

# opencv 3.x
params = cv2.SimpleBlobDetector_Params()
detector = cv2.SimpleBlobDetector_create(params)

# detect blobs
keypoints = detector.detect(image) #将image图像中检测到的特征点存储起来放在keypoints中

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blobs", blobs)
cv2.waitKey()
cv2.destroyAllWindows()