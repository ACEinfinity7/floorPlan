from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
from Room import Room


class FloorPlan:

    def __init__(self, filename) -> None:
        self.filename = filename

        self.img = Image.open(self.filename, mode='r', formats=None)
        self.img = self.img.convert("RGB")

        self.width, self.height = self.img.width, self.img.height

        data = list(self.img.getdata())
        data = [1 if x == (0, 0, 0) else 0 for x in data]

        self.matrix = np.array(data).reshape(self.height, -1)

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
    filename = "test10x20_2.png"

    fp = FloorPlan(filename)
    # print(fp)
    # fp.toGraph()

    room = fp.toRoom()

    room.findRooms()

    print(fp.width, fp.height)
    plt.xlim(-1, fp.width+1)
    plt.ylim(-1, fp.height+1)
    plt.autoscale(False)
    x = list()
    y = list()

    for r in room.rooms[1:]:
        for pt in r:
            x.append(pt[0])
            y.append(fp.height - pt[1])

    plt.scatter(x, y)
    plt.show()
