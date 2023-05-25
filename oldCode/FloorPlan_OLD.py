from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import subprocess
from Room_Old import Room


class FloorPlan:

    # creates floorplan object
    def __init__(self, filename) -> None:
        self.filename = filename

        # opens floorplan image
        self.img = Image.open(self.filename, mode='r', formats=None)

        self.width, self.height = self.img.width, self.img.height

        # converts RGB Pixels to a 1 and 0 map
        # where 1's are black and 0's are all other colors
        thresh = 150
        def fn(x): return 255 if x > thresh else 0
        self.img = self.img.convert('L').point(fn, mode='1')

        data = list(self.img.getdata())
        # print(data)
        data = [1 if x == 0 else 0 for x in data]

        # shape pixels into matrix same size as image
        self.matrix = np.array(data).reshape(self.height, -1)
        # print(self.matrix)

    def toGraph(self):
        x = list()
        y = list()
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] == 1:
                    x.append(j)
                    y.append(self.height-i)

        plt.xlim(-1, self.width)
        plt.ylim(-1, self.height)
        plt.autoscale(False)

        plt.scatter(x, y)

        plt.show()

    def __str__(self) -> str:
        str = '-' * self.width + "\n"
        for row in self.matrix:
            for col in row:
                if col == 1:
                    str += '█'
                else:
                    str += ' '
            str += '\n'
        str += '-' * self.width
        return str

    def toRoom(self) -> Room:
        pts = {}  # full of tuples of (x, y, val)
        for i in range(self.height):
            for j in range(self.width):
                pts[(j, i)] = self.matrix[i][j]

        return Room(pts, self.matrix)


if __name__ == "__main__":
    # filename = "images/test10x20_2.png"
    filename = "images/1600sqft.jpg"

    fp = FloorPlan(filename)
    sys.setrecursionlimit(fp.width*fp.height)
    print(fp)
    # fp.toGraph()

    room = fp.toRoom()

    room.findRooms()

    print(fp.width, fp.height)

    # fig = plt.figure()
    plt.xlim(-1, fp.width+1)
    plt.ylim(-1, fp.height+1)
    plt.autoscale(False)
    # axis = fig.add_subplot()

    for r in room.rooms[1:]:
        print(r)
        x = []
        y = []
        for pt in r:
            print(pt[0], fp.height-pt[1])
            x.append(pt[0])
            y.append(fp.height - pt[1])

        plt.scatter(x, y, s=0.5, marker=',')
    plt.show()
