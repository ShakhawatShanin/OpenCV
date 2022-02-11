import cv2 as cv
import numpy as np

points = []   # store four points coordinate
img = cv.imread('Resources/rotate.jpg')

def getpoints(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append([x, y])
        print(points)
        if len(points) == 4:
            getperspective()
    #cv.imshow('image', img)

def getperspective():
    width = points[1][0] - points[0][0]   # subtract 0_index_first_value from 1_index_first_value
    height = points[2][1] - points[0][1]  # points[0][1] = index 0 & 2 nd value take from points list
    pts1 = np.float32([points[0:4]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    wp_img = cv.warpPerspective(img, matrix, (width, height))
    cv.imshow('output', wp_img)

while True:
    cv.imshow('image', img)
    cv.setMouseCallback('image', getpoints)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

    elif cv.waitKey(1) & 0xff == ord('r'):
        img = cv.imread('Resources/rotate.jpg')
        points = []
        cv.imshow('image', img)
        cv.setMouseCallback('image', getpoints)
    else:
        continue
