class Point:
    def draw(self):
        print("drawing...")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
