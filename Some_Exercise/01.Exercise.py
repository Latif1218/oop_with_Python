class Greeter:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"hello, {self.name}!. haw are you.")
        
g1 = Greeter("Shumon")
g1.greet()