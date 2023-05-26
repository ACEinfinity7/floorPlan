from PIL import Image, ImageFilter, ImageOps
import numpy as np
import sys
from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull
from enum import Enum
import cv2
from celluloid import Camera


class Anim:

    def __init__(self, img: Image, width, height) -> None:
        self.xFrames = []
        self.yFrames = []
        self.width, self.height = width,  height
        self.img = img


class FileLoader:
    CONV_KERNEL = [1, 1, 1,
                   1, -9, 1,
                   1, 1, 1]
    CONV_KERNEL_DIM = (3, 3)

    CV2_KERNEL_ERODE = np.ones((3, 3), np.uint8)
    CV2_KERNEL_DILATE = np.ones((3, 3), np.uint8)

    KERNEL_SCALE = 1
    KERNEL_OFFSET = 2
    DILATE_ITERATIONS = 1
    EROSION_ITERATIONS = 1

    FILTER_STRENGTH = 10
    TEMPLATE_WINDOW_SIZE = 7
    SEARCH_WINDOW_SIZE = 21

    def __init__(self, filename: str) -> None:
        self.img = Image.open(filename, mode='r').convert("L")
        self.height, self.width = self.img.height, self.img.width

    def convolute(self) -> 'FileLoader':
        self.img = self.img.filter(ImageFilter.kernel(
            self.X_dim, self.X, scale=self.KERNEL_SCALE, offset=self.KERNEL_OFFSET))

        return self

    def erode(self) -> 'FileLoader':
        imgCV2 = np.array(self.img.convert("RGB"))[:, :, ::-1].copy()
        eroded = cv2.erode(
            imgCV2, self.CV2_KERNEL_ERODE, iterations=self.EROSION_ITERATIONS)
        eroded = cv2.cvtColor(eroded, cv2.COLOR_BGR2RGB)
        self.img = Image.fromarray(eroded).convert("L")

        return self

    def dilate(self) -> 'FileLoader':
        imgCV2 = np.array(self.img.convert("RGB"))[:, :, ::-1].copy()
        dilated = cv2.dilate(
            imgCV2, self.CV2_KERNEL_DILATE, iterations=self.DILATE_ITERATIONS)
        dilated = cv2.cvtColor(dilated, cv2.COLOR_BGR2RGB)
        self.img = Image.fromarray(dilated).convert("L")

        return self

    def black_and_white(self, threshold: int = -1) -> 'FileLoader':
        if (threshold == -1):
            threshold = np.average(np.array(self.img.getdata()))

        self.img = self.img.point(
            lambda x: 255 if x >= threshold else 0, mode="1")

        return self

    def sharpen(self) -> 'FileLoader':
        self.img = self.img.filter(ImageFilter.SHARPEN)

        return self

    def denoise(self) -> 'FileLoader':
        imgCV2 = np.array(self.img.convert("RGB"))[:, :, ::-1].copy()
        denoised = []
        denoised = cv2.fastNlMeansDenoising(imgCV2, None, self.FILTER_STRENGTH,
                                            self.TEMPLATE_WINDOW_SIZE, self.SEARCH_WINDOW_SIZE)
        denoised = cv2.cvtColor(denoised, cv2.COLOR_BGR2RGB)
        self.img = Image.fromarray(denoised).convert("L")

        return self

    def get_data(self) -> list:
        data = self.img.getdata()
        matrix = np.array(data).reshape(self.height, -1)
        return list(matrix)

    def get_image(self) -> Image:
        return self.img.copy()


class FloorPlan:

    ANIMATE = False

    def _traverse(self, x, y):
        #  print(x, y)
        if self.visited[y][x] != 0:
            return

        if self.matrix[y][x] == 0:
            return

        self.visited[y][x] = 1

        if y < self.height-1:
            # print("went up")
            self._traverse(x, y+1)
            if (x > 1):
                # bottom left
                self._traverse(x-1, y+1)
            if (x < self.width-1):
                # bottom right
                self._traverse(x+1, y+1)
        # up
        if y > 1:
            self._traverse(x, y-1)
            if (x > 1):
                # up left
                self._traverse(x-1, y-1)
            if (x < self.width-1):
                # up right
                self._traverse(x+1, y-1)
        # left
        if x > 1:
            self._traverse(x-1, y)
        # right
        if x < self.width-1:
            self._traverse(x+1, y)

    def __init__(self, matrix: list, scale: int = 10) -> None:
        self.matrix = matrix
        self.scale = scale
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.visited = np.zeros((self.height, self.width), np.int8)

        sys.setrecursionlimit(self.width * self.height)

        self._traverse(0, 0)

        self.pts = []  # list of tuples (x,y)
        for y in range(self.height):
            for x in range(self.width):
                if self.visited[y][x] == 0:
                    self.pts.append((x, y))

    def setScale(self, scale: int) -> int:
        self.scale = scale
        return self.scale

    def getSqft(self) -> int:
        return int(len(self.pts) / self.scale)


filename = "images/1600sqft.copy.jpg"
file = FileLoader(filename)
file.denoise().erode().black_and_white()
data = file.get_data()
img = file.get_image()
# img.show()
fp = FloorPlan(data, 92)
print(fp.getSqft())

anim = Anim(img, file.width, file.height)


#  plt.xlim(-1, self.width+1)
#         plt.ylim(-1, self.height+1)
#         plt.autoscale(False)

#         X, Y = [], []
#         for y in range(self.height):
#             for x in range(self.width):
#                 if self.visited[y][x] == 0:
#                     X.append(x)
#                     Y.append(self.height-y)

#         # fig, ax = plt.subplots()
#         plt.scatter(X, Y, s=1, marker=',')
#         plt.show()
