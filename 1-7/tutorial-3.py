import cv2                       # BGR
import numpy as np
import matplotlib.pyplot as plt  # RGB

"""Drawing and Writing on Image"""

# grayscaled image
img = cv2.imread("furkan.jpg", cv2.IMREAD_GRAYSCALE)

# Çizgi, elips silindir, veya text bile yazabiliriz. Bunu kendi projemizde kullanabiliriz
cv2.line(img, (0, 0), (150, 150), (255, 255, 255),
         thickness=15)
cv2.rectangle(img, (0, 0), (15, 25), (0, 255, 0),
              thickness=5)
cv2.circle(img, (100, 63), 55, (0, 255, 255), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)

cv2.polylines(img, [pts], True, (0, 255, 255), 5)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, "Deep Crash", (520, 310), font,
            5, (255, 255, 255), 5, cv2.LINE_AA)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
