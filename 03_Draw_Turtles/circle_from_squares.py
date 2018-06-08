# encoding: utf-8
# Steps to draw a circle out of squares
# 1- Draw a square
# 2- Turn right/left with a small angle (ex: 10°)
# 3- Repeat steps 1 & 2 until completing a full circle (360°)

import turtle

def draw_square(a_turtle):
    for i in range(4):
        a_turtle.forward(200)
        a_turtle.right(90)

def circle_of_squares():
    t = turtle.Turtle(shape="turtle")
    t.color("green yellow")
    t.pensize(2)
    t.speed(10)

    for i in range(36):
        draw_square(t)
        t.right(10)

def picasso():
    draw_board = turtle.Screen()
    draw_board.bgcolor("black")
    circle_of_squares()
    draw_board.exitonclick()

picasso()
