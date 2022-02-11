import cv2 as cv
import numpy as np
ans_key = [2, 0, 1, 0, 2]

img = cv.imread('Resources/mark.png')
copy_img = img.copy()
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh_img = cv.threshold(gray_img, 240, 255, cv.CHAIN_APPROX_NONE)
contours, hierarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cv.drawContours(copy_img, contours, -1, (0, 0, 255), 1)

rows = np.vsplit(thresh_img, 6)  # split image into 6 part (marks also)
rows = np.delete(rows, 5, 0)     # delete marks split part
cv.imshow('Row', rows[4])
boxes = []                       # collection of all cell / single box
for row in rows:
    cols = np.hsplit(row, 4)
    for box in cols:
        boxes.append(box)
cv.imshow('Box', boxes[2])

pixel_list = np.zeros((5, 4))   # create 2d matrix (#question, #choice)
x = y = 0
for box in boxes:               # store pixel value of individual boxes
    pixel_val = cv.countNonZero(box)
    pixel_list[x][y] = pixel_val
    y += 1
    if (y == 4):
        x += 1
        y = 0
print(pixel_list)

idx = []
for i in range(0, 5):           # store just max pixel value of individual boxes
    arr = pixel_list[i]
    idx_val = np.where(arr == np.amax(arr))
    idx.append(idx_val[0][0])
print(idx)

grade = 0
for i in range(0, 5):           # compare with answer key
    if ans_key[i] == idx[i]:
        grade += 1
print('Total correct answer: ', grade)

cv.imshow('Orginal Image', img)
cv.imshow('Contour Image', copy_img)
cv.imshow('Gray Image', gray_img)
cv.imshow('Thresh Image', thresh_img)

cv.waitKey(0)
cv.destroyAllWindows()
