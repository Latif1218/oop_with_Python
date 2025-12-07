my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"my_list = {my_list}")
# Basic slicing: elements from index 2 up to (but not including) index 6
slice1 = my_list[2:6]
print(f"my_list[2:6] = {slice1}")    # Output: [2, 3, 4, 5]


# slice from the beginning to a specific index
slice2 = my_list[:4]
print(f"my_list[:4] = {slice2}")     # output: [0, 1, 2, 3]


# slice from a specific index to the end
slice3 = my_list[5:]
print(f"my_list[5:] = {slice3}")     # output: [5, 6, 7, 8, 9]


# slice with a step 
slice4 = my_list[1:9:2]
print(f"my_list[1:9:2] = {slice4}")  # output: [1, 3, 5, 7]


# Reversing a list using slicing 
reversed_list = my_list[::-1]
print(f"my_list[::-1] = {reversed_list}")  # output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# slicing with negative indices
slice5 = my_list[-4:-1]
print(f"my_list[-4:-1] = {slice5}")  # output: [6, 7, 8]


# Slicing beyond list boundaries dose not raise an error
slice6 = my_list[5:100]
print(f"my_list[5:100] = {slice6}")  # output: [5, 6, 7, 8, 9]