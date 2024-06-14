#calculating the percentage results
marks = eval(input("Please enter your marks out of 300: "))
percent = marks/300 * 100
print("Your percenteage is : ", percent, "100")
if marks > 300:
    print("You entered a wrong value.")
elif percent > 60:
    print("Your division is first.")
elif percent > 50 and percent < 53:
    print("you division is second.")
elif percent > 33 and percent < 50:
    print("Your division is the third.")
else:
    print("fail")