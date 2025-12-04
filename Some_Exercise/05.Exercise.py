class MaxFinder:
    def __init__(self, num):
        self.num = num
        
    def find_max(self):
        if not self.num:
            return "List is empty"
        return max(self.num)
    
    
    
find = MaxFinder([])
print(f"max num of the list is {find.find_max()}")