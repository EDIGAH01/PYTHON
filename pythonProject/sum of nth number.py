#Calculating the sum of the nth number
n = int(input("Please enter the nth number: "))
sum = 0
for c in range (1,n):
    sum += c
    print("The sum is: ", sum)
print("The total sum is: ", sum)