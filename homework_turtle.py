import turtle


def main():
    screen = turtle.Screen()
    screen.title("ayush 8092 turtle homework")
    screen.bgcolor("white")
    screen.setup(width=600, height=450)

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(4)
    pen.color("navy")

    # draw a square around the centre of the window
    pen.penup()
    pen.goto(-75, 75)
    pen.pendown()
    for _ in range(4):
        pen.forward(150)
        pen.right(90)

    pen.penup()
    pen.goto(0, -125)
    pen.color("black")
    pen.write("Ayush-8092", align="center", font=("Arial", 18, "normal"))
    pen.hideturtle()
    turtle.done()


if __name__ == "__main__":
    try:
        main()
    except turtle.TurtleGraphicsError as error:
        raise SystemExit(
            "could not open the turtle drawing window. run this program on a computer with a desktop display. "
            f"details: {error}"
        )
