import cv2                       # BGR
import argparse
import numpy as np
import matplotlib.pyplot as plt  # RGB

"""Thresholding"""

ap = argparse.ArgumentParser()

ap.add_argument("-t", "--thresh", required=True,
                help="Thresh value for threshold func")
args = {
    "thresh": 12
}

img = cv2.imread("bookpage.jpg")

retval, threshold = cv2.threshold(
    img, int(args["thresh"]), 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval_gray, threshold_gray = cv2.threshold(
    grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(
    grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("original", img)
cv2.imshow("threshold", threshold)

cv2.imshow("grayscaled", threshold_gray)
cv2.imshow("gaus", gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
