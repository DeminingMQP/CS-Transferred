#!/usr/bin/env python
import numpy as np
import cv2
import threading
from pylepton import Lepton
import time

def capture_video():
 with Lepton("/dev/spidev0.0") as l:
    #a = np.zeros((240, 320, 3), dtype=np.uint8)
    lepton_buf = np.zeros((60, 80, 1), dtype=np.uint16)

    last_nr = 0

    while True:
        time.sleep(.1)
        _, nr = l.capture(lepton_buf)
        if nr == last_nr:
            # no need to redo this frame
            continue
        last_nr = nr
        cv2.normalize(lepton_buf, lepton_buf, 0, 65535, cv2.NORM_MINMAX)
        np.right_shift(lepton_buf, 8, lepton_buf)
       # a[:lepton_buf.shape[0], :lepton_buf.shape[1], :] = lepton_buf
	resizedImage = cv2.resize(lepton_buf, (800, 600))
        cv2.imshow('image', np.uint8(resizedImage)) #just overwriting the saved file repeatedly
        cv2.waitKey(1)
if __name__ == '__main__':
   capture_video()