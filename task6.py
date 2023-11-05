import cv2 as cv
# from PIL import Image, ImageDraw
from pyzbar.pyzbar import decode

def show_image(name, image):
  window_name = name
  aspect_ratio = image.shape[1] / image.shape[0]
  cv.namedWindow(window_name, cv.WINDOW_NORMAL)
  cv.setWindowProperty(window_name, cv.WND_PROP_ASPECT_RATIO, cv.WINDOW_KEEPRATIO)
  cv.resizeWindow(window_name, 800, int(800 / aspect_ratio))
  cv.imshow(window_name, image)

img = cv.imread('sample/test.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)    
# show_image("gray", gray)
# image = Image.open('sample/1.bmp').convert('RGB')
# draw = ImageDraw.Draw(image)
show_image('thresh', thresh)
for barcode in decode(img):
  print(barcode.data)
    # rect = barcode.rect
    # draw.rectangle(
    #     (
    #         (rect.left, rect.top),
    #         (rect.left+rect.eidth, rect.top+rect.height)
    #     ),
    #     outline='#0080ff'
    # )
    # draw.polygon(barcode.polygon, outline='#e945ff')

# image.save('bar.png')
# image.show()

cv.waitKey()
cv.destroyAllWindows()