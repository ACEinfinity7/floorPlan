

class Room:

    # pts : dict (x,y) -> matrix[y][x]
    # matrix : int[][] 1 is black 0 is all other pixels

    THRESHOLD = 1

    def __init__(self, pts, matrix) -> None:
        self.pts = pts
        self.matrix = matrix

    def _findRooms(self, x: int, y: int, room: list):
        if (x, y) in self.visited or self.pts[(x, y)] == 1:
            return

        # print(f'x:{x} y:{y} room:{room}')

        self.visited.add((x, y))
        room.append((x, y))
        # up
        if y < len(self.matrix)-1:
            self._findRooms(x, y+1, room)
        # down
        if y > 1:
            self._findRooms(x, y-1, room)
        # left
        if x > 1:
            self._findRooms(x-1, y, room)
        # right
        if x < len(self.matrix[0])-1:
            self._findRooms(x+1, y, room)

        return

    def findRooms(self) -> None:
        self.visited = set()  # tuples (x,y)
        self.rooms = list()

        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                room = list()
                self._findRooms(x, y, room)
                if room != []:
                    self.rooms.append(room)

        for room in self.rooms:
            print(room)
