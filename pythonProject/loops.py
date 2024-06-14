x = [10, 12, 13, 14, 17, 19, 21, 22, 25]

# e a for loop that iterates over the x list and prints out all the elements of the list.

for i in x:
    print(i)

#  a for loop that iterates over the x list and prints out the remainders of
# each element of the list divided by 3.
for i in x:
    print(i % 3)

#  a for loop that iterates over the x list and prints out all the elements
# of the list in reversed order and multiplied by 10.
for  i in reversed(x):
    print(i * 10)
print()
# or 

for i in sorted(x, reverse = True):
    print(i * 10)

#  a for loop that iterates over the x list and prints out all the elements of
# the list divided by 2 and the string Great job! after the list is exhausted.

for i in x:
    print(i /2) # youcan also use else after this statement
print("Great job for the list is exhausted. ")

# a for loop that iterates over the x list and prints out the index of each element.

for i in x:
    print(x.index(i))
print()
# a while loop that prints out the value of x squared while x is less than
# or equal to 5. Be careful not to end up with an infinite loop!

x= 0
while x <= 5:
    print(x * x)# you can use x ** 2
    x+=1
print()

# a while loop that prints out the value of x times 10 while x is less
# than or equal to 4 and then prints out Done! when x becomes larger than 4.
# Be careful not to end up with an infinite loop!

x = 0
while x< 4:
    print(x * 10)
    x+=1
else:
    print("Done!")
print()
#  a while loop that prints out the value of x plus 10 while x is less than
# or equal to 15 and the remainder of x divided by 5 is 0. Be careful not to end up
# with an infinite loop!
x = 0
while x <= 15 and x % 5 == 0:
    print(x + 10)
    x+=1
else:
    print("None")
print()

#  a while loop that prints out the absolute value of x while x is
# negative. Be careful not to end up with an infinite loop!

x = -7
while x < 0:
    print(abs(x))
    x+=1
print()
# a while loop that prints out the value of x times y while x is greater
# than or equal to 5 and less than 10, and prints out the result of x divided by y
# when x becomes 10. Be careful not to end up with an infinite loop!
x= 5
y = 2
while x >= 5 and x < 10:
    print(x * y)
    x += 1
else:
    print(x / y)

print()

# e code that will iterate over the x list and multiply by 10 only the elements that are greater
# than 20 and print them out to the screen.

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x :
    if i > 20:
        print(i * 10)

print()

# code that will iterate over the x and y lists and multiply each element
# of x with each element of y, also printing the results to the screen.

x = [2,4,6]
y = [5, 10]
for i in x:
    for j in y:
        print(i * j)

print()

# code that will iterate over the x and y lists and multiply each
# element of x with each element of y that is less than 12, also printing the
# results to the screen.
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]
 
for i in x:
    for k in y:
        if k < 12:
            print(i * k)

print()

# code that will iterate over the x and y lists and multiply each element
# of x that is greater than 5 with each element of y that is less than 12, also
# printing the results to the screen.

for i in x:
    for j in y:
        if i>5 and j < 12:
            print(i * j)

print()

# code that will iterate over the x and y lists and multiply each
# element of x with each element of y that is less than or equal to 10, also
# printing the results to the screen. For ys elements that are greater than 10,
# multiply each element of x with y squared.

for i in x:
    for j in y:
        if j <=10:
            print(i * j)
            
        if j > 10:
            print(i * (j**2))

print()

# code that will print out each character in x doubled if that character is
# also inside y. Hint: use nesting!

x = "cryptocurrency"
y = "blockchain"
for i in x:
    if i in y:
        print(i * 2)
print()
# code that will iterate over the range generated by range(9) and
# for each element that is between 3 and 7 inclusively print out the result
# of multiplying that element by the second element in the same range.
my_range = range(9)
for i in my_range:
    if i >= 3 and i <= 7: # you can also use (3 <= i <= 7)
        print(i * my_range[1])
print()

# code that will iterate over the range starting at 1, up to but not
# including 11, with a step of 2, and for each element that is between 3 and 8
# inclusively print out the result of multiplying that element by the last element in
# the same range. For any other element of the range (outside [3-8]) print Outside!

my_range = range( 1, 11, 2)
for i in my_range:
    if 3 <= i <= 8:
        print(i * my_range[-1])
    else:
        print("Outside")
print()

# code that will iterate over the range starting at 5, up to
# but not including 25, with a step of 5, and for each element that is between
# 10 and 21 inclusively print out the result of multiplying that element by
# the second to last element of the same range. For any other element of the
# range (outside [10-21]) print Outside! Finally, after the entire range is
# exhausted print out The end!
my_range = range(5, 25, 5)
for i in my_range:
    if 10 <= i <= 21:
        print(i * my_range[-2])
    else:
        print("Outside!")
print("The end")
print()

# a while loop that prints out the value of x times 11 while x is less than
# or equal to 11. When x becomes equal to 10, print out x is 10! Be careful not to
# end up with an infinite loop!
x = 5
while x <= 11:
    print(x * 11)
    if x == 10:
        print("x is 10!")
    x += 1
print()

# break statement
x = [1,2]
y = [10, 100]
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            break
        print(i)
    print(j)
print()
# 
for i in x:
    for j in y:
        if i % 2 ==0:
            print(i * j)
            
        print(i)
        break
    print(j)
print()
# 
for i in x:
    for j in y:
        if i % 2 == 0:
            break
            print(i * j)
        print(i)
    print(j)
print() 

# 
for i in x:
    for j in y:
        if i % 2 ==  0:
            print(i * j)
            continue
        print(i)
    print(j)
    
print()

# 
for i in x:
    for j in y:
        if i % 2 ==  0:
            continue
            print(i * j)
        print(i)
    print(j)
    
print()

# 

for i in range(4):
    print('*'*6)

for i in range(4):
    print('*'*(i + 1))

for i in range(100):
    print(i,"Edigah")

for i in range(100):
    print("Edigah", end = " ")

for i in range(1, 101):
    print(i, " Edigah")

for i in range(1,21):
    print(i," ", i ** 2)
    
for i in range(8, 90, 3):
    print(i, end = ", ")
print()

for i in range(100, 1, -2):
    print(i, end = ", ")
print()

for j in range(10):
    print("A", end = "")
for i in range (7):
    print("B", end  = "")
for k in range(4):
    print("CD", end = "")
else:
    print("E", end = "")
    for m in range(6):
        print("F", end = "")
    print("G")
   
name = str(input("Please enter your name here: "))
n = int(input("Please enter the number of times to print your name here: "))
for i in range(n):
    print(i, " ", name)

#Fibonacci sequence
num  = int(input("How many fibonacci nummber do you want: "))
num1 = 0
num2 = 1
for i in range(0, num):
    if i <= 1:
        next = i
    else:
        next = num1 + num2
        num1 = num2
        num2 = next
    print(next)

#Rectangular Parterns with asterics using for loops
width = int(input("Please enter the width of the rectangle: "))
length = int(input("Please enter the length of the rectangle: "))
for i in range(width):
    print("*"*length)

for i in range(0,width + 1):
    for j in range(0, i+1):
        print("*", end = "")
    print()

for k in range(width, 0, -1):
    for l in range(0, k):
        print("*", end = "")
    print()

print()

for j in range (0, width):
    for i in range(0, j+1):
        print(" ")
        for k in range(0, j+1):
            print("*", end = "")
    print()