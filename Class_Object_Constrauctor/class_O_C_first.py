# create a class. the class name always started with capital letter
class Student:
    
    # Default constructor    
    def __init__(self):
        pass
    
    # parameterized construstor
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")
        
# Obhect for Student class
s1 = Student("Jim", 3.67)
print(s1.name, s1.marks)

# Obhect for Student class
s2 = Student("Rumon", 3.78)
print(s2.name, s2.marks)