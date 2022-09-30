#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

# open camera
# cap = cv2.VideoCapture('/dev/AMA0', cv2.CAP_V4L)
cap = cv2.VideoCapture(0)
print('camera open')
# set dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# take frame
ret, frame = cap.read()
print(frame)

# write frame to file
cv2.imwrite('AMAimage.jpg', frame)
# release camera
cap.release()
