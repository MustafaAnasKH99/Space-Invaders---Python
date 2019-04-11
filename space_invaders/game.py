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
enemy.shape("circle")
enemy.setposition(-200, 250)
enemy.color('red')
enemy.penup()
enemy.speed(2)
enemy.setheading(270)

#Set Speed
player_speed = 15
enemy_speed = 15

#Create the Player's Weapon:
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 20
bullet_state = 'ready'



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

def fire_bullet():
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


#Events Listeners
turtle.listen()
turtle.onkey(move_player_left, 'a')
turtle.onkey(move_player_right, 'd')
turtle.onkey(move_player_up, 'w')
turtle.onkey(move_player_down, 's')
turtle.onkey(fire_bullet, 'space')

# Enemy Motion / Main Loop:
while True:
    #Move Enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = 'ready'

    if bullet.ycor() == enemy.ycor():
        print('won!')

turtle.done()
