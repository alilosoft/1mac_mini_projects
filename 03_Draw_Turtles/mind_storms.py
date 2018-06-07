import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    t = turtle.Turtle(shape="turtle")
    t.color("yellow")
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)

    t = turtle.Turtle()
    t.color("blue")
    t.circle(100)
    window.exitonclick()

draw_square()

