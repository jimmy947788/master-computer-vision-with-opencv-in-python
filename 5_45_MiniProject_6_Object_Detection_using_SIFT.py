import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Load out image template, thisis our reference image
image_template = cv2.imread("images/box_in_scene.png")
