import turtle

wn = turtle.Screen ()
# wn.bgcolor("blue") color the background
maria = turtle.Turtle ()  # constructor initialization
maria.pensize(3)
maria.right(90)
maria.forward(200)
maria.left(90)
maria.penup()
maria.forward(30)
maria.pendown()
maria.left(90)
maria.forward(200)
maria.right(90)
maria.penup()
maria.forward(30)
maria.pendown()
maria.right(90)
maria.forward(200)
wn.exitonclick ()