# rsz_1438840048-2cf71ed69d-findangle.png  is a right triangle,  at .
# Therefore, .

# Point  is the midpoint of hypotenuse .

# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side .
# The second line contains the length of side .

# Constraints


# Lengths  and  are natural numbers.
# Output Format

# Output  in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


# Sample Input

# 10
# 10
# Sample Output

# 45°


# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true


# if __name__=='__main__':
#     import math
#     AB = int(input())
#     BC = int(input())
#     x = AB/BC
    
#     angleMBC=math.atan(x)
#     rounded_angle = round(math.degrees(angleMBC))
#     degree_symbol = '\u00b0'
#     print(f"{rounded_angle}{degree_symbol}")






# if __name__=='__main__':
    
#     def create_palindom(n):
#         num_str = ''.join(str(i) for i in range(1, n + 1))
#         palindrom_str = num_str + num_str[::-1][1:]    #"123"[::-1]  # output "321"
#         pal_num = int(palindrom_str)                    #"321"[1:]  # output "21"
#         return pal_num
    
#     for j in range(1,int(input())+1):
#         print(create_palindom(j))
    
    
    
def create_palindrome(n):
    # সংখ্যার বিপরীত অংশ তৈরি করার জন্য
    original_num = n
    reversed_num = 0
    
    # বিপরীত সংখ্যা তৈরি করা
    while n > 0:
        digit = n % 10  # শেষ ডিজিট বের করা
        reversed_num = reversed_num * 10 + digit  # বিপরীত অংশে যোগ করা
        n //= 10  # শেষ ডিজিট বাদ দেওয়া
    
    # প্যালিনড্রোম তৈরি করা: প্রথম সংখ্যা ও বিপরীত সংখ্যা যোগ করা (বিপরীত অংশে প্রথম ডিজিট বাদ)
    palindrome_num = original_num * (10 ** len(str(reversed_num))) + (reversed_num % (10 ** (len(str(reversed_num)) - 1)))
    
    return palindrome_num

print(create_palindrome(3))




# https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true