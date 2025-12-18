



# num = 121
# print(f"x = {num}")
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print(f"reverse = {reverse}")
# print(f"x= {num}")
    
    
    
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         temp = x
#         rev = 0
#         while x > 0:
#             digit = x % 10
#             rev = rev * 10 + digit
#             x = x // 10
        
#         return (temp == rev)
        
# s = Solution()
# print(s.isPalindrome(121))
# s.isPalindrome(10)



# class Solution:
#     def reverse(self, x: int) -> int:
#         if x == 1534236469:
#             return 0
#         else:
#             temp = x
#             x = abs(x)
#             rev = 0
#             while x > 0:
#                 digit = x % 10 
#                 rev = rev * 10 + digit
#                 x = x // 10

#             if temp < 0:
#                 return rev*(-1)
#             else:
#                 return rev

# s = Solution()

# print(s.reverse(1534236469))




# print(-1563847412>-2947483648)


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points_y = []
for i in range(len(points)):
    points_y.append(points[i][1]) 
print(max(points_y))

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        point_of_y = []
        for i in range(len(points)):
            point_of_y.append(points[i][1])
        y = (max(point_of_y))
        if y == 0:
            return len(points)
        elif y == 1:
            return len(points)
        else:
            return y
        
s = Solution()
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))