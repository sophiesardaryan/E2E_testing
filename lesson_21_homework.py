age = int(input("Enter your age: "))
decades = age // 10
years = age % 10


if age < 10:
    print(f"You are {years} year(s) old")
elif age % 10 == 0:
    print(f"You are {decades} decade{'s' if decades > 1 else ''} old")

else:
    print(f"You are {decades} decades and {years} year(s) old")