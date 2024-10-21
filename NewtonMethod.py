class NewtonMethod:
    err = 1.0E-6

    def __init__(self, X):
        self.startX = X
    
    def fx(self, x):
        return (pow(x,2) - 2)
    
    def dF(self, x):
        return (self.fx(x+self.err) - self.fx(x))/self.err
    
    def solve(self):
        x = 0
        nextX = self.startX
        while(abs(x - nextX) > self.err):
            x = nextX
            nextX = x - (self.fx(x)/self.dF(x))
        print("root = ", x)