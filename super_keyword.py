class Person:
    country = "India"

    def getSalary(self):
        print(f"The salary of the {self.slary}")

    def __init__(self) -> None:
        print("Initializing the person class")

    def takeBreath(self):
        print("I'm Breathing.....")

class Employee(Person):

    eCode = 1008
    company = "Google"

    def __init__(self):
        super().__init__()
        print("Initializing the Employee class.......")

    def getSalary(self):
        print(f"The Salary of the Employee is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print(f"I'm Employee so i'm breathing luckily....")

class Programmer(Employee):
    
    language = "Python"
    
    def __init__(self):
        print("Initializing the Programmer class")
    


p = Person()
p.takeBreath()
