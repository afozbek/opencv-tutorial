import cv2                       # BGR
import numpy as np
import matplotlib.pyplot as plt  # RGB

"""Image Operations"""

img = cv2.imread("furkan.jpg", cv2.IMREAD_COLOR)

img[55, 55] = [255, 255, 255]
px = img[55, 55]

# Region of Image
# Converting some pixels to white
img[1400:1600, 1400:1600] = [255, 0, 0]

# copy paste some places
watch_face = img[500:1500, 500:1500]
img[0:1000, 0:1000] = watch_face

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
