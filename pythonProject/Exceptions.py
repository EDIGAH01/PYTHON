# Debugging code to eradicate errors before they occur 
# 0
x = [1, 2]
y = [10, 100]
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
print()

# 1
for i in x:
    for  j in y:
        if i % 2 == 0:
            print(i * j)
print()

# 2
for i in x:
    for j in y:
        if i % 2 == 0 and j / 2 == 50:
            print(x[1]*y[1])
print()

# 3
try:
    print(25 % 0)
except ZeroDivisionError: 
    print("Zero!")
print()

# 4
try:
    print(25 % 5 **5 + 5)
except:
    print("Bug!")
else:
    print("Clean!")
print()

# 5
try:
    print(25 % 0 **5+5)
except:
    print("Bug!")
finally:
    print("Result!")
print()

# 6
x = [1, 9, 17, 32]
try:
    print(x[3]%3**5+x[4])
except ZeroDivisionError:
    print("Zero!")
except IndexError:
    print("Index!")
print()

# 7
try:
    print(25 % 5 ** 5 + 5)
    print("Clean!")
except ZeroDivisionError:
    print("Zero!")
finally:
    print("Finish!")
print()

# 8
