import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("ayush creative turtle")

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "yellow", "cyan", "lime", "magenta"]

for i in range(36):
    pen.color(colors[i % len(colors)])
    for j in range(4):
        pen.forward(100)
        pen.right(90)
    pen.right(10)

turtle.done()
