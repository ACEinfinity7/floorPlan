from PIL import Image
from PIL import ImageFilter
import smartcrop
import json
import numpy as np

# filename = "images/1600sqft.jpg"

# img = Image.open(filename, mode='r').filter(
#     ImageFilter.UnsharpMask()).filter(ImageFilter.EDGE_ENHANCE)
# img.show()

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8]

l1.extend(l2)
print(l1)


# img2 = img.filter(ImageFilter.SHARPEN)
# thresh = 150
# def fn(x): return 255 if x > thresh else 0


# r = img2.point(fn, mode='1')
# r.show()


# filename = "images/1600sqft.jpg"
# img = Image.open(filename).convert("RGB")
# sc = smartcrop.SmartCrop()
# res = sc.crop(img, 500, 500)
# # print(json.dumps(res, indent=2))
# for entry in res:
#     print(res[entry])
u = 2.3522
v = 48.8566

print(f'theta: {u*np.pi/180 + 2*np.pi} phi: {np.abs((v-90)*np.pi/180)}')
print(np.pi/2)
