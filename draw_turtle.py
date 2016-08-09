import turtle

def draw_square(z_turtle):
    for x in range(1,5):
        z_turtle.forward(100)
        z_turtle.right(90)
        x = x + 1

def draw_triangle(z_turtle):
    for x in range(1,4):
        z_turtle.forward(100)
        z_turtle.right(120)
        x = x + 1

def square_circle(z_turtle):
    z_turtle.penup()
    z_turtle.goto(-510, 0)
    z_turtle.pendown()
    for x in range(1,37):
        draw_square(z_turtle)
        z_turtle.right(10)

def triangle_circle(z_turtle):
    for x in range(1,37):
        draw_triangle(z_turtle)
        z_turtle.right(10)

def turtx():
    window = turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    triangle_circle(brad)
    square_circle(brad)

    window.exitonclick()

turtx()