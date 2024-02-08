def FtoC(F):
    C = (5 / 9) * (F - 32)
    return C

F = float(input())
print("in C =", FtoC(F))