from FloorPlan import FloorPlan

if __name__ == "__main__":
    filename = "test10x20.png"
    fp = FloorPlan(filename)

    fp.toGraph()
