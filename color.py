# 看 hsv 色彩空间下的各颜色
import cv2 as cv
import numpy as np

yellow = np.uint8([[[0,255, 255]]])
blue = np.uint8([[[255, 0, 0]]])
red = np.uint8([[[0, 0, 255]]])

y_hsv = cv.cvtColor(yellow, cv.COLOR_BGR2HSV)
b_hsv = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
r_hsv = cv.cvtColor(red, cv.COLOR_BGR2HSV)

print(y_hsv)
print(b_hsv)
print(r_hsv)


# [[[ 30 255 255]]]
# [[[120 255 255]]]
# [[[  0 255 255]]]