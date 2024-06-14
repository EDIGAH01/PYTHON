# codes for conditionals:

# code that prints out True! if x has 50 characters or more.
x = "The days of Python2 are almost over. Python 3 is the king now."
if len(x)>=50:
    print(True)
print("Here x is : ", x)

# code that prints out True! if x is a
# string and the first character in the string is T.
x = "The days of Python 2are almost over. Python 3 is kingnow"
if type(x) is str and x.startswith("T"):
    print(True)

# code that prints out True! if at least one of
# the following conditions occurs:
# the string contains the character z
# the string contains the character y at least twice
x = "The days for Python 2 are almost over. Python 3 is king now"
if "z" in x and x.count("y") > 2:
    print(True)

# code that prints out True! if the index
# of the first occurrence of letter f is less than 10 and prints out False! if the
# same condition is not satisfied
x = "The days of Python 2 are almost over. Python 3 is king"
if "f" in x < x[11]:
    print(True)
else:
    print(False)

# or

if x.index("f") < 10:
    print(True)
else:
    print(False)

# code that prints out True! if the last 3
# characters of the string are all digits and prints out False! otherwise
x = "The days of Python 2 are almost over. Python 3 is king now"
if type(x[-1:-3]) == int:
    print(True)
else:
    print(False)

# or

if x[-3:].isdigit():
    print(True)
else:
    print(False)

# code that prints out True! if x has at
# least 8 elements and the element positioned at index 6 is a floating-point
# number and prints out False! otherwise.
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if len(x) >= 8 and type(x[6]) == float: # can also use type(x[6]) is float
    print("True")
else:
    print(False)
print("Here x is : ", x)

#  code that prints out True! if the second
# string of the first list in X ends with the letter h and the first string of the second
# list in x also ends with the letter h, and prints out False! otherwise.
if x[3][1].endswith("h") and x[7][0].endswith("h"):
    print(True)
else:
    print(False)

# code that prints out True! if one of the
# following two conditions are satisfied and prints out False! otherwise.
# • the third string of the first list in x ends with the letter h
# • the second string of the second list in x also ends with the letter h
if x[3][2].endswith("h") or x[7][1].endswith("h"):
    print(True)
else:
    print(False)

# code that prints out True ! if the largest
# value among the first 3 elements of the list is less than or equal to the smallest
# value among the next 3 elements of the list. Otherwise, print out False!
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
max = 0
min = 0
for i in x[0:2]:
    if i > max:
        max = i

for j in x[3:5]:
    if j < min:
        min = j

if i <= j :
    print(True)
else:
    print(False)
print("Here x is : ", x)

# print(min(x[3:6])) # throws type error 'int' and 'float' are not callable
# print(max(x[:3]))

# if max(x[0:3]) <= min(x[3:6]):
#     print(True)
# else:
#    print(False)

#  code that prints out True! if 115 appears
# at least once inside the list or if it is the first element in the list.
# Otherwise, print out False

if 115 in x or 115 is x[0]:
    print(True)
else:
    print(False)

# or

if x.count(115) >= 1 or x.index(115) == 0:
    print(True)
else:
    print(False)

#  code that prints out True! if the value
# associated with key number 5 is Perl or the number of key-value pairs in the
# dictionary divided by 5 returns a remainder less than 2. Otherwise, print out
# False!
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "c#", 7: "c++"}
if x[5]  is 'Perl' or (x.count()) % 5 < 2: # in (x.count()) you can also use len(x)
    print(True)
else:
    print(False)
print("Here x is : ", x)

# code that prints out True! if 3 is a key
# in the dictionary and the smallest value (alphabetically) in the dictionary is
# C#. Otherwise, print out False!
if 3 in x and sorted(x.values())[0] == "c#":
    print(True)
else:
    print(False)

# code that prints out True! if the last
# character of the largest (alphabetically) value in the dictionary is n. Otherwise,
# print out False!
if sorted(x.values())[6].endswith("n"): # use this if only you know the number of values in the dictionary.
    print(True)
else:
    print(False)

# or

if sorted(x.values())[-1][-1] == "n":
    print(True)
else:
    print(False)

print(x.keys())

# write code that prints out True! if the
# largest key in the dictionary divided by the second largest key in the
# dictionary returns a remainder equal to the smallest key in the dictionary.
# Otherwise, print out False!
if (sorted(x.keys())[-1]) / (sorted(x.keys())[-2]) == sorted(x.keys())[0]:
    print(True)
else:
    print(False)

# code that prints out True! if the sum of all
# the keys in the dictionary is less than the number of characters of the string
# obtained by concatenating the values associated with the first 5 keys in the
# dictionary. Otherwise, print out False!
if sum(x.keys()) < len(x[1] + x[2] + x[3] + x[4] + x[5]):
    print(True)
else:
    print(False)

#  code that prints out True! if the 3rd
# element of the first range is less than 2, prints out False! if the 5th element of the
# first range is 5, and prints out None! otherwise.
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if x[0][2] < 2:
    print(True)
elif x[0][4] is 5:
    print(False)
else:
    print("Here x is : ", x)
    print(None)

#  code that prints out True! if the 3rd
# element of the 3rd range is less than 6, prints out False! if the 1 st element of the
# second range is 5, and prints out None ! otherwise.
if x[2][2] < 6:
    print(True)
elif x[1][0] is 5:
    print(False)
else:
    print(None)

# code that prints out True! if the
# last element of the first range is greater than 3, prints out False! if the last
# element of the second range is less than 9, and prints out None! otherwise.

if x[0][-1] > 3:
    print(True)
elif x[1][-1] < 9:
    print(False)
else:
    print(None)

#  code that prints out True! if the length of
# the first range is greater than or equal to 5, prints out False! if the length of the
# second range is 4, and prints out None! otherwise.
if len(x[0]) >= 5:
    print(True)
elif len(x[1]) is 4:
    print(False)
else:
    print(None)

# e code that prints out True! if the sum
# of all the elements of the first range is greater than the sum of all the
# elements of the third range, prints out False! if the largest element of the
# second range is greater than the largest element of the third range, and
# prints out None! otherwise.
max1 = 0
max2 = 0
for i in x[1]:
    if i > max1:
        max1 = i
print(max1)

for j in x[2]:
    if j > max2:
        max2 = j
print(max2)

if sum(x[0]) > sum(x[2]):
    print(True)
elif max1 > max2:
    print(False)
else:
    print(None)

#  code that prints out True! if the largest
# element of the first range minus the second element of the 3rd range is equal to
# the first element of the first range, prints out False! if the length of the first range
# minus the length of the 2nd range is equal to the first element of the 3rd range,
# prints out Maybe! if the sum of all the elements of the 3rd range divided by 2
# returns a remainder of 0, and prints out None! otherwise.

max0 = 0
for k in x[0]:
    if k > max0:
        max0 = k
print(max0)

if (max0 - x[2][1]) == x[0][0]:
    print(True)
elif len(x[0]) - len(x[1]) == x[2][0]:
      print(False)
elif sum(x[2]) % 2 is 0:
    print("Maybe!")
else:
    print(None)

#  code that prints out True! if the sum
# of the last 3 elements of the first range plus the sum of the last 3 elements of
# the 3rd range is equal to the sum of the last 3 elements of the 2nd range, and
# prints out False! if the length of the first range times 2 is less than the sum
# of all the elements of the 3rd range
if ((x[0][-1]+ x[0][-2]+ x[0][-3]) + (x[2][-1] + x[2][-2] + x[2][-3])) == (x[1][-1] + x[1][-2] + x[1][-3]):
    print(True)
elif len(x[0]) * 2 < sum(x[2]):
    print(False)

# or
# Note sum iterates with n++ and not n-- so sum(x[0][-1:-3]) wil not work
if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print(True)
elif len(x[0]) * 2 < sum(x[2]):
    print(False)

#  code that prints out True! if the 2nd
# character of the value at key 1 is also present in the value at key 4, and prints out
# False! otherwise.
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if x[1][1] in x[4]:
    print(True)
else:
    print(False)
print("Here x is : ", x)

# 
if x[3][-2] is x[5][0]:
    print(True)
else:
    print(False)

#  code that prints out True! if the number of
# characters of the smallest value in the dictionary is equal to the number of
# occurrences of letter a in the value at key 3, and prints out False! otherwise.
for val in x.values():
    x = x[1] [0]
    if val < x:
        x = val

if len(val) ==  x[3].count("a"):
    print(True)
else:
    print(False)
