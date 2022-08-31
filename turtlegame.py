#building a turtle game via She Codes Aus Tut - Space Turtle Chomp
import turtle

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("mediumslateblue")


#Create player turtle
player = turtle.Turtle()
player.color("coral")
player.shape("turtle")
player.penup()
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