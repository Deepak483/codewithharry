class Employee:
    
    company = "Google"
    eCode = 120

class Freelancer:
    level  = 0

    def upgradelevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):
    language = "Python"

    def getlanguage(self):
        print(f"The language of programmers is {self.language}")


e = Employee()
print(e.eCode)

    