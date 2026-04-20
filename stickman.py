import turtle

t = turtle.Turtle()
t.speed(3)

# Head
t.penup()
t.goto(0, 50)
t.pendown()
t.circle(20)

# Body
t.penup()
t.goto(0, 50)
t.setheading(-90)
t.pendown()
t.forward(80)

# Left arm
t.penup()
t.goto(0, 20)
t.setheading(225)
t.pendown()
t.forward(40)

# Right arm
t.penup()
t.goto(0, 20)
t.setheading(-45)
t.pendown()
t.forward(40)

# Left leg
t.penup()
t.goto(0, -30)
t.setheading(225)
t.pendown()
t.forward(50)

# Right leg
t.penup()
t.goto(0, -30)
t.setheading(-45)
t.pendown()
t.forward(50)

turtle.done()
