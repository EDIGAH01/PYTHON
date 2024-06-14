print("Calculating the surface are, volume and perimeter of a cuboid")
width = int(input("Please enter the width of your cuboid: "))
length = int(input("Please enter the length of your cuboid: "))
area = (2 * (width * width)) * (4 * (length * width))
volume = (2 *(width * width)) * length
perimeter = ((width * 4) * 2) + (4 * (2 * (length + width)))
print("The are of the cuboid is: ", area)
print("The volume of the cuboid is: ", volume)
print("The perimeter of the cubid is: ", perimeter)