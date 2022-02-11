import cv2 as cv
import numpy as np
import mediapipe as mp

vdo = cv.VideoCapture('Resources/hand_guitar.mp4')
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
hand = mp_hand.Hands()

allLandmark = []
while True:
    ret, img = vdo.read()
    if not ret:
        break

    imgH, imgW, _ = img.shape
    process = hand.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    if process.multi_hand_landmarks:
        for lm in process.multi_hand_landmarks:
            for i, each_lm in enumerate(lm.landmark):
                x, y = int(each_lm.x * imgW), int(each_lm.y * imgH)  # convert to x y coordinate
                allLandmark.append([i, x, y])
                if i == 4 or i == 8:
                    cv.circle(img, (x, y), 10, (255, 0, 0), cv.FILLED)
            mp_draw.draw_landmarks(img, lm, mp_hand.HAND_CONNECTIONS)

    cv.imshow('Exercise', img)
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break

vdo.release()
cv.destroyAllWindows()
