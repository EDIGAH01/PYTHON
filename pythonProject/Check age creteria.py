#Checking the age of the user.
age = int(input("Please enter your age: "))
if age > 0 and age < 12:
    print("kid")
elif age >= 12 and age <= 19:
    print("Teenager.")
elif age > 19 and age <= 30:
    print("You are young.")
elif age >30 and age <= 45:
    print("Mature.")
elif age > 45 and age <= 60:
    print("Experienced.")
elif age > 60 and age <= 75:
    print("Old.")
elif age > 75:
    print("Senior citizen.")