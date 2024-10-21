import math

class Gradient:
    l = 0.1
    err = 1.0E-6
    def __init__(self, X, Y):
        self.startX = X
        self.startY = Y
    
    def fXY(self, x, y):
        return pow((x-1),2) + pow((y-2),2)
    
    def dX(self, x, y):
        return(self.fXY((x + self.err), y) - self.fXY(x,y))/self.err
    
    def dY(self, x, y):
        return(self.fXY(x,y+self.err) - self.fXY(x,y))/self.err
    
    def solve(self):
        x = self.startX
        y = self.startY
        checkErr = 1
        while (checkErr > self.err):
            tempX = x - self.l * self.dX(x, y)
            tempY = y - self.l * self.dY(x, y)
            checkErr = math.sqrt(pow((x-tempX),2) * pow((y- tempY),2))
            x = tempX
            y = tempY
    
        print(f"x: {x}\ny: {y}")
        print("Значение в минимуме: ", self.fXY(x, y))