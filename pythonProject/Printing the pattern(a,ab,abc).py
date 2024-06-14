check = str(input("Please enter a character here: "))
a = ord(check)
for x in range(65, a+1):
    for c in range(65, x+1):
        print(chr(c), end = "")
    print("")
