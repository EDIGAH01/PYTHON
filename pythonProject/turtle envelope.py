import turtle
import math

turtle. forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle. left(90)
turtle.forward(117)
turtle.left(121)
turtle.forward(62)
turtle.up()
turtle.left(90)
turtle.forward(100)
turtle.down()
turtle.left(90)
turtle.forward(62)
turtle.left(120)
turtle.forward(117)
turtle.right(120)
turtle.up()
turtle.forward(59)
turtle.right(90)
turtle.down()
turtle.forward(100)

turtle.up()
turtle.goto(0, -100)
turtle.down()

# Assume the house body is a square and the roof is a right-angled triangle (half a square).

# We can then get the various diagonals using Pythogoras’ Theorem with all angles being multiples
# of 45.
# It seems almost totally unreasonable not to use variables to solve this problem.
sideLength = 40
halfDiagonalLength = 0.5 * math.sqrt ( 2 * ( sideLength ** 2 ) )
# Create the right orientation.
turtle.left ( 90 )
# Draw the house.
turtle.forward ( sideLength )
turtle.right ( 135 )
turtle.forward ( halfDiagonalLength )
turtle.right ( 90 )
turtle.forward ( halfDiagonalLength )
turtle.left ( 135 )
turtle.forward ( sideLength )
turtle.left ( 135 )
turtle.forward ( halfDiagonalLength )
turtle.right ( 90 )
turtle.forward ( halfDiagonalLength )
turtle.left ( 135 )
turtle.forward ( sideLength )
turtle.right ( 135 )
turtle.forward ( halfDiagonalLength )
turtle.right ( 90 )
turtle.forward ( halfDiagonalLength )
turtle.right ( 45 )
turtle.forward ( sideLength )
input("what kind of icecream do you like? ")
