from person import data

def get_full_name(name, surname):
    fullName = name + " " + surname
    return fullName

get_full_name(my_dict["name"],my_dict["surname"])

def print_person(name, surname):
    fullName = name + " " + surname
    print(fullName)