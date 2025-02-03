print("Enter number 1 for additon")
print("Enter number 2 for subtraction")
print("Enter number 3 for multpication")
print("Enter number 4 for division")

option = int(input("Enter the value => "))

if option==1:
    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: "))

    print("THe addtion of the two numbers are ", number1+number2 )

elif option==2:
    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: "))

    print("THe subtraction of the two numbers are ", number1-number2 )
    
elif option==3:
    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: ")) 

    print("THe multiplication of the two numbers are ", number1*number2 )
    
elif option==4:
    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: "))

    print("THe division of the two numbers are ", number1/number2 )
    
else:
    print("Enter the valid option")
    