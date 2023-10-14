class parent:
    def __init__(self,x):
         self.x = x

class child(parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def addition(self):
         z = self.x + self.y
         return z
        
ch = child(1010,1000)
result = ch.addition()
print(f"Result: {result}")
