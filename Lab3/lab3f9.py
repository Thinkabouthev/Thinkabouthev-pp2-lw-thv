import math 
r=int(input())

def volume(r):
    v = 4/3*math.pi*r**3
    return v

print(volume(r))