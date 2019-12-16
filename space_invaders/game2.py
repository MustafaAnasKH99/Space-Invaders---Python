#  This file is for the follow up tutorial 🐢
import turtle
import math

from random import randint

score = 0
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

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90) #this just makes the triangular turtle head towards the top of the screen
bullet.shapesize(2, 2)
bullet.hideturtle()
bullet_speed = 50
bullet_state = 'ready' #???

turtle.color("white")
turtle.penup()
turtle.setposition(-300, 250)
turtle.write("Your score is: {}".format(score), move=False, align="left", font=("Arial", 18, "normal"))
turtle.hideturtle()

def moveRight():
  x = player.xcor()
  x += 10
  player.setx(x)


def moveLeft():
    x = player.xcor()
    x -= 10
    player.setx(x)  

def moveForward():
    y = player.ycor()
    y += 10
    player.sety(y)

def moveBackward():
    y = player.ycor()
    y -= 10
    player.sety(y)

def fire_bullet():
    # the global word makes bullet_state accessible from whitin the function. If you remove it, the code breaks
    global bullet_state 
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor() # get the x location of the player
        y = player.ycor() + 10 # get the y location of the player
        bullet.setposition(x, y) # move the bullet to where the player is
        bullet.showturtle() # show the bullet

def isCollosion(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 35:
        return True
    else:
        return False

wn = turtle.Screen()
wn.listen()

wn.onkey(moveRight, 'd')
wn.onkey(moveLeft, 'a')
wn.onkey(moveForward, 'w')
wn.onkey(moveBackward, 's')
wn.onkey(fire_bullet, 'space')

wn.bgpic("bg.gif")

enemy_speed = 30 # this is the speed of our enemies - You can change it to make them faster/slower

while True:
    for enemy in enemies: # go through the enemies one by one
        if isCollosion(player, enemy):
          player.hideturtle()  #hide player from the arena
          turtle.color('red')
          turtle.penup()
          turtle.setposition(0, 0)
          turtle.write("Game Over!", move=False, align="center", font=("Arial", 35, "normal"))
          turtle.setposition(0, -50) #Go to a new line      
          turtle.write("Your score is: {}".format(score), move=False, align="center", font=("Arial", 35, "normal"))
          turtle.done()  #Stop Game
          break

        if isCollosion(bullet, enemy):
          bullet.hideturtle()
          bullet_state = 'ready' #make the state ready to allow firing again
          enemy.setposition(-300, 300)
          score += 1
          turtle.clear()
          turtle.color("white")
          turtle.penup()
          turtle.setposition(-300, 250)
          turtle.write("Your score is: {}".format(score), move=False, align="left", font=("Arial", 18, "normal"))
          turtle.hideturtle()

        if enemy.xcor() > 270: # check if the enemy hit the white line
          y = enemy.ycor() # get the current y location of the enemy
          y -= 40 # change the y location of the enemy by 40
          enemy.sety(y) # move it closer to us by y which is 40
          enemy.speed(0) # this makes the transition seems instant
          enemy.setx(-270) # move the enemy to the left side again

        if enemy.ycor() < -260: # check if the enemy hit the bottom white line
            y = 300  # set y to the new location at the top of the screen
            enemy.speed(0) # this makes the transition seems instant
            enemy.sety(y)  # move the enemy to the new location

        if bullet_state == 'fire': # check if the state of the bullet is fire
            y = bullet.ycor() # get the y location of the bullet
            y += bullet_speed # increase the y location of the bullet by its speed
            bullet.sety(y) # move the bullet to the new location

        if bullet.ycor() > 275: # check if the bullet hit the top white line
            bullet.hideturtle() # hide the billet
            bullet_state = 'ready' # change its state to ready to enable the player to fire again
        
        x = enemy.xcor() # get the current x location of the enemy
        x += enemy_speed # change the x location of the enemy by its speed which is 30
        enemy.setx(x) # move the enemy to its new x location

turtle.done() #this just keeps the window open until we close it.
turtle.close() #this just fixes issues related to closing the window