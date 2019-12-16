# Teach Your Kids How To Build Their Own Game with Python - Part 3

So, without further due, lets pickup from where we left last time.
So far our code creates the main player and allows us to move it, create the enemies, and randomly place them in the battle field.
The code by now looks like this:

```python
import turtle

from random import randint

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

wn.bgpic("bg.gif")

turtle.done() #this just keeps the window open until we close it.
turtle.close() #this just fixes issues related to closing the window
```

Great. Now lets plan what we still have to do before we move on.

 - Keep on moving the enemies towards us as long as they are not dead
 - Allow the player to fire
 - We die if an enemy touches us
 - Sure enough, emenies die if our bullet hits them

Lets tackle this step by step. First lets work on the enemies movement.
You can plan this differently as you wish, but for this tutorial, we will keep it simple. Enemies will keep moving to one of the sides until they reach the white line. When they reach the white line, they will step down towards us and move to the other side of the field. Each time an enemy reaches the white line, it will step closer to us and move again to the other side. If it reaches the bottom of the field without us killing it or it touching us, it will start all over again from the top of the field. Sounds good? Lets get this happening 🚀 .
