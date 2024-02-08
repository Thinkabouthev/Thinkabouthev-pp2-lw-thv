class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    def show(self):
        print(f'(x, y) = {self.x, self.y}')

    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        print(f'(x, y) = {self.x, self.y}')

    
    def dist(self, x1, y1):
        return ( (self.x - x1)**2 + (self.y - y1)**2)**(1/2)

ps = Point(int(input()), int(input()))

#1
ps.show()

#2
ps.move(int(input()), int(input()))

#3
print(f'distance = {ps.dist(int(input()), int(input()))}')
# f-строки (форматированные строки) позволяют вставлять значения переменных или выражений прямо в строку без необходимости использования оператора конкатенации или метода форматирования.