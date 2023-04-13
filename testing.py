from PIL import Image


filename = "1600sqft.jpg"

img = Image.open(filename, mode='r')


thresh = 150
def fn(x): return 255 if x > thresh else 0


r = img.convert('L').point(fn, mode='1')
r.show()
