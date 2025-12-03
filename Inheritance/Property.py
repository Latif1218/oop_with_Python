# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem 
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
#         #percentage
        
        
        
# s1 = Student(98,97,99)
# print(s1.percentage)


# s1.phy = 87

# print(s1.phy)
# print(s1.percentage)



# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem 
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
#         #percentage
#     def calc_percentage(self):
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
        
# s1 = Student(98,97,99)
# print(s1.percentage)


# s1.phy = 86

# print(s1.phy)
# s1.calc_percentage()
# print(s1.percentage)




class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem 
        self.math = math

    @property
    def calc_percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
        
        
s1 = Student(98,97,99)
print(s1.calc_percentage)


s1.phy = 86

print(s1.phy)

print(s1.calc_percentage)