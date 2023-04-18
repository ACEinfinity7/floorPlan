from scipy.spatial import ConvexHull
from PIL import Image
from PIL import ImageFilter
import numpy as np


filename = "images/1600sqft.jpg"
img = Image.open(filename, mode='r')

blur = img.filter(ImageFilter.FIND_EDGES)

high_freq = np.asarray(blur) - np.asarray(img)
sharpened = Image.fromarray(np.asarray(img) + high_freq)
subtracted = Image.fromarray(high_freq)
img.filter(ImageFilter.FIND_EDGES).show()
# sharpened.show()
