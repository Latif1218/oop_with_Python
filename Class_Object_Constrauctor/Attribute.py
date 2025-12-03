class Student:
    
    # called class attribute
    Versity_name = "DU"
        
    # Default constructor    
    def __init__(self):
        pass
    
    # parameterized construstor
    def __init__(self, name , marks):
        
        # self.name called object attribute
        self.name = name
        self.marks = marks
        print("adding new student in database..")
        
# Obhect for Student class
s1 = Student("Jim", 3.67)
print(s1.name, s1.marks)

# Obhect for Student class
s2 = Student("Rumon", 3.78)
print(s2.name, s2.marks)

# and precedent of object attribute is higher then class attribute