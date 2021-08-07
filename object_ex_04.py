# self parameter
class Employee:
    company = "YouTube"
    def getSalary(self,signature):
        print(f"The Salary of the Employee is {self.salary} and the company is {self.company}\n{signature}")

    @staticmethod
    def greet():
        print("Hello,Sir Good Morning!!")
    

e = Employee()
e.salary = 400
e.getSalary("Thanks!!")
e.greet()