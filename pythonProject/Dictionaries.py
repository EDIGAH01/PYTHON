crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
value = crypto[4] # using indexing
print(value)

value = crypto.get(4) # using a method
print(value)

crypto[4] = "Cardano" # updating the dictionary
print(crypto[4])

crypto[6] = "Monero" # adding a key-value pair to the dictionary
print(crypto[6])

number = len(crypto) # returning the number of key-value pairs in the dictionary
print(number)

del crypto[3] # deleting a key-value pair without using a method
print(crypto)

crypto[3] = "Litecoin"
print(crypto)

crypto.pop(3) # deleting a key-value pair using a method
print(crypto)

crypto[3] = "Litecoin"
print(crypto)

check = 7 not in crypto # checking if a value is a key-value pair in the dictionary
print(check)

crypto.clear() # Deleting all the key-value pair from the dictionary
print(crypto)

crypto = {1: "Bitcoin", 2: "Ethreum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}

result = crypto.items() # Putting the key value pairs in to a list of tuples
print(list(result))

add = sum(crypto) # Getting the sum of all the keys in the dictionary
print(add)

val = crypto.values() # getting a list of all the values in the dictionary
print(list(val))

key = min(crypto) # finding the smallest key in the dictionary
print(key)

keys = crypto.keys() # printing a list of all the keys in the dictionary
print(list(keys))

crypto.popitem() # returning and removing an arbitrary key-value pair from the dictionary
print(len(crypto))
print(crypto)

