import turtle

def draw_line(t):
    t.left(90)
    t.forward(200)
    t.backward(200)
    t.right(90)

def move_gap(t):
    t.penup()
    t.forward(30)
    t.pendown()

wn=turtle.Screen()
moxie=turtle.Turtle()

def threelines(moxie):
    draw_line(moxie)
    move_gap(moxie)

    draw_line(moxie)
    move_gap(moxie)

    draw_line(moxie)

    moxie.penup()
    moxie.backward(60)
    moxie.pendown()
for count in range(10):
 threelines(moxie)
 moxie.left(36)
wn.exitonclick()