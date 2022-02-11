import cv2 as cv
import numpy as np

img = cv.imread('Resources/gray_img.png')

imageGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

contours, hierarchy = cv.findContours(imageGray, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

# Sort the contours in decreasing order
sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)

# Draw largest 3 contours
for i, cont in enumerate(sorted_contours[:3], 1):
    show_contour = cv.drawContours(img, cont, -1, (0, 255, 0), 3)  # Draw the contour
    cv.imshow("Contour Image", show_contour)

    # Display the position of contour in sorted list
    cv.putText(img, str(i), (cont[0, 0, 0], cont[0, 0, 1] - 10), cv.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 4)

cv.waitKey(0)
