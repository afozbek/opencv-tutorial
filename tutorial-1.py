import cv2                       # BGR
import numpy as np
import matplotlib.pyplot as plt  # RGB

"""INTRODUCTION TO OPENCV AND MATPLOTLIB"""

# Grayscale çok daha basitleştirilmiş hali
img = cv2.imread("furkan.jpg", cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR - 1
# GRAYSCALE - 0
# IMREADE_UNCHANGED - -1

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.plot([50, 100], [80,])
# plt.show()

cv2.imwrite("furkan.png", img)
