import cv2
import numpy as np

template_image = cv2.imread("images/4star.jpg", 0)
cv2.imshow("Template Image", template_image)
cv2.waitKey(0)

target_image = cv2.imread("images/shapestomatch.jpg")
target_gray_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(template_image, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray_image, 127, 255, 0)

# Find contours in template
binary, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# We need to sort the contours by area so that we can remove the Largest
# contour which is the image outline 
# 去除外圍的正方形大邊框
stored_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# We extrace the second Largest contour which be our template contour
# 去除外圍的正方形大邊框
template_contour = contours[1]

# Extract contours from second target image
binary, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # Iterate through each contour in the target image and
    # use cv2.matchShapes to compare contour shapes
    # cv2.matchShapes
    # Parameters:	
    #     object1 – First contour or grayscale image.
    #     object2 – Second contour or grayscale image.
    #     method – Comparison method: CV_CONTOURS_MATCH_I1 , CV_CONTOURS_MATCH_I2 or CV_CONTOURS_MATCH_I3 (see the details below).
    #     parameter – Method-specific parameter (not supported now).
    # return: match value(lower values means a closer match) 值越小越相似
    match = cv2.matchShapes(template_contour, c, 1, 0.0) # Match Shapes
    print(match)
    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []

cv2.drawContours(target_image, [closest_contour], -1, (0,255,0), 3)
cv2.imshow("Output Image", target_image)
cv2.waitKey()
cv2.destroyAllWindows() 

# 參考:
# https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?