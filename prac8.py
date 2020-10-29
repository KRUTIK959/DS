import turtle
from turtle import *
import math

root = turtle.Screen()
root.bgcolor('lightblue')
t = turtle.Turtle()
t.pu()
t.goto(0,-280)
t.speed(0)
t.pd()
t.begin_fill()
t.color('brown')
t.fd(750)
t.left(135)
t.fd(550)
t.left(90)
t.fd(550)
t.right(90)
t.fd(550)
t.left(95)
t.fd(510)
t.left(130)
t.fd(750)
t.end_fill()
t.pu()
t.back(30)
t.goto(-20,-400)
t.shape('circle')
t.color('yellow')
t.shapesize(5)
t.speed(1)
t.left(90)
while True:
    t.pu()
    root.update()
    t.fd(10)


root.exitonclick()

