# How to Detect Obstacle
## Import Library
import cv2
import numpy as np
from ultralytics import YOLOv10
import math
import time
import supervision as sv


## Setup Database

## UART Mikrokontroler

## Detect Buoy
## Depth Sensor


# Buka dua kamera (stereo)
cap_left = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap_right = cv2.VideoCapture(2, cv2.CAP_DSHOW)

while True:
    retL, frameL = cap_left.read()
    retR, frameR = cap_right.read()

    if not retL or not retR:
        break

    # Konversi ke grayscale
    grayL = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY)

    # Buat stereo depth map
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(grayL, grayR)

    # Tampilkan hasil
    cv2.imshow("Depth Map", disparity)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()


## Capture Image

