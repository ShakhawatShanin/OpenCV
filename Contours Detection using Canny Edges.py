import cv2 as cv
import numpy as np

# Import image
img = cv.imread('Resources/color_img.png')
cv.imshow("Orginal Image", img)

# Blur the image
blurred_image = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Blurred Image", blurred_image)

# Apply canny edge detection
edges = cv.Canny(blurred_image, 100, 160)
cv.imshow("Edge Image", edges)

contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("Number of contours found = {}".format(len(contours)))    # Display all the contours

show_contour = cv.drawContours(img, contours, -1, (0,0,255), 5)     # Draw all the contours
cv.imshow("Contour Image", show_contour)

cv.waitKey(0)
