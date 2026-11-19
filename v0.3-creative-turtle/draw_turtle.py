import turtle
from pathlib import Path
from PIL import Image

folder = Path(__file__).resolve().parent
background_file = folder / "background.gif"

# pillow creates the background image
Image.new("RGB", (900, 650), "#080820").save(background_file, "GIF")

# turtle opens the background and draws the picture
screen = turtle.Screen()
screen.setup(900, 650)
screen.title("ayush creative sea turtle")
screen.bgpic(str(background_file))
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def polygon(points, colour):
    pen.penup()
    pen.goto(points[0])
    pen.color(colour)
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()

def circle(x, y, radius, colour):
    pen.goto(x, y - radius)
    pen.color(colour)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()

# four flippers
polygon([(-80, 30), (-210, 110), (-180, -20), (-90, -60)], "#00bcd4")
polygon([(80, 30), (210, 110), (180, -20), (90, -60)], "#ff9800")
polygon([(-80, -30), (-190, -150), (-40, -100)], "#e040fb")
polygon([(80, -30), (190, -150), (40, -100)], "#00c853")

# shell
circle(0, 0, 115, "#ffeb3b")
circle(0, 0, 95, "#00bcd4")
polygon([(-80, 35), (0, 90), (75, 35), (45, -65), (-45, -65)], "#ff1744")
polygon([(-80, 35), (-45, -65), (-100, -25)], "#ff9800")
polygon([(75, 35), (45, -65), (100, -25)], "#e040fb")

# head and eyes
circle(0, 150, 48, "#00c853")
circle(-17, 165, 7, "white")
circle(17, 165, 7, "white")
circle(-17, 165, 3, "black")
circle(17, 165, 3, "black")

# tail
polygon([(-25, -105), (25, -105), (0, -175)], "#ff9800")

screen.update()
print("turtle drawing completed")
screen.mainloop()
