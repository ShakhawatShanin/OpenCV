import cv2 as cv
import numpy as np

# Import image
img = cv.imread('Resources/color_img.png')
cv.imshow("Orginal Image", img)

# Blur the image
blurred_image = cv.GaussianBlur(img, (7,7), 0)

gray_img = cv.cvtColor(blurred_image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray_img)

# Perform adaptive thresholding
binary = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 5)

contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("Number of contours found = {}".format(len(contours)))    # Display all the contours

show_contour = cv.drawContours(img, contours, -1, (0,0,255), 5)     # Draw all the contours
cv.imshow("Contour Image", show_contour)

cv.waitKey(0)
