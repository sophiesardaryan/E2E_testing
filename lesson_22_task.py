str_1 = "abc"
str_2 = "xyz" #xyc abz

new_str = (str_2[0:2] + str_1[2:]) + " " + (str_1[0:2] + str_2[2])
print(new_str)