n = int(input("Please enter the number of rows: "))

for i in range(0, n, +1):
    for j in range(n-i, 0, -1):
        print(" ", end = "")
    for j in range (0, i, +1):
        print("*", end = " ")
    print()

print()
print("HELLO! WOLRD")
print()

for i in range(n, 0, -1):
    for j in range(0, n+i,-1):
        print(" ")  
    for j in range(i, 0, -1):
        print("*", end = " ")
    print()