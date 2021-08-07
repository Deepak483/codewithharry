# Getter and Setter method 

class Employee:
    company = "Bharat Gas"
    salary = 5000
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.salary)
print(e.salarybonus)
e.totalSalary = 5800
print(e.salarybonus)
        