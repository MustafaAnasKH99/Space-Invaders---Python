#  This file is for the follow up tutorial 🐢
import turtle

from random import randint
from tkinter import PhotoImage

pen = turtle.Turtle()

turtle.register_shape("ship.gif")
turtle.register_shape("invador.gif")

pen.penup()
pen.setposition(-300,300)
pen.pendown() #this line puts the pen on the paper
for side in range(3): #see number three? its what reminds Python,  THREE times!
  pen.forward(600)
  pen.right(90)
pen.forward(600)
pen.hideturtle()

player = turtle.Turtle()
player.shape('ship.gif')
player.penup()

enemies = []
for i in range(10):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    x = randint(-300, 300)
    y = randint(0, 300)
    enemy.penup()
    enemy.setposition(x, y)
    enemy.shape('invador.gif')

def moveRight():
    x = player.xcor()
    x += 10
    player.setx(x)



def moveLeft():
    x = player.xcor()
    x -= 10
    player.setx(x)  

def moveForward():
    print('something')
    y = player.ycor()
    y += 10
    player.sety(y)

def moveBackward():
    y = player.ycor()
    y -= 10
    player.sety(y)

wn = turtle.Screen()
wn.listen()

wn.onkey(moveRight, 'd')
wn.onkey(moveLeft, 'a')
wn.onkey(moveForward, 'w')
wn.onkey(moveBackward, 's')

turtle.done() #this just keeps the window open until we close it.
turtle.close() #this just fixes issues related to closing the window