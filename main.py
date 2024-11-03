import turtle
from turtle import Turtle, Screen

ken = Turtle()
ken.speed("fastest")
def move_forward():
    ken.forward(10)

def move_back():
    ken.back(10)

def turn_right():
    ken.right(10)

def turn_left():
    ken.left(10)

def clean():
    ken.clear()
    ken.penup()
    ken.home()
    ken.pendown()


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_back, key='s')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=clean, key='c')
screen.exitonclick()