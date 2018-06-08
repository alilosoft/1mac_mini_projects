import turtle

def draw_polygon(t, color, radius, s):
    t.color(color)
    t.circle(radius, steps=s)

def draw_fractals():
    t = turtle.Turtle(shape="turtle")
    t.pensize(2)
    t.speed(10)

    for i in range(10):
        draw_polygon(t, "green", 70, 7)
        t.right(36)
        draw_polygon(t, "yellow", 120, 3)
        t.right(36)
        draw_polygon(t, "magenta", 140, 5)
        t.right(36)

def picasso():
    draw_board = turtle.Screen()
    draw_board.bgcolor("black")
    draw_fractals()
    draw_board.exitonclick()

picasso()
