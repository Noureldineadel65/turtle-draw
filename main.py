import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_right():
    tim.right(45)


def turn_left():
    tim.left(45)


screen.title("Welcome to Nour Paint!")


tim.setx(turtle.window_width() / 20)
tim.sety(turtle.window_height() / 20)

screen.bgcolor("black")
tim.color("white")

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)


screen.exitonclick()