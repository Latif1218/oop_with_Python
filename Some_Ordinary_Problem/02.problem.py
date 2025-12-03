# define a Employee class with attributes role, department and salary. This class has also showDetails() method
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age 


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role:",self.role)
        print("department:",self.dept)
        print("salary:",self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        super().__init__("Ai Engineer", "FSD", "75000")


e1 = Engineer("Elon Mask", 40)
e1.showDetails()
        
        