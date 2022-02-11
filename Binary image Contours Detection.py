import cv2 as cv
import numpy as np

# Import image
img = cv.imread('Resources/gray_img.png')
cv.imshow("Orginal Image", img)

# Convert orginal image to gray-scale image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray_img)

# Find all contours in the image.
contours, hierarchy = cv.findContours(gray_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("Number of contours found = {}".format(len(contours)))    # Display all the contours

show_contour = cv.drawContours(img, contours, -1, (0,0,255), 5)     # Draw all the contours
cv.imshow("Contour Image", show_contour)

cv.waitKey(0)