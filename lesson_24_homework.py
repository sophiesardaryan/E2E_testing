# 1. Write a Python program to get the Fibonacci series between 0 to 50. 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 1 2 3 5 8 13 21 34

# num_1 = 0
# num_2 = 1

# while(num_1 < 50):
#     print(f"{num_1}", end = " ")
#     next_num = num_1 + num_2
#     num_1 = num_2
#     num_2 = next_num


# fib_sequence = [0, 1]
# k = 1 

# for i in range(50):
#     k += fib_sequence[i]

#     if k >= 50:
#         break

#     fib_sequence.append(k)

# print(f"Fibonachi sequence is", fib_sequence)


# 2. Write a Python program that accepts a string and calculates the number of digits and letters.  

# my_data = input("Enter any text: ")
# count_of_digits = 0
# count_of_letters = 0

# for letter in my_data:
#     if letter.isdigit():
#         count_of_digits +=1
#     elif letter.isalpha():
#         count_of_letters += 1

# print(f"The total count of digits is: {count_of_digits}\nThe total count of letters is: {count_of_letters}")

# 3. Write a Python program to print alphabet pattern 'L'  

# for i in range(6):
#     print("*")
# print(5* "* ")
