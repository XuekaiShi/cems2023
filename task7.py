import cv2 as cv
import numpy as np

img = cv.imread('sample/test.bmp')
img_cnt = img.copy()

def show_image(name, image):
    window_name = name
    aspect_ratio = image.shape[1] / image.shape[0]
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.setWindowProperty(
        window_name, cv.WND_PROP_ASPECT_RATIO, cv.WINDOW_KEEPRATIO)
    cv.resizeWindow(window_name, 800, int(800 / aspect_ratio))
    cv.imshow(window_name, image)

def find_pos(cnt):
    perimeter = cv.arcLength(cnt,True)
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    if cx < img.shape[1]//2 - perimeter/8:
        if cy < img.shape[0]//2 - perimeter/8:
            return 1
        elif cy > img.shape[0]//2 + perimeter/8:
            return 7
        else:
            return 4
    elif cx > img.shape[1]//2 + perimeter/8:
        if cy < img.shape[0]//2 - perimeter/8:
            return 3
        elif cy > img.shape[0]//2 + perimeter/8:
            return 9
        else:
            return 6
    else:
        if cy < img.shape[0]//2 - perimeter/8:
            return 2
        elif cy > img.shape[0]//2 + perimeter/8:
            return 8
        else:
            return 5

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_yellow = np.array([[[20, 50, 50]]])
upper_yellow = np.array([[[60, 255, 255]]])

lower_blue = np.array([[[80, 50, 50]]])
upper_blue = np.array([[[130, 255, 255]]])

lower_red = np.array([[[0, 50, 50]]])
upper_red = np.array([[[20, 255, 255]]])

mask_y = cv.inRange(hsv, lower_yellow, upper_yellow)
mask_b = cv.inRange(hsv, lower_blue, upper_blue)
mask_r = cv.inRange(hsv, lower_red, upper_red)

_, thresh_y = cv.threshold(mask_y, 0, 255, cv.THRESH_OTSU)
_, thresh_b = cv.threshold(mask_b, 0, 255, cv.THRESH_OTSU)
_, thresh_r = cv.threshold(mask_r, 0, 255, cv.THRESH_OTSU)

kernel = np.ones((6, 6), np.uint8)
opening_y = cv.morphologyEx(thresh_y, cv.MORPH_OPEN, kernel)
opening_b = cv.morphologyEx(thresh_b, cv.MORPH_OPEN, kernel)
opening_r = cv.morphologyEx(thresh_r, cv.MORPH_OPEN, kernel)

contours_y, _ = cv.findContours(
    opening_y, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours_b, _ = cv.findContours(
    opening_b, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours_r, _ = cv.findContours(
    opening_r, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

lengths_y = []
for cnt in contours_y:
    length = cv.arcLength(cnt, True)
    lengths_y.append(length)
print(lengths_y)
if (len(lengths_y) > 0):
    idx_y = lengths_y.index(max(lengths_y))

lengths_b = []
for cnt in contours_b:
    length = cv.arcLength(cnt, True)
    lengths_b.append(length)
print(lengths_b)
if (len(lengths_b) > 0):
    idx_b = lengths_b.index(max(lengths_b))

lengths_r = []
for cnt in contours_r:
    length = cv.arcLength(cnt, True)
    lengths_r.append(length)
print(lengths_r)
if (len(lengths_r) > 0):
    idx_r = lengths_r.index(max(lengths_r))


idxs_y = []
for i in range(0, len(contours_y)):
    if lengths_y[i] > lengths_y[idx_y]*0.75:
        idxs_y.append(i)
print(idxs_y)

idxs_b = []
for i in range(0, len(contours_b)):
    if lengths_b[i] > lengths_b[idx_b]*0.75:
        idxs_b.append(i)
print(idxs_b)

idxs_r = []
for i in range(0, len(contours_r)):
    if lengths_r[i] > lengths_r[idx_r]*0.75:
        idxs_r.append(i)
print(idxs_r)


for j in idxs_y:
    c = contours_y[j]
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img_cnt, (x, y), (x+w, y+h), (0, 255, 0), 10)
    poss = find_pos(c)
    cv.putText(img_cnt, str(poss), (x+10, y+10), color=(0, 255, 0),
               fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=3.0, thickness=10)
    # cv.drawContours(img_cnt, [c], 0, (0,255,0), 10)

for j in idxs_b:
    c = contours_b[j]
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img_cnt, (x, y), (x+w, y+h), (0, 255, 0), 10)
    poss = find_pos(c)
    cv.putText(img_cnt, str(poss), (x+10, y+10), color=(0, 255, 0),
               fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=3.0, thickness=10)
    # cv.drawContours(img_cnt, [c], 0, (0,255,0), 10)

for j in idxs_r:
    c = contours_r[j]
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img_cnt, (x, y), (x+w, y+h), (0, 255, 0), 10)
    poss = find_pos(c)
    cv.putText(img_cnt, str(poss), (x+10, y+10), color=(0, 255, 0),
               fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=3.0, thickness=10)

show_image('img_cnt', img_cnt)

cv.waitKey(0)
cv.destroyAllWindows()
