import cv2 as cv
import numpy as np
import mediapipe as mp

vdo = cv.VideoCapture('Resources/finger_count.mp4')
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

            tips_idx = [4, 8, 12, 16, 20]
            if len(allLandmark) != 0:
                finger_status = []

                if allLandmark[tips_idx[0]][1] > allLandmark[tips_idx[0]-1][1]:   # THUMP FINGER
                    finger_status.append(1)
                else:
                    finger_status.append(0)
                for i in range(1, 5):       # ALL FINGER EXCEPT THUMP FINGER
                    if allLandmark[tips_idx[i]][2] < allLandmark[tips_idx[i]-2][2]:
                        finger_status.append(1)
                    else:
                        finger_status.append(0)

                print(finger_status)
                print(finger_status.count(1))


            mp_draw.draw_landmarks(img, lm, mp_hand.HAND_CONNECTIONS)

            cv.putText(img, " Total Fingers: ", (10, 25), cv.FONT_HERSHEY_COMPLEX, 1, (20, 255, 155), 2)
            cv.putText(img, str(sum(finger_status)), (imgW // 2 + 150, 240), cv.FONT_HERSHEY_SIMPLEX, 8.9, (20, 255, 155), 10, 10)

    cv.imshow('Exercise', img)
    allLandmark.clear()
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break

vdo.release()
cv.destroyAllWindows()
