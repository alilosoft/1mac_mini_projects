import turtle

def draw_square():
    t = turtle.Turtle(shape="turtle")
    t.color("yellow")
    for i in range(4):
        t.forward(200)
        t.right(90)

def draw_circle():
    t = turtle.Turtle()
    t.color("blue")
    t.circle(100)

def picasso():
    draw_board = turtle.Screen()
    draw_board.bgcolor("red")

    draw_square()
    draw_circle()

    draw_board.exitonclick()

picasso()

