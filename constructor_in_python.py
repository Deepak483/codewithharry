class Employee:

    company = "Google"

    def __init__(self,name,salary,subnit):
        self.name = name
        self.salary = salary
        self.subnit = subnit
        print("Employee data is created")
    
    def getDetails(self):
        print(f"Employee name is {self.name} ")
        print(f"Employee salary is {self.salary} ")
        print(f"Employee subnit is {self.subnit} ")
    
    def getSalary(self):
        print(f"Employee works in {self.company} salary is {self.salary} \n {self.signature}")

    @staticmethod
    def greet():
        print("Hello Sir, Good Morning!!")
    
e = Employee("Harry",3000,"Youtube")
e.salary = 4000
e.signature = "thanks"
e.getDetails()
e.getSalary()


        