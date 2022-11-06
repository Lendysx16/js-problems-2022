class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, point: Point):
        self.point = point


A = Point(*map(int, input().split()))
B = Point(*map(int, input().split()))
C = Point(*map(int, input().split()))
AB = Vector(Point(B.x - A.x, B.y - A.y))
OC = Vector(Point(C.x - B.x, C.y - B.y))
if AB.point.x * OC.point.x - AB.point.y * OC.point.y == 0:
    if B.x <= C.x <= A.x or A.x <= C.x <= B.x:
        print('Точка C лежит на отрезке AB')
    else:
        print('Точка C не лежит на отрезке AB')
else:
    print('Точка C не лежит на отрезке AB')
