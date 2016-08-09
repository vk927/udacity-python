# in this pgm we will draw M and draw o (circle), in the same way you can draw your name
import turtle

def turtx():
    window = turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    # draws |
    brad.right(90)
    brad.forward(100)
    brad.backward(100)

    # draws |\
    brad.left(45)
    brad.forward(45)

    # draws |\/
    brad.left(90)
    brad.forward(45)

    # draws |\/|
    brad.right(135)
    brad.forward(100)
    brad.backward(100)

    # draws |\/| and moves turtle positions
    brad.penup()
    brad.goto(90,-45)
    brad.pendown()

    # draws a circle
    brad.circle(40)


    window.exitonclick()

turtx()