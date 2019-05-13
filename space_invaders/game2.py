import turtle
import random

window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders')

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()

player = turtle.Turtle()
player.setposition(0, -250)
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setheading(90)

enemies = []
for i in range(5):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.penup()
    enemy.color('yellow')
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

def moveRight():
    x = player.xcor()
    x += 10
    player.setx(x)

def moveLeft():
    x = player.xcor()
    x -= 10
    player.setx (x)

def moveUp():
    y = player.ycor()
    y += 10
    player.sety(y)

def moveDown():
    y = player.ycor()
    y -= 10
    player.sety(y)

turtle.listen()
turtle.onkey(moveRight, 'Right')
turtle.onkey(moveLeft, 'Left')
turtle.onkey(moveDown, 'Down')
turtle.onkey(moveUp, 'Up')

turtle.done()

