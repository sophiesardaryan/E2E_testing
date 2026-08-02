# 1

# a = int(input("Enter any number: "))
# b = int(input("Enter any number: "))
# c = int(input("Enter any number: "))

# if a > b:
#     if a > c:
#         print(f"Maximum number is {a}")
#     else:
#         print(f"Maximum number is {c}")
# elif b > c:
#     print(f"Maximum number is {b}")
# else:
#     print(f"Maximum number is {c}") #practice how to find the maxiumum number

# 2

# number_list = [14, 10, 91, 82, 16, 6]
# entered_number = int(input("Enter any number: "))

# if entered_number in number_list:
#     print(f"The number {entered_number} exists in the list.")

#     if entered_number % 2 == 0:
#         print(f"The number {entered_number} is even.")
#     else:
#         print(f"The number {entered_number} is odd.")

# else:
#     print(f"The number {entered_number} is not in the list.")


# 3

my_list = [14, 10, 91, 82, 16, 6]
input_number = int(input("Enter any number: "))

new_list = [num for num in my_list if num != input_number]
print("Updated list is: ", new_list)