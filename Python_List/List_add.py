# list

# list1 = [1,2,3]
# list2 = [4,5,6]


# # method(01) list add using (+) operater
# combind_list1 = list1 + list2
# print(combind_list1)



# # method(02) list add using extend() method

# list1.extend(list2)
# print(list1)




# # method(03) list add using for loop with append()

# for item in list2:
#     list1.append(item)
# print(list1)


# method(04) list add using list comprehension

# summed_list = [list1[i] + list2[i] for i in range(len(list1))]
# print(summed_list)




# def create_palindrome_triangle(n):
#     for i in range(1, n + 1):
        
#         num = 0
#         for j in range(1, i + 1):
#             num = num * 10 + j
        
       
#         reversed_num = 0
#         temp = num
#         while temp > 0:
#             digit = temp % 10
#             reversed_num = reversed_num * 10 + digit
#             temp //= 10
        
        
#         palindrome_num = num * (10 ** (len(str(reversed_num)) - 1)) + (reversed_num % (10 ** (len(str(reversed_num)) - 1)))
        
        
#         print(palindrome_num)

# if __name__ == '__main__':
#     n = int(input("Enter a number: "))
#     create_palindrome_triangle(n)



# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


