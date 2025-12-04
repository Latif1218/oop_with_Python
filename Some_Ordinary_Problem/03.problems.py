# Create a class called Order whitch store item & its price Use Dunder Function __gt__() to convey that order1>order2 if price of order1 > price of order2


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def showProduct(self):
        print("product is:",self.item,"price is:",self.price)
        
    def __gt__(self, o2):
        return self.price > o2.price
        
        
o1 = Order("Phone", 10000)
o2 = Order("Pc", 20000)

o1.showProduct()
o2.showProduct()

print(o1 > o2)
