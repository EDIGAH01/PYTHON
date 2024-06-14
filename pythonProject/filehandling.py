# Add the necessary code in between print's parentheses in order to read
# the content of test.txt as a string and have the result printed out to the
# screen.
# f = open("test.txt", "r")
# print()


f = open("hello.py", "r")
print(f.read())
print()

# Add the necessary code in between print's parentheses in order
# to read the content of test.txt as a list where each element of the list is a
# row in the file, and have the result printed out to the screen.
# f = open("test.txt", "r")
# print()

f = open("hello.py", "r")
print(f.readlines())
print()

#Add the necessary code on line 5 in order to bring back the cursor at the
# very beginning of test.txt before reading from the file once again.
# f = open("test.txt", "r")
# f.read()
# print(f.read())

f = open("hello.py", "r")
f.read()
f.seek(0)
print(f.read())
print()

#  Add the necessary code on line 5 (in between the parentheses of
# print()) in order to get the current position of the cursor inside test.txt and
# have the result printed out to the screen.
# f = open("test.txt", "r")
# f.read(5)
# print()

f = open("hello.py", "r")
f.read(5)
print(f.tell())
print()

#  Add the necessary code on line 5 (in between the parentheses of print()) in
# order to get the current mode in which test.txt is open (read, write etc.) and have
# the result printed out to the screen.
# f = open("test.txt", "r")
# f.read(5)
# print()

f = open("hello.py", "r")
f.read(5)
print(f.mode)
print()

# Add the necessary file access mode on line 1 in order to open test.txt for
# appending and reading at the same time.
# f = open("test.txt", )
# print(f.mode)


f = open("hello.py","a+")
print(f.mode)
print()

#  Add the necessary code on lines 3 and 4 in order to write the string python
# to test.txt and have the result of reading the file printed out to the screen.
# f = open("test.txt", "w")
# f = open("test.txt", "r")
# print(f.read())

f = open("hello.py", "w")
f.write("python")
f.close()
f = open("hello.py", "r")
print(f.read())
print()

#  Add the necessary code on lines 3 and 4 in order to write a list of
# strings ['python', ' ', 'and', ' 'java'] to test.txt and have the result of reading the
# file printed out to the screen.
# f = open("test.txt", "w")
# f = open("test.txt", "r")
# print(f.read())

f = open("hello.py", "w")
f.writelines(['python', ' ', 'and', ' ', 'java'])
f.close()
f = open("hello.py", "r")
print(f.read())
print()

# Add the necessary code starting at line 1 in order to write the string python
# and also close test.txt properly using the with statement.
# f = open("test.txt", "r")
# print(f.read())

with open("hello.py", "w")as f:
    f.write("python")
f = open("hello.py", "r")
print(f.read())
print()

#  Add the necessary code on lines 4 and 5 in order to delete the entire
# content of test.txt.
# with open("test.txt", "w") as f:
# f.write("python")
# f = open("test.txt", "r")
# print(f.read())

with open("hello.py", "w") as f:
    f.write("python")
f = open("hello.py", "r+")
f.truncate()
f = open("hello.py", "r")
print(f.read())
print()

# writting back the line of code back to hello.py

with open("hello.py", "w") as f:
    f.write('print( "Hello world")')
    f.close()
f = open("hello.py", "r")
print(f.read())
f.close()
print()

with open("hello.py", "a+") as f:
    f.write('print("Hi! My name is Edigah, my c++ code is not running, can you help?")')
f = open("hello.py", "r")
print(f.read())
f.close()
print()

with open("hello.py", "r") as f:
    print(f.read())
    f.close()
print()