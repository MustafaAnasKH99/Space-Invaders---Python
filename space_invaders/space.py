import turtle

window = turtle.Screen()
window.bgcolor('yellow')
window.title('Space Invaders')

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
    
border_pen.hideturtle()

turtle.done()