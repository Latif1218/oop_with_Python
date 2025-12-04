# Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.

class Calculator:
    def add(self, a, b):
        print(f"{a} + {b} = {a+b}")
        
    def sub(self, a, b):
        print(f"{a} - {b} = {a-b}")
        
cal = Calculator()

cal.add(2,5)
cal.sub(5,9)