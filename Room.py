

class Room:

    """

    param: pts: list of tuples, (x,y)

    """

    def __init__(self, pts) -> None:

        self.pts = []
        self.addPts(pts)

    def addPts(self, pts):
        self.pts.extend(pts)
        self.area = len(pts)

        xMin = pts[0][0]
        xMax = pts[0][0]
        yMin = pts[0][1]
        yMax = pts[0][1]

        for pt in pts:
            xMin = pt[0] if pt[0] <= xMin else xMin
            xMax = pt[0] if pt[0] >= xMax else xMax
            yMin = pt[1] if pt[1] <= yMin else yMin
            yMax = pt[1] if pt[1] >= yMax else yMax

        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
