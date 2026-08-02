#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

# my_list = [1, 2, 3, 1, 8, 2, 5, 9, 3]
# new_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.

# my_list = [1, 2, 3, 11, 8, 28, 5, 9, 33]

# for i in range(0, len(my_list)):
#     if i in (5, 4, 0):
#         my_list.remove(my_list[i])
# print(my_list)


# my_list = ["banana",1, 2, "apple", "peach", "banana",2,3,1]
# updated_list = []

# for i in range(0,len(my_list)):
#     if i not in (0, 4, 5):
#         updated_list.append(my_list[i])

# print(updated_list) 

#3 Write a Python program to get the difference between the two lists.

# list_1 = [1, 2, 2, 3, 3]
# list_2 = [3, 4, 5]
# diff_list = []

# for item in list_1:
#     if item not in list_2:
#         diff_list.append(item)
# print(diff_list) #optimal solution


# list_diff = list(set(list_1) - set(list_2))
# print(f"Difference between two list is {list_diff}")

# 4 Write a Python program to convert a tuple to a dictionary.

# import json
# my_tuple = (
#     ("name", "Sophie"),
#     ("surname", "Sardaryan")
# )

# my_tuple = dict(my_tuple)
# my_tuple = json.dumps(my_tuple, indent=4)
# print(my_tuple)


#5 Write a Python program to add an item in a tuple.

# my_tuple = ("QA engineer", 34, "Sophie", "Sardaryan")
# updated_tuple = my_tuple + ("041101264",)

# print(updated_tuple)


#6 Write a Python program to add a key with value to a dictionary.

# import json

# my_dict = {
#     "name" : "Sophie",
#     "surname" : "Sardaryan"
# }

# my_dict["age"] = 34
# my_dict = json.dumps(my_dict, indent=4)
# print(my_dict)


#7 Write a Python program to get the maximum and minimum value in a dictionary().

# my_dict = {
#     "age" : 34,
#     "salary": 300,
#     "course_count": 5
# }

# print(max(my_dict.values()))
# print(min(my_dict.values()))


#8 Write a Python program to create a union of sets.
# set_1 = {1, 2, 3}
# set_2 = {"a", "123", 3, "hello"}

# print(set_1.union(set_2))

#9 Student  Information
# Write a Python program to create a dictionary with the following information about a student: name age address education phone_numbers (store two phone numbers in a list) 

# Then:
# Print the entire dictionary. 
# Print only the student's name. 
# Print only the list of phone numbers. 
# Add a new key called "email" with your email address. 
# Print the updated dictionary.

# my_dictionary = {
#     "name" : "Sophie",
#     "age" : 34,
#     "address" : "Vanadzor",
#     "education" : "NPUA",
#     "phone_numbers" : ["041101264", "055101264"]

# }

# print(my_dictionary)
# print(my_dictionary["name"])
# print(my_dictionary["phone_numbers"])

# my_dictionary["email"] = "sofi.sardaryan.9191@gmail.com"
# print(my_dictionary)