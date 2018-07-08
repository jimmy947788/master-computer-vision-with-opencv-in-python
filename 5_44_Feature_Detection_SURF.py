import cv2
import numpy as numpy

image = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create SURF Feture Detector object
# surf = cv2.SURF()
surf = cv2.xfeatures2d.SURF_create() #opencv 3

# Only fetures, whose hessian is larger then hessianThreshold are retained by the detector
surf.setHessianThreshold(7500) 
keypoints, descriptors = surf.detectAndCompute(gray, None)
print("Number of keypoints Detected: ", len(keypoints) )

# Draw rich key points on input image
cv2.drawKeypoints(image, keypoints, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Feture Method - SURF", image)
cv2.waitKey(0)
cv2.destroyAllWindows()