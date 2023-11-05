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

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# show_image('hsv', hsv)

lower_yellow = np.array([[[ 20, 50, 50]]])
upper_yellow = np.array([[[ 60, 255, 255]]])

# lower_yellow = np.array([[[ 80, 50, 50]]])
# upper_yellow = np.array([[[ 130, 255, 255]]])

# lower_yellow = np.array([[[ 0, 50, 50]]])
# upper_yellow = np.array([[[ 20, 255, 255]]])

mask = cv.inRange(hsv, lower_yellow, upper_yellow)
# show_image('mask', mask)

# res = cv.bitwise_and(img, img, mask)
# show_image('res', res)

# gray = cv.cvtColor(mask, cv.COLOR_HSV2BGR)
# show_image('gray', gray) 

_, thresh = cv.threshold(mask, 0, 255, cv.THRESH_OTSU)
# show_image('thresh', thresh)

kernel = np.ones((6, 6), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
# show_image('opening', opening)

contours, _ = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img_cnt = img.copy()
# cv.drawContours(img_cnt, contours, -1, (0,255,0), 5)
# show_image('img_cnt', img_cnt)

perimeter = int(img.shape[1]/8)*4
print(perimeter)

lengths = []
for cnt in contours:
  length = cv.arcLength(cnt, True)
  lengths.append(length)
print(lengths)
idx = lengths.index(max(lengths))

idxs = []
for i in range(0, len(contours)):
  if lengths[i] > lengths[idx]*0.75:
    idxs.append(i)
print(idxs)

for j in idxs:
  c = contours[j]
  x, y, w, h = cv.boundingRect(c)
  cv.rectangle(img_cnt, (x, y), (x+w, y+h), (0,255,0), 10)
  # cv.drawContours(img_cnt, [c], 0, (0,255,0), 10)
show_image('img_cnt', img_cnt)

cv.waitKey(0)
cv.destroyAllWindows()