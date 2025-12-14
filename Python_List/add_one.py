
# d = [1, 2, 3, 4, 5]  # Example list of integers
# s = ''.join(str(item) for item in d)  # Convert each item to a string
# print(s)




# d1 = [1, 2, 3, 4, 5]  
# s1 = ''.join(map(str, d1))  
# print(type(s1))

# s2 = int(s1)+1
# print(type(s2))
# list = list(map(int, str(s2)))
# print(list)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(map(str, digits))
        integer = int(string) + 1
        list1 = list(map(int, str(integer)))
        return list1
        

s = Solution()
print(s.plusOne([1,2,3]))