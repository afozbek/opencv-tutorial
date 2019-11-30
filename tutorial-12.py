import cv2                       # BGR
import numpy as np
import matplotlib.pyplot as plt

"""GrapCut Foreground Extractions"""

img = cv2.imread("furkan.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (30, 30, 1750, 1750)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img*mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
