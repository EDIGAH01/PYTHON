import math
print("calculating the area and circumference of a circle")
radius = int(input("Please enter the radius of your circle: "))
diameter = int(input("Please enter the diameter of your circle: "))
pi = 3.142
area = pi * (radius * radius)
circumference = pi * (radius + radius)
circumference2 = pi * diameter
print("The area of the circle is: ", area)
print("The circumference of the circle using the radius is: ", circumference)
print("The circumference of the circle using the diameter is: ", circumference2)