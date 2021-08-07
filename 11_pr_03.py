class Employee:

    salary = 4000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salary)
print(e.increment)
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 8000
print(e.salaryAfterIncrement)
print(e.increment)
