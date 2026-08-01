#1. Find the maximum value in a list.

# my_list = [1, 5, 11, 16, 24, 49, 99, 59, 85, 18]

# First solution
# max_value = my_list[0]

# for item in my_list:
#     if item > max_value:
#         max_value = item    
    
# print(f"Maximum value is {max_value}")

#Second solution
# max_value = my_list[0]

# for i in range(0, len(my_list)):
#     if my_list[i] > max_value:
#         max_value = my_list[i]
    
# print(f"Maximum value is {max_value}")


#2. Find the minimum value in a list.

# min_value = my_list[0]

# for i in my_list:
#     if i < min_value:
#         min_value = i
# print(f"Minimum value is {min_value}")


#3. Calculate the sum of all elements in a list.

# sum = 0

# for i in my_list:
#     sum += i
# print(f"Sum of all elements in a list is {sum}")

#4. Sort the list in ascending order.

# my_list = [8, 5, 3, 7]

# for i in range(len(my_list)):
#     for j in range(0, len(my_list)-1):
#         if my_list[j] > my_list[j+1]:
#             temp = my_list[j]
#             my_list[j] = my_list[j + 1]
#             my_list[j + 1] = temp
    
# print(my_list)


# my_list = [8, 5, 11, 29, 3, 7]

# for i in range(len(my_list)):
#     for j in range(0, len(my_list) -1):
#         if my_list[j]> my_list[j+1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

# print(my_list)


