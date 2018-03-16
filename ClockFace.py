#!/usr/bin/python3.5
import turtle
wn = turtle.Screen ()
wn.bgcolor("green")
turtle.shape('turtle')
turtle.color("blue")
turtle.stamp()
move=30
for i in range(12):
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(25)
    turtle.penup()
    turtle.forward(15)
    turtle.stamp()
    turtle.home()
    turtle.right(move)
    move=move+30
turtle.exitonclick ()
