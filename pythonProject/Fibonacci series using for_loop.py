a = int(input("Please enter the range here: "))
first_value = 0
second_value = 1
for i in range(0,a):
    if i<=1:
        next = i
    else:
        next = first_value + second_value
        first_value = second_value
        second_value =next
    print(next)