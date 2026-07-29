#1. Write a Python program to calculate the length of a string.

# my_string = "Here is string for your exercise!"
# print(len(my_string))


#2. The last 2 chars from a given a string
# Sample String : 'w3resource'
# Expected Result : 'w3ce'

# my_str = "w3resource"
# new_str = my_str[0:2] + my_str[-2:]
# print(new_str)

#3. Write a Python program to replace ‘cat’ word to ‘dog’

# str_1 = "I have a cat and I love it"
# new_str1 = str_1.replace("cat", "dog")
# print(new_str1)


#4.Write a Python program to reverse 123  to 321 in text.

# text = "I have 123 books"
# splited_text = text.split()

# for i in splited_text:
#     if i.isdigit():
#         reversed_text = "".join(reversed(i))
#         text = text.replace(i, reversed_text)
# print(text)


#5. Replace all occurrence of word five to one.

# sample_string = "five five was a race horse, two two was one too."
# rep_text = sample_string.replace("five", "one")
# print(rep_text)


#6. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# test_data = [1, 5, 8, 3]
# print(3 in test_data)
# print(-1 in test_data)


#7. Write a Python program to solve (x + y) * (x + y). Expected Output : (4 + 3) ^ 2) = 49

# x = 4
# y = 3
# output = (x + y) * (x + y)
# print(f"({x} + {y}) ^ 2 = {output}")


#8. Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.

# x = 2.5
# y = 13.75
# sum = int(x) + int(y)
# print("".join(reversed(str(sum))))
# print(str(sum)[::-1])