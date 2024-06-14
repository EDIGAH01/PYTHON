value = 10 # converting a decimal number/an integer to a string value
conv = str(value)
print(type(conv))
print(conv)

value = "10" # converting a string to an integer
conv = int(value)
print(type(conv))

value = 10 # converting an int value to a float value
conv = float(value)
print(type(conv))

value = "Hello!" # converting a string to a list
conv = list(value)
print(type(conv))
print(conv)

value = [ 1, 2, 3, 10, 20, 30] # converting a  list to a tuple
conv = tuple(value)
print(type(conv))
print(conv)

value = (10, 20, 40, 10, 25, 30, 45) # convertig to a frozen set
conv= frozenset(value)
print(type(conv))
print(conv)

value = 10 # cnverting a decimal value to a binary number
conv = bin(value)
print(type(conv))
print(conv)

value = 10 # converting decimal number to hexadecimal value
conv = hex(value)
print(type(conv))
print(conv)

value = '0b1010' # converting binary number to decimal notation
conv = int(value, 2)
print(type(conv))
print(conv)

value = '0xa' # Converting hexadecimal value to decimal notation
conv = int(value, 16)
print(type(conv))
print(conv)