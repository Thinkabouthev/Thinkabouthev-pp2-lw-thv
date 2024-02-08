class Shape:
    def __init__(self, leng, wid):
        pass

    def area(self):
        return self.leng * self.wid


class Rectangle(Shape):
    def __init__(self, leng=0, wid=0):
        self.leng = leng
        self.wid = wid


s1 = Rectangle(int(input()), int(input()))
print(f"area of the Rectangle: {s1.area()}")