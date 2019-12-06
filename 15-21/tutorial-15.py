import cv2                       # BGR
import numpy as np

"""MOG Background Reduction"""

cap = cv2.VideoCapture(0)
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
