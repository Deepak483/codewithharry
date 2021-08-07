class Calculator:
    
    def __init__(self,num):
        self.number = num

    def Square(self):
        print(f"The value of {self.number} square is {self.number ** 2}")

    def Cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

    def SquareRoot(self):
        print(f"The value of {self.number} SquareRoot is {self.number}")

c = Calculator(5)
c.Square()
c.SquareRoot()
c.Cube()


        

