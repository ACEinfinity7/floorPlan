

class Room:

    # pts : dict (x,y) -> matrix[y][x]
    # matrix : int[][] 1 is black 0 is all other pixels

    THRESHOLD = 1

    def __init__(self, pts, matrix) -> None:
        self.pts = pts
        self.matrix = matrix

    def _findRooms(self, x: int, y: int, room: list):
        # print("at top", x, y, end=" | ")

        if (x, y) in self.visited:
            # print("been visited", end=" | ")
            return

        if self.pts[(x, y)] == 1:
            # print("is black")
            return

        # print(f'x:{x} y:{y} room:{room}')

        self.visited.add((x, y))
        room.append((x, y))
        # up
        if y < len(self.matrix)-1:
            # print("went up")
            self._findRooms(x, y+1, room)
        # down
        if y > 1:
            # print("went down")
            self._findRooms(x, y-1, room)
        # left
        if x > 1:
            # print("went left")
            self._findRooms(x-1, y, room)
        # right
        if x < len(self.matrix[0])-1:
            # print("went right")
            self._findRooms(x+1, y, room)

        return

    def findRooms(self) -> None:
        self.visited = set()  # tuples (x,y)
        self.rooms = list()

        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                room = list()
                self._findRooms(x, y, room)
                # print(room)
                if room != []:
                    print(room)
                    self.rooms.append(room)

        # for room in self.rooms:
            # print(room)

    def threshold(self):
        threshold = list()
        for col in range(len(self.matrix[0])):
            count = 0
            onBlack = False
            for row in self.matrix:
                if (row[col] == 1):
                    onBlack = True
                if onBlack:
                    count += 1
                if (row[col] == 0 and onBlack):
                    onBlack = False
                    count = 0
                    threshold.append(count)
