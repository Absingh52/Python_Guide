# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
import math
class Calculator:
    def __init__(self,n):
        self.n=n
    def Square(self):
        return f"Square of {self.n}",self.n*self.n
    def Cube(self):
        return(f"Cube Of {self.n}",self.n*self.n*self.n)
    def sqrt(self):
        return(f"sqrt of {self.n}",round(math.sqrt(self.n),2))    
    def greet():
        print("hello")

a=int(input("Enter the value of a:"))
n=Calculator(a)
print(Calculator.greet())
print(n.Square())
print(n.Cube())
print(n.sqrt())
