class Employee:
    company = "Google"
    salary = 100
    location = "Delhi"

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal
        print(f"The salary of the employee is {cls.salary}")

e = Employee()
e.changeSalary(455)
print(e.salary)
Employee.salary = 500
print(Employee.salary)