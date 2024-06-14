a = []
fact = []
checker = "Y"
while checker == "Y" or checker == "Y":
    item = int(input("Enter the element of list: "))
    a.append(item)
    checker = input("do you want to add more values: ").upper()
print("The list is: ", a)
for i in a:
    f = 1
    for j in range(1, i+1):
        f=f * a
    fact.append(f)
print("The factorial of each element in the list is: ", fact)