import turtle
import os

window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders')

#Draw Border
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


#Initiate Player
player = turtle.Turtle()
player.setposition(0, -250)
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setheading(90)


#Initiate Enemy
enemy = turtle.Turtle()
enemy.setposition(0, 250)
enemy.color('red')
enemy.shape('triangle')
enemy.penup()
enemy.speed(0)
enemy.setheading(270)

#Set Speed
player_speed = 15
enemy_speed = 15


# Player Motion
def move_player_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_player_right():
    x = player.xcor()
    x += player_speed   
    if x > 280: 
        x = 280
    player.setx(x)

def move_player_up():
    y = player.ycor()
    y += player_speed
    player.sety(y)

def move_player_down():
    y = player.ycor()
    y -= player_speed
    player.sety(y)

# Enemy Motion:
def move_enemy_left():
    x = enemy.xcor()
    x -= enemy_speed
    if x < -280:
        x = -280
    enemy.setx(x)

def move_enemy_right():
    x = enemy.xcor()
    x += enemy_speed   
    if x > 280: 
        x = 280
    enemy.setx(x)

def move_enemy_down():
    y = enemy.ycor()
    y -= enemy_speed
    enemy.sety(y)

def move_enemy_up():
    y = enemy.ycor()
    y += enemy_speed
    enemy.sety(y)


#Events Listeners
turtle.listen()
turtle.onkey(move_player_left, 'a')
turtle.onkey(move_player_right, 'd')
turtle.onkey(move_player_up, 'w')
turtle.onkey(move_player_down, 's')

turtle.onkey(move_enemy_left, 'Left')
turtle.onkey(move_enemy_right, 'Right')
turtle.onkey(move_enemy_up, 'Up')
turtle.onkey(move_enemy_down, 'Down')


turtle.done()
