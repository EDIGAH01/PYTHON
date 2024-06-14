print("Checking the greatest of three numbers.")
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number"))
c = int(input("Please enter the third number : "))
if a>b and a>c:
    print("The greatest of the three  numbers is: ", a)
elif b>c:
    print("The greatest number of the three is: ", b)

else:
    print("The greatset of the three numbers is: ", c)