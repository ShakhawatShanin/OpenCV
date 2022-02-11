import cv2 as cv
import numpy as np

img = cv.imread('Resources/color_img.png')
hull_img = img.copy()
contour_img = img.copy()

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray_img, 230, 255, cv.THRESH_BINARY_INV)  # Create a binary thresholded image
contours, hierarchy = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

# Since the image only has one contour, grab the first contour (5 contour)
cnt = contours[0]

# Get the required hull
hull = cv.convexHull(cnt)

# draw the hull
show_hull = cv.drawContours(hull_img, [hull], 0, (0, 0, 220), 3)
cv.imshow("Convex Hull", show_hull)

print(f"hull variable point: ", hull)
print(f"cnt variable point: ", cnt)
cv.waitKey(0)
