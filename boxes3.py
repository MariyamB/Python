import turtle

wn = turtle.Screen ()
# wn.bgcolor("blue") color the background
maria = turtle.Turtle ()  # constructor initialization
maria.stamp ()  # draws the turtle shape of the current location
maria.penup()
maria.forward(80)
maria.penup()
maria.left(90)
maria.pendown()
maria.forward(80)
maria.left(90)
maria.forward(160)
maria.left(90)
maria.forward(160)
maria.left(90)
maria.forward(160)
maria.left(90)
maria.forward(80)
maria.circle(80,100)
maria.circle(80,100)
maria.circle(80,100)
maria.circle(80,100)
wn.exitonclick ()
