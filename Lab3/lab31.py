class STUDENT:
    def __init__(self):
        pass
    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())


s1 = STUDENT()
s1.getString()
s1.printString()