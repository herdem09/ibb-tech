grade = int(input("Please enter your grade: "))
if 100 >= grade >= 90:
    print("AA")
elif 89 >= grade >= 79:
    print("BA")
elif 78 >= grade >= 68:
    print("BB")
elif 67 >= grade >= 57:
    print("BC")
elif 56 >= grade >= 46:
    print("CC")
elif 45 >= grade >= 35:
    print("DC")
elif 34 >= grade >= 24:
    print("DD")
elif 23 >= grade >= 0:
    print("FF")
else:
    print("Please make sure you entered a number between 100 and 0")
