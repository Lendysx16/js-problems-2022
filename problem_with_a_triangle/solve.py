class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c
        if not self.__check_if_triangle_exists():
            raise ValueError("Triangle does not exist")

    def __check_if_triangle_exists(self):
        line1 = ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5
        line2 = ((self.a.x - self.c.x) ** 2 + (self.a.y - self.c.y) ** 2) ** 0.5
        line3 = ((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2) ** 0.5
        if line1 + line2 > line3 and line1 + line3 > line2 and line2 + line3 > line1:
            return True
        else:
            return False


def parse_point(file_input):
    arr = list(map(float, file_input.readline().split()))
    return Point(arr[0], arr[1])


def check_if_point_inside_a_triangle(point: Point, triangle: Triangle):
    value1 = (triangle.b.x - triangle.a.x) * \
             (point.y - triangle.a.y) - (triangle.b.y - triangle.a.y) * (point.x - triangle.a.x)
    value2 = (triangle.c.x - triangle.b.x) * \
             (point.y - triangle.b.y) - (triangle.c.y - triangle.b.y) * (point.x - triangle.b.x)
    value3 = (triangle.a.x - triangle.c.x) * \
             (point.y - triangle.c.y) - (triangle.a.y - triangle.c.y) * (point.x - triangle.c.x)
    return (value1 >= 0 and value2 >= 0 and value3 >= 0) or (value1 <= 0 and value2 <= 0 and value3 <= 0)


with open('files\\in.txt') as input_file:
    point1 = parse_point(input_file)
    point2 = parse_point(input_file)
    point3 = parse_point(input_file)
    point4 = parse_point(input_file)
    triangle_1 = 0
    try:
        triangle_1 = Triangle(point1, point2, point3)
    except ValueError:
        print("Triangle does not exist")
        exit(1)
    with open('files\\out.txt', 'w', encoding="utf-8") as output_file:
        if check_if_point_inside_a_triangle(point4, triangle_1):
            output_file.write('ДА')
        else:
            output_file.write('НЕТ')
