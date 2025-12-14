





# x = 8
# result = x ** 0.5
# print(int(result))




# a = 7
# b = -3
# c = a//b

# print(c)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Perform division
        result = dividend // divisor
        
        # Handle overflow edge case
        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        else:
            return result
        
        
s = Solution()
print(s.divide(-2147483648,-1))