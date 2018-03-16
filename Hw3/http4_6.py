import turtle

wn = turtle.Screen()
alex = turtle.Turtle() # need parens
sides = int(input("Enter the number of sides: "))
angle = 360 / sides
length = int(input("Enter the length of sides: "))
line_color = input("Enter the color of the lines: ") # takes input like "red" or "black" etc..
alex.color(line_color)
fill_color = input("Enter the fill color for the polygon:" )
alex.fillcolor(fill_color)
alex.begin_fill()
for i in range(sides):
    alex.forward(length)  # added 44, you had an undefined variable there which is not valid
    alex.left(angle)
alex.end_fill()
wn.exitonclick ()