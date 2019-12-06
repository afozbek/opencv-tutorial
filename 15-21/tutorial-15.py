import cv2                       # BGR
import numpy as np
import os
import argparse

"""MOG Background Reduction"""

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file", required=True, help="The path of the data")

args = vars(ap.parse_args())

cap = cv2.VideoCapture(os.getcwd() + args["file"])
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow("original", frame)
    cv2.imshow("fg", fgmask)

    if cv2.waitKey(30) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
