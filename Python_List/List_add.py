# list

list1 = [1,2,3]
list2 = [4,5,6]


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