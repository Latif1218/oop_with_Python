



# num = 121
# print(f"x = {num}")
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print(f"reverse = {reverse}")
# print(f"x= {num}")
    
    
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        
        return (temp == rev)
        
s = Solution()
print(s.isPalindrome(121))
s.isPalindrome(10)
