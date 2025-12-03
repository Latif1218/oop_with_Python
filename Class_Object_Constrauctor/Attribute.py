# first methods#######################################

class Student:
    
    def __init__(self, name , marks_ban, marks_eng, marks_math):
        
        # self.name called object attribute
        self.name = name
        self.marks_ban = marks_ban
        self.marks_eng = marks_eng
        self.marks_math = marks_math
        
    def marks_avg(self):
        mark_avg = (self.marks_ban + self.marks_eng + self.marks_math)/3
        return mark_avg        
        
# Obhect for Student class
s1 = Student("Jim", 3.67, 4.00, 3.20)
print(s1.name, s1.marks_avg())

# Obhect for Student class
s2 = Student("Rumon", 3.78, 3.90, 3.57)
print(s2.name, s2.marks_avg())

# and precedent of object attribute is higher then class attribute




# secend methods ##################################################
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("hello,,")
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "ÿour avg score is :", sum/3)
        
s1 = Students("tony",[99,97,98])
s1.get_avg()


s1.name = "ironman"
s1.hello()
s1.get_avg()