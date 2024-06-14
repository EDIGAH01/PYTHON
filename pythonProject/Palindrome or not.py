a = int(input("Please enter the number: "))
b = a
c = 0
while a > 0:
    d = a % 10
    c =c * 10+d
    a =a // 10
if(b == c):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")