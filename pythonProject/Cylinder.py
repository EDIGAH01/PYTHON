print("Calculating the surface area and volume of a cylinder.")
radius = int (input("Please enter the radius of your cylinder: "))
height = int(input("Please enter the height of your cylinder: "))
pi = 3.142
area = ((pi * (radius * radius)) * 2) * (( pi * (radius + radius)) * height )
volume = (pi * (radius * radius)) * height
print("The surface area of the cylinder is: ", area)
print("The volume of the cylinder is: ", volume)