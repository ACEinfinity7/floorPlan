from scipy.spatial import ConvexHull
from PIL import Image
from PIL import ImageFilter
import numpy as np
import sys
from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull


def fn(filename):
    img = Image.open(filename, mode='r').convert("L")

    x = [1, 1, 1,
         1, -9, 1,
         1, 1, 1]
    # img.show()
    # print(img.mode)
    img = img.filter(ImageFilter.Kernel((3, 3), x, scale=1, offset=2))
    # img.show()

    avgColor = np.average(np.array(img.getdata()))
    # print(avgColor)

    def fn(x): return 255 if x <= avgColor else 0

    img2 = img.point(fn, mode="1")
    # img2.show()
    data = img2.getdata()
    matrix = np.array(data).reshape(img2.height, -1)

    # blur = img.filter(ImageFilter.UnsharpMask(
    #     radius=10, percent=500, threshold=1))

    # high_freq = np.asarray(img) - np.asarray(blur)
    # sharpened = Image.fromarray(np.asarray(img) + high_freq)
    # subtracted = Image.fromarray(high_freq)
    # img.show()
    # # blur.show()
    # sharpened.show()

    def traverse(x, y, matrix, edge):
        if (matrix[y][x] == 255):
            # print("is white")
            return

        if ((x, y) in visited):
            return

        edge.add((x, y))
        visited.add((x, y))
        # print(f'{x}, {y} added')
        # down
        if y < len(matrix)-1:
            # print("went up")
            traverse(x, y+1, matrix, edge)
            if (x > 1):
                # bottom left
                traverse(x-1, y+1, matrix, edge)
            if (x < len(matrix[0])-1):
                # bottom right
                traverse(x+1, y+1, matrix, edge)
        # up
        if y > 1:
            # print("went down")
            traverse(x, y-1, matrix, edge)

            if (x > 1):
                # up left
                traverse(x-1, y-1, matrix, edge)
            if (x < len(matrix[0])-1):
                # up right
                traverse(x+1, y-1, matrix, edge)

        # left
        if x > 1:
            # print("went left")
            traverse(x-1, y, matrix, edge)
        # right
        if x < len(matrix[0])-1:
            # print("went right")
            traverse(x+1, y, matrix, edge)

        return

    sys.setrecursionlimit(img2.width*img2.height)
    edges = list()
    visited = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            edge = set()
            traverse(x, y, matrix, edge)
            if (len(edge) != 0):
                edges.append(edge)

    plt.xlim(-1, img2.width+1)
    plt.ylim(-1, img2.height+1)
    plt.autoscale(False)
    if (0, 0) in edges[0]:
        edges = edges[1:]
    edges = sorted(edges, reverse=True, key=lambda x: len(x))
    # print(edges)
    m = max(edges)
    x = []
    y = []
    for edge in edges:
        for pt in edge:
            x.append(pt[0])
            y.append(img2.height - pt[1])
    p = []
    for pt in m:
        # x.append(pt[0])
        # y.append(img2.height - pt[1])
        p.append((pt[0], img.height - pt[1]))

    ax = plt.subplot()
    ax.scatter(x, y, s=0.5, marker=',')

    pts = np.array(list(p))
    hull = ConvexHull(pts)
    border = pts[hull.vertices]
    x, y = border[:, 0], border[:, 1]
    x = np.append(x, border[0][0])
    y = np.append(y, border[0][1])
    ax.plot(x, y, color='red')
    plt.show()

    print(int(hull.volume/92))


filenames = ["1600sqft.jpg",
             "floorplan 4 copy.jpg",
             "floorplan 5.jpeg",
             "floorplan 6.jpeg",
             "floor plan 7.jpeg"]

for filename in filenames:
    fn("images/" + filename)
