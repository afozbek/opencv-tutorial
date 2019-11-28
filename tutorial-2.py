import cv2                       # BGR
import numpy as np
import matplotlib.pyplot as plt  # RGB

"""VIDEO CAPTURING"""

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID" ???
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow("gray", gray)
    cv2.imshow("curr_frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
