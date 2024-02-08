class Shape:
    def __init__(self,leng):
        pass
    def area(self):
        return self.leng*self.leng

class Square(Shape):
    def __init__(self, leng=0):
        self.leng = leng

s1 = Square(int(input()))
print(f"area of the square: {s1.area()}")