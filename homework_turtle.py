import turtle

# set up the drawing window
screen = turtle.Screen()
screen.title("ayush 8092 turtle homework")
screen.bgcolor("white")

# create the turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

# draw a square
for side in range(4):
    pen.forward(150)
    pen.right(90)

# write the project name
pen.penup()
pen.goto(0, -30)
pen.write("Ayush-8092", align="center", font=("Arial", 16, "normal"))

# keep the window open until it is closed
turtle.done()
