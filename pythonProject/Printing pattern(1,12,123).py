rows = int(input("Please enter the number of rows here: "))
for i in range (1,rows+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()