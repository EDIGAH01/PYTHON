rows = int(input("Please enter the number of rows here: "))
for i in range (1, rows+1):
    for j in range(1, i+1):
        print(i, end = "")
    print()
print("\n")
for a in range(rows, 0,-1):
    for b in range(1, a+1):
        print(a, end = "")
    print()