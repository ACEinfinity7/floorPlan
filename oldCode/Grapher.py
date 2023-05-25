import matplotlib.pyplot as plot


class Graph:

    def __init__(self, matrix) -> None:
        self.setMatrix(matrix)

    def setMatrix(self, matrix):
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.matrix = matrix
        self.x = []
        self.y = []

        plot.xlim(-1, self.width+1)
        plot.ylim(-1, self.height+1)
        plot.autoscale(False)
