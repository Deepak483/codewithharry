class Employee:
    company = "Google"
    salary = 300

harry = Employee()
rajni = Employee()


harry.company = "YouTube"
# rajni.company = "FanFesta"


harry.salary = 500
rajni.salary = 400

Employee.company = "google Classroom"

# print(rajni.address) this line throws error as Employee object has no attribute address
print(harry.salary)
print(harry.company)
print(rajni.company)
print(rajni.salary)