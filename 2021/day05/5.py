import os
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def slope(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return dx/dy

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_p1(self):
        return self.p1

    def get_p2(self):
        return self.p2
    
    def get_slope(self):
        return self.p1.slope(self.p2)

    def __str__(self):
        return str(self.p1) + "->" + str(self.p2)

# --

def get_line_obj(line_str):
    tokens = line_str.split(" -> ")

    x1 = int(tokens[0].split(",")[0])
    y1 = int(tokens[0].split(",")[1])

    x2 = int(tokens[1].split(",")[0])
    y2 = int(tokens[1].split(",")[1])

    return Line(Point(x1, y1), Point(x2, y2))

def get_line_points(line):
    '''Returns all the points in a line'''
    p1 = line.get_p1()
    p2 = line.get_p2()

    points = []
    if p1.get_x() == p2.get_x():
        upper = max(p1.get_y(), p2.get_y())
        lower = min(p1.get_y(), p2.get_y())

        for i in range(lower, upper + 1):
            points.append(Point(p1.get_x(), i))
    elif p1.get_y() == p2.get_y():
        upper = max(p1.get_x(), p2.get_x())
        lower = min(p1.get_x(), p2.get_x())

        for i in range(lower, upper + 1):
            points.append(Point(i, p1.get_y()))
    else: # line is diagonal

        points.append(p1)
        points.append(p2)

        lower_x = min(p1.get_x(), p2.get_x())
        upper_x = max(p1.get_x(), p2.get_x())

        lower_y = min(p1.get_y(), p2.get_y())
        upper_y = max(p1.get_y(), p2.get_y())

        x_values = list(range(lower_x, upper_x + 1))
        y_values = list(range(lower_y, upper_y + 1))

        # make p1 be the "left"-most point
        if p2.get_x() > p1.get_x():
            temp = p2
            p2 = p1
            p1 = temp

        increasing = p1.slope(p2) > 0
        if not increasing:
            y_values.reverse()
        
        points = [Point(i, j) for i, j in zip(x_values, y_values)]

    return points

# --

sample = False

filename = ""
if sample:
    filename = "sample.txt"
else:
    filename = "input.txt"

data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, filename),) as file:
    data = file.readlines()
    data = [line.strip() for line in data]



lines = [get_line_obj(line) for line in data]

# Part 1 & 2
map = {}

for line in lines:
    for p in get_line_points(line):
        if p in map:
            map[p] = map[p] + 1
        else:
            map[p] = 1

solution = len(list(filter(lambda x: x >= 2, map.values())))
print(solution)