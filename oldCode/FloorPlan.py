from PIL import Image
from PIL import ImageFilter
import numpy as np
import os


class FloorPlan:

    x = (-1, -1, -1, -1, -1,
         -1, 1, 1, 1, -1,
         1, 1, 8, 1, 1,
         -1, 1, 1, 1, -1,
         -1, -1, -1, -1, -1)

    x = (-1, -1, -1,
         -1, 8, -1,
         -1, -1, -1)

    thresh = 175

    def fn(self, x): return 255 if x > self.thresh else 0

    def __init__(self, filename):
        self.filename = filename

        img = Image.open(filename, mode='r').convert("L")

        print(img.size, img.mode)
        self.height = img.height
        self.width = img.width
        # img.show()
        img.filter(ImageFilter.SHARPEN).point(self.fn, mode="1").show()

        img2 = img.filter(ImageFilter.Kernel(
            (3, 3), self.x, scale=1)).convert("1", dither=Image.Dither.NONE).show()

        data = list(img.getdata())
        edge_data = list(img2.getdata())

        self.matrix = np.array(data).reshape(self.height, -1)
        self.edges = np.array(edge_data).reshape(self.height-1)


if __name__ == "__main__":
    filename = "images/1600sqft.jpg"
    # filename = "images/test10x20_2.png"
    fp = FloorPlan(filename)
