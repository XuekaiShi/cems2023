import cv2 as cv
import numpy as np

def show_image(name, image):
  window_name = name
  aspect_ratio = image.shape[1] / image.shape[0]
  cv.namedWindow(window_name, cv.WINDOW_NORMAL)
  cv.setWindowProperty(window_name, cv.WND_PROP_ASPECT_RATIO, cv.WINDOW_KEEPRATIO)
  cv.resizeWindow(window_name, 800, int(800 / aspect_ratio))
  cv.imshow(window_name, image)

img = cv.imread('sample/test.bmp')
# show_image("img", img)

# 灰度
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
show_image("gray", gray)

# 任务二
img_resize = cv.resize(img, (1224, 1024                                                                                                               ))
cv.imwrite('resize.bmp', img_resize)

cv.waitKey(0)
cv.destroyAllWindows()

