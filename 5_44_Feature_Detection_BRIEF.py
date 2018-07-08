import cv2
import numpy as numpy

image = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create SURF Feture Detector object
# fast = cv2.FastFeatureDetector()
fast = cv2.FastFeatureDetector_create() #opencv 3

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create() #opencv 3

# obtain key points, by default non max suppression is On
# to turn off set fast.setBooL('nonmaxSuppression', False)
keypoints = fast.detect(gray, None)

keypoints, descriptors = brief.compute(gray, keypoints)
print("Number of keypoints Detected: ", len(keypoints) )

# Draw rich key points on input image
cv2.drawKeypoints(image, keypoints, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Feture Method - BRIEF", image)
cv2.waitKey(0)
cv2.destroyAllWindows()