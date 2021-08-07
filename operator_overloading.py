class Calculator:

    def __init__(self,num1):
        self.num1 = num1

    def __add__(self,num2):
        return self.num1 + num2.num1

    def __mul__(self,num2):
        return self.num1 * num2.num1
    
    def __len__(self,str):
        return len(self.str)

    def __str__(self):
        return f"The Decimal Number that we have used {self.num1}"

n1 = Calculator(9)
print(n1)
# print(str(n))
# n2 = Calculator(10)

# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)

# print(str)