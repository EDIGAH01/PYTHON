a = int(input("Please enter the number: "))
b = int(input("Please enter the power: "))
c = a
for f in range(0,b-1):
    c *= a
print(c)