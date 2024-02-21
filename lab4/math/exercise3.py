import math

n = int(input("Input number of sides:"))
l = int(input("Input the length of a side:"))
s = l / (2 * math.tan(math.pi / n)) * n * l / 2
print(f"The area of the polygon is: {s}")