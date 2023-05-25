import cv2
import numpy as np
from PIL import Image


img_cv2 = cv2.imread("images/floor plan 7.jpeg", 0)


kernel = np.ones((3, 3), np.uint8)

img_erode = cv2.erode(img_cv2, kernel, iterations=1)
img_erode = cv2.cvtColor(img_erode, cv2.COLOR_BGR2RGB)

# img_dilate = cv2.dilate(img_cv2, kernel, iterations=2)
# img_dilate = cv2.cvtColor(img_dilate, cv2.COLOR_BGR2RGB)

img = Image.fromarray(img_erode).convert("L")
avgColor = np.average(np.array(img.getdata()))
avgColor = 240
img = img.point(lambda x: 255 if x >= avgColor else 0, mode="1")
img.show()

# img2 = Image.fromarray(img_cv2)
# img_denoise = []
# Image.fromarray(
#     cv2.fastNlMeansDenoising(img_cv2, img_denoise, 10, 7, 21))
# # img2.show()
# img_denoise.show()
