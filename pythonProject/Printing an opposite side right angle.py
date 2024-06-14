# printing an upside down right angled triangle.
rows = int(input("Please enter the number of rows here: "))
for i in range (rows, 0, -1):
    for j in range (0, i):
        print("*", end = "")
    print()