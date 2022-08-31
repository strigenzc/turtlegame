#building a turtle game via She Codes Aus Tut - Space Turtle Chomp

import turtle

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('mediumslateblue')

# Create player turtle
player = turtle.Turtle()
player.color('coral')
player.shape('turtle')
player.penup()

# Set speed variable
speed = 1

while True:
    player.forward(speed)