import cv2 as cv
import numpy as np
import imutils
import scipy.spatial.distance as dist

def calculate_mid(ptX, ptY):
    return ((ptX[0]+ptY[0])/2, (ptX[1]+ptY[1])/2)

# LOAD, CONVERT TO GRAY and THRESH IMAGE
img = cv.imread('Resources/color_img.png')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh, thrash_img = cv.threshold(gray_img, 200, 255, cv.CHAIN_APPROX_NONE)
cv.imshow('GRAY IMAGE', thrash_img)

# FIND TOTAL CONTOUR
contours = cv.findContours(thrash_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # may be missing all the contours
print('Total Contours (without imutils): ', len(contours))
contours = imutils.grab_contours(contours)     # find all contours
print('Total Contours (with imutils): ', len(contours))

blank_img = np.zeros(img.shape)  # Create blank image

for contour in contours:
    if cv.contourArea(contour) < 300:
       continue

    # PRINT COORDINATE POINT OF ALL CONTOUR
    min_rect = cv.minAreaRect(contour)
    min_rect = cv.boxPoints(min_rect)   # convert to the points
    min_rect = np.array(min_rect, dtype='int')  # AS INTEGER
    print(min_rect)

    cv.drawContours(blank_img, contours, -1, (255, 255, 255), 3)  # Print contours in blank image
    cv.drawContours(blank_img, [min_rect], -1, (0, 0, 255), 2)  # Print border sorround the contours

    FONT = cv.FONT_HERSHEY_SIMPLEX
    for (x, y) in min_rect:   # x & y store each corner point coordinate of a contour
        cv.circle(blank_img, (x, y), 2, (255, 0, 0), 2)   # draw circle at corner to each contour
        (tl, tr, br, bl) = min_rect

        # CALCULATE MID POINTS OF RECTANGLE
        (top_midX, top_midY) = calculate_mid(tl, tr)
        (btm_midX, btm_midY) = calculate_mid(bl, br)
        (left_midX, left_midY) = calculate_mid(tl, bl)
        (right_midX, right_midY) = calculate_mid(tr, br)

        # DRAW MID-POINTS & LINE
        cv.circle(blank_img, (int(top_midX), int(top_midY)), 1, (255, 0, 0), 2)
        cv.circle(blank_img, (int(btm_midX), int(btm_midY)), 1, (255, 0, 0), 2)
        cv.line(blank_img, (int(top_midX), int(top_midY)), (int(btm_midX), int(btm_midY)), (255, 255, 0), 1)

        cv.circle(blank_img, (int(left_midX), int(left_midY)), 1, (255, 0, 0), 2)
        cv.circle(blank_img, (int(right_midX), int(right_midY)), 1, (255, 0, 0), 2)
        cv.line(blank_img, (int(left_midX), int(left_midY)), (int(right_midX), int(right_midY)), (255, 255, 0), 1)


        # CALCULATE DISTANCE BASED ON MID POINTS
        hight_dist = dist.euclidean((top_midX, top_midY), (btm_midX, btm_midY))
        width_dist = dist.euclidean((left_midX, left_midY), (right_midX, right_midY))

        cv.putText(blank_img, "{:.1f} px".format(hight_dist), (int(top_midX-10), int(top_midY-10)), FONT, 0.4, (255, 255, 255), 1)
        cv.putText(blank_img, "{:.1f} px".format(width_dist), (int(right_midX+10), int(right_midY+10)), FONT, 0.4, (255, 255, 255), 1)

cv.imshow('Contour Image', blank_img)
cv.waitKey(0)

# find contours -> draw min rectangle on contours -> find corner point of min rec -> calculate mid points (4) -> calculate size based on mid points
