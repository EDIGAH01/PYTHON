marks = int(input("Please enter the your marks: "))
if (marks >=0 and marks<= 39):
    print("you are not there yet, keep going.")
elif (marks >= 40 and marks <= 59):
    print("You got a refer. try again don't give up.")
elif (marks >= 60 and marks <= 79):
    print("you got a pass, good job keep pushing")
elif (marks >= 80):
    print("You got a distinction, congrats, keep it up")
else:
    print("You entered an invalid value")