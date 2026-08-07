# 1. Write a Python program which will open file, if not exist then create it.  
# First version

# def create_file(file_name):
#     f = open(file_name, "a+")
#     f.writelines("Hello\nIt's my first file handling!")
#     f.seek(0)

#     for i in f:
#         print(i, end = "")
#     f.close()

# create_file("homework_26.txt")


# Second version

# def createFile(file_name):
#     with open(file_name, "w+") as f:
#         f.write("Hello\nIt's my first file handling!")
#         f.seek(0)
#         print(f.read())

# createFile("homework_26.txt")


# 2. Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.

# def generateFile():
#     for i in range(65, 91):
#         letter = chr(i)

#         with open(f"{letter}.txt", "w+") as f:
#             f.write(f"{letter}.txt file is created")
#             f.seek(0)
#             print(f.read())

# generateFile()

# with writelines

def generate_file():
    for i in range(65, 91):
        letter = chr(i)

        with open(f"{letter}.txt", "w+") as new_file:
            new_file.writelines(f"{letter}.txt file is created")
            new_file.seek(0)
            for i in new_file:
                print(i)

generate_file()