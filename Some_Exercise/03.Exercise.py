class Employee:
    def __init__(self, name, age=None, salary=None):
        self.name = name
        self.age = age
        self.salary = salary
        
    def empDetals(self):
        
        print(f"employ name {self.name}")
            
        if self.age:
            print(f"age is: {self.age}")
        
        if self.salary:
            print(f"salary is: {self.salary}")
            
e1 = Employee("Latif")
e1.empDetals()
e2 = Employee("shumon", 23)
e2.empDetals()
e3 = Employee("Latif", 23, 25)            
e3.empDetals()
        
    