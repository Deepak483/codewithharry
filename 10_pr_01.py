class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,product):
        self.name = name
        self.salary = salary
        self.product = product
        
    def getInfo(self):
        print(f"The company of the employee is {self.company} and name is {self.name} and product is {self.product}")


harry = Programmer("Harry",300,"Github")
rajni = Programmer("Rajni",400,"Skype")

harry.getInfo()
rajni.getInfo()
