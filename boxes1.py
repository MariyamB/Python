# Inner Squares
import turtle

wn = turtle.Screen ()
# wn.bgcolor("blue") color the background
maria = turtle.Turtle ()  # constructor initialization
maria.stamp ()  # draws the turtle shape of the current location
maria.penup()
maria.forward(50)
maria.pendown()
maria.left(90)
maria.forward(50)
maria.left(90)
maria.forward(100)
maria.left(90)
maria.forward(100)
maria.left(90)
maria.forward(100)
maria.left(90)
maria.forward(50)
maria.penup()
maria.right(90)
maria.forward(10)
maria.pendown()
maria.left(90)
maria.forward(60)
maria.left(90)
maria.forward(120)
maria.left(90)
maria.forward(120)
maria.left(90)
maria.forward(120)
maria.left(90)
maria.forward(60)
wn.exitonclick ()