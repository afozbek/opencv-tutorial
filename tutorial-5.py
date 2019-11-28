import cv2                       # BGR
import numpy as np
import matplotlib.pyplot as plt  # RGB

"""Image Arithmetics and Logic"""

img1 = cv2.imread("3D-Matplotlib.png")
img2 = cv2.imread("linear.png")
logo = cv2.imread("mainlogo.png")

# (155, 100, 200) + (100, 155, 155) = 255, 255, 355 translated to (255, 255, 255) -> white

# add = img1 + img2
# add = cv2.add(img1, img2)
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# cv2.imshow("weighted", weighted)

# MAIN LOGO PART
rows, cols, channels = logo.shape
roi = img1[0:rows, 0:cols]  # REGION OF IMAGE

img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# mask -> istenmeyen kısımlar siyah gerisi beyaz

mask_inv = cv2.bitwise_not(mask)
# mask_inv -> istenmeyen kısımlar beyaz gerisi siyah

# python logosu siyah 0, 0, 0 diğer kısımlar 255, 255, 255
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# python logosu asıl halinde diğer kısımlar önemsiz
img2_fg = cv2.bitwise_and(logo, logo, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst

# cv2.imshow("res", mask)
cv2.imshow("mask", mask)
cv2.imshow("mask_inv", mask_inv)
cv2.imshow("img1_bg", img1_bg)
cv2.imshow("img2_fg", img2_fg)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
