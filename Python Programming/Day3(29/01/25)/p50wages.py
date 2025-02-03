gender = str(input("Enter the Gender - "))
age = int(input("Enter the age - "))

if age<=18 and age<30:
    if gender== 'male' or 'Male':
        print("The wages you will get is 700 per day")
    else:
        print("The wages you will get is 750 per day")
elif age<=30 and age<=40:
    if gender== 'male' or 'Male':
        print("The wages you will get is 800 per day")
    else:
        print("The wages you will get is 850 per day")
else:
    print("Enter the valid age")