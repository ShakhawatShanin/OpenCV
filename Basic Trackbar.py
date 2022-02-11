import numpy as np
import cv2 as cv

def nothing(x):
    print()

img = np.zeros( (500, 500, 3), np.uint8)

cv.namedWindow('image')
cv.createTrackbar('B', 'image', 0, 255, nothing)  # 0=start & 255=ending range
cv.createTrackbar('G', 'image', 0, 255, nothing)  # onChange=called whenever trackbar
cv.createTrackbar('R', 'image', 0, 255, nothing)  # value changes (in this case nothing)

while (1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current bgr values
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    # set current bgr values
    img[:] = [b, g, r]

cv.destroyAllWindows()
