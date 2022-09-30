#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
while True:
    cap = cv2.VideoCapture('/dev/AMA0', cv2.CAP_V4L)
    print("cap")

    while cap.isOpened():
        print('read')
        ret, img = cap.read()
        print(ret)
        if ret:
            print("camera found")
            cv2.imshow('camera-0',img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            print('no camera')
            break
    break
cap.release()
cv2.destroyAllWindows()
