#This is a simple calculator supporting multiplication, division, addition, and subtraction.
a = 0
def begin():
    a = 0
    print("Welcome to calculator!")
    print("press... 1 for addition... 2 for subtraction... 3 for multiplication... or 4 for division.")
    print("when you are done, press ENTER")
    operation = int(input("Enter your choice: "))
    if operation != 1 or operation != 2 or operation != 3 or operation != 4:
        a = 1
    else:
        a = 1
    if a == 1:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        
        if operation == 1:
            print(num1,"+",num2,"=", (num1+num2))
        elif operation == 2:
            print(num1,"-",num2,"=", (num1-num2))
        elif operation == 3:
            print(num1,"x",num2,"=", (num1*num2))
        elif operation == 4:
            print(num1,"÷",num2,"=", (num1/num2))
        else:
            print("INVALID")
            begin()

begin()


