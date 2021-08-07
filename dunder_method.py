class Number:

    def __init__(self,num) -> None:
        self.num = num

    def __add__(self,num2):
        return self.num + num2.num

    def __mul__(self,num2):
        return self.num * num2.num

    def __len__(self):
        return 1
            
    def __str__(self):
        return f"Decimal Number:{self.num}"

n = Number(9)
print(n)
print(len(n))