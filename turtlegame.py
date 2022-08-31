#building a turtle game via She Codes Aus Tut - Space Turtle Chomp
import turtle

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("mediumslateblue")

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(1)
mypen.color('coral')
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("coral")
player.shape("turtle")
player.penup()
player.pensize(5)
player.speed(0) 

#Set speed variable
speed = 1

#Define  functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed -= 1

#Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up") 
turtle.onkey(decrease_speed, "Down") 



while True:
    player.forward(speed)

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)