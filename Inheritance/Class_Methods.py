class Person:
    name = "anonymous"
    
    # def changeName(obj, name):
    #     self.__class__.name = "Robun"
    
    @classmethod
    def changename(cls, name):
        cls.name = name
        
p1 = Person()
p1.changename("Sharuk")
print(p1.name)
print(Person.name)

