#checking for the greatest of four numbers
a = int(input("Pleaase enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the third number: "))
d = int(input("Please enter the fourth number: "))
if a>b and a>c and a>d:
    print("The greatest number of the four is: ", a)
elif b>c and b>d:
    print("The greatestof the four is: ", b)
elif c>d:
    print("The greatest of the four is: ", c)
else:
    print("The greatest of the four is: ", d)