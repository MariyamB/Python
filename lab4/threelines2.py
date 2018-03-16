#source code : threelines2.py
#name:Sai ratnam peri


import turtle
def parallelLines(t,num,length) :
    gap = 30
    t.stamp()
    for i in range(num) :
        t.left(90)
        t.forward(length)
        t.backward(length)
        t.penup()
        t.right(90)
        t.forward(gap)
        t.pendown()
        t.left(90)
        t.forward(length)
        t.backward(length)
        t.penup()
        t.right(90)
        t.forward(gap)
        t.pendown()
        t.left(90)
        t.forward(length)
        t.backward(length)
        t.pendown()
wn=turtle.Screen()
t=turtle.Turtle()
t.pensize(3)
t.speed()
n = 1
size = 200
parallelLines(t, n, size)
wn.exitonclick()