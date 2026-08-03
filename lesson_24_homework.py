# 1. Write a Python program to get the Fibonacci series between 0 to 50. 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 1 2 3 5 8 13 21 34


num_1 = 0
num_2 = 1

while (num_1 <50):
    print(f"{num_1}", end = ' ')

    next_num = num_1 + num_2
    num_1 = num_2
    num_2 = next_num


