import cv2 as cv
import numpy as np

img = cv.imread('Resources/gray_img.png')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thrash = cv.threshold(gray_img, 240, 255, cv.CHAIN_APPROX_NONE)
contours, hierarchy = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    cv.drawContours(img, contour, 0, (0, 0, 0), 5)
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    x, y, w, h = cv.boundingRect(approx)

    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 4:
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv.waitKey(0)
