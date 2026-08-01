#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

# my_list = [1, 2, 3, 1, 8, 2, 5, 9, 3]
# new_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.

my_list = [1, 2, 3, 11, 8, 28, 5, 9, 33]

for i in range(0, len(my_list)):
    if i in (0, 4, 5):
        my_list.remove(my_list[i])
print(my_list)








# my_list = ["banana",1, 2, "apple", "peach", "banana",2,3,1]
# updated_list = []

# for i in range(0,len(my_list)):
#     if i not in (0, 4, 5):
#         updated_list.append(my_list[i])

# print(updated_list) 