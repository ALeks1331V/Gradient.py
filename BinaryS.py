class BinarySearch:
    err = 1.0E-6

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def fx(self, x):
        return (pow(x,2) - 2)
    
    def solve(self):
        root = (self.start + self.end)/2
        while(abs(self.fx(root)) > self.err):
            if((self.fx(root) - self.err) > 0):
                self.end = root
            else: 
                self.start = root
            root = (self.start + self.end)/2
            
        print("Root = ", root)
