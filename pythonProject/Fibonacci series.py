a = int(input("Please enter the range you want: "))
first_value = 0
second_value = 1
i = 0
while i < a :
    if i <= 1:
        next  = i
    else:
        next = first_value + second_value
        first_value = second_value
        second_value = next
    print(next)
    i+=1