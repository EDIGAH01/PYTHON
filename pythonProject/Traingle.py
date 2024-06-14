print("Calculating the are and perimeter of a triangle")
base = int(input("Please enter the base of your triangle: "))
height = int(input("Please enter the height of your triangle: "))
hypotenuse = int(input("Please enter the hypotenuse of your triangle: "))
area = 0.5*(base * height )
perimeter = hypotenuse + base + height
print("The area of the triangle is: ", area)
print("The perimeter of the triangle is:", perimeter)