import cv2 as cv
import numpy as np

img = cv.imread('Resources/gray_img.png')
img_copy = img.copy()   # use for "bounding rectangle" function
imageGray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
contours, hierarchy = cv.findContours(imageGray, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

# Get the bounding rectangle | x=top-left corner, y=top-left corner
x, y, w, h = cv.boundingRect(contours[2])  # w=width of the rectangle, h=height of the rectangle
# Draw the rectangle around the object
show_rec_contour = cv.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 3)
cv.imshow("Rectangle boundary", show_rec_contour)
show_rec_contour_area = cv.contourArea(contours[2])
print(f"Rectangle area: ", show_rec_contour_area)

# calculate the minimum area Bounding rectangle
rect = cv.minAreaRect(contours[2])
# convert the rectangle object to box points
box = cv.boxPoints(rect).astype('int')
# Draw a both rectangle around the object
min_rec_boundary = cv.drawContours(img, [box], 0, (0, 255, 0), 3)   # use img for "min bounding rectangle" function
cv.imshow("Minimum rectangle boundary", min_rec_boundary)
show_min_rec_contour_area = cv.contourArea(contours[2])
print("Min rectangle area: ", show_min_rec_contour_area)

show_both_contour = cv.rectangle(img, (x, y), (x+w, y+h), (0,0, 255), 3)
cv.imshow("Both Image", show_both_contour)

cv.waitKey(0)
