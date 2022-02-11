import cv2 as cv
import numpy as np
vehicle_counter = 0
vdo = cv.VideoCapture('Resources/car_passing.mp4')

bgObj = cv.createBackgroundSubtractorMOG2(detectShadows=True)   # Initialize the background object

while True:
    ret, frame = vdo.read()

    if not ret:
        break

    fgMask = bgObj.apply(frame)   # obj (binary) + shadows (gray)
    _, fgMask = cv.threshold(fgMask, 250, 255, cv.THRESH_BINARY)    # Get pure binary image | increasing white foreground

    fgMask = cv.erode(fgMask, None, iterations=1)    # remove noise
    fgMask = cv.dilate(fgMask, None, iterations=2)

    frameCopy = frame.copy()
    cv.line(frameCopy, (50, 250), (550, 250), (0, 255, 0), 3)   # draw reference line
    contours, _ = cv.findContours(fgMask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)      # Detect contours in the frame.


    for cnt in contours:
        if cv.contourArea(cnt) > 400:   # remove little contours (noise)
            x, y, w, h = cv.boundingRect(cnt)  # Retrieve the bounding box coordinates from the contour
            cv.rectangle(frameCopy, (x, y), (x+w, y+h), (0, 0, 255), 2)   # Draw a bounding box around the car
            cntXMidCoordinate = int((x + (x+w)) / 2)
            cntYMidCoordinate = int((y + (y+h)) / 2)
            cv.circle(frameCopy, (cntXMidCoordinate, cntYMidCoordinate), 2, (0, 0, 255), 2)

            if (cntYMidCoordinate > 248) and (cntYMidCoordinate < 252):
                vehicle_counter += 1

    cv.putText(frameCopy, 'Total Vehicles: {}'.format(vehicle_counter), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

    fgReal = cv.bitwise_and(frame, frame, mask=fgMask)   # Extract the foreground from the frame using the segmented mask
    stacked = np.hstack((frame, fgReal, frameCopy))
    cv.imshow('Original Frame, Extracted Foreground and Detected Cars', cv.resize(stacked, None, fx=0.5, fy=0.5))

    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break
vdo.release()

cv.destroyAllWindows()

# if prevFrame & currFrame center point value belongs reference line then count vehicle
