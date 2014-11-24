#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import subprocess


cap = cv2.VideoCapture(0)

INFILE = '/Volumes/RAM Disk/in.bmp'
OUTFILE = '/Volumes/RAM Disk/out.bmp'

while(True):
    _, img = cap.read()

    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    cv2.imwrite(INFILE, img)
    subprocess.Popen(['convert', INFILE, '-ordered-dither', 'h4x4o', '-quantize', 'GRAY', '-colors', '6', OUTFILE]).wait()
    frame = cv2.imread(OUTFILE)

    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()
