#function
def menu():
    print ("1) Sum")
    print ("2) Subtract")
    print ("3) Multiply")
    print ("4) Divide")

#call the function
menu()
#read the input of the keyboard
(opt) = input("Select an option")

num1 = float(input("Please enter the first number"))
num2 = float(input("Please enter the second number"))

if opt == "1":
    total = num1 + num2
    print ("The total is " + str(total))
elif opt == "2":
    total = num1 - num2
    print ("The total is " + str(total))
elif opt == "3":
    total = num1 * num2
    print ("The total is " + str(total))
elif opt == "4":
    if num2 ==0:
        print("You cannot divide by zero")
    else:
        total = num1 / num2
        print ("The total is " + str(total))
else:
    print("Invalid option")
