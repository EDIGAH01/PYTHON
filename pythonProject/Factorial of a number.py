num = int(input("Please enter your number here: "))
factorial = 1
if num < 0:
    print("Sorry, Factorial does not exit.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
        print("The factorial of ", num, " is: ", factorial)