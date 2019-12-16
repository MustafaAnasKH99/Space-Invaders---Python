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
 - Display our score on the screen
 - Sure enough, emenies die if our bullet hits them

Lets tackle this step by step. First lets work on the enemies movement.
You can plan this differently as you wish, but for this tutorial, we will keep it simple. Enemies will keep moving towards the right side until they reach the white line. When they reach the white line, they will step down towards us, start again from the left side, and move towards the right side. Each time an enemy reaches the right white line, it will step closer to us and start over from the left side. If it reaches the bottom of the field without us killing it or it touching us, it will start all over again from the top of the field. If we manage to hit it with a bullet, we will make it start all over again from the top. Sounds good? Lets get this happening 🚀 .

> Move the enemies
Notice that our aim is to _keep_ on moving the enemies in one direction, *unless* they hit the white line, in which case we will make it start from the left side again.
So the first step is to _keep_ on moving the enemy. This means that we need to write a piece of code that will *always* run. In code, we call this an *infinite loop*. Anything inside an infinite loop keep on running until we tell it to stop.

to create an infinite loop in Python we write: 
```python
while Ture:
    # this is the body of the loop
```

No we will write the code that moves the enemies in the _body_ of the infinite loop.
Remember the _methods_ `xcor()` and `ycor()` we used to move our player? we will use the same _methods_ to move the emeies. Lets define the speed of the enemies and move them by writing the body of the loop

```python
enemy_speed = 30 # this is the speed of our enemies - You can change it to make them faster/slower

while True:
    for enemy in enemies: # go through the enemies one by one
        x = enemy.xcor() # get the current x location of the enemy
        x += enemy_speed # change the x location of the enemy by its speed which is 30
        enemy.setx(x) # move the enemy to its new x location
```

Now if you run this code,you will see that the enemies will keep on moving to the right until they are out of the screen. This is good but we still need to tell the enemy that *if* you hit the one of the white lines, stop, got step close to the player, then move in the opposite direction.

To do so, we will use in _if statement_. This is a statement that only run if the condition we choose is right. Our condition is *if the enemy hits one of the sides*. How do we define such condition in the code?

Easy.

We check that if the current x location (`xcor()`) of the enemy is equal to `300 - enemy_speed`. 
WAIT ... what??
Ok lets take a second here.

Check the code you wrote previously to draw the battle field. Do you see `pen.setposition(-300,300)` ? this 300/-300 is the x location of the two sides of the field. The reason we subtract the speed of the enemy is to make sure it stays in the battle field. Because when the player is at 270, it will still move by 30. Which makes it at 300. THEN we can make at start again from the other side but at a step closer to us. 

> before we right the code. So far we talked about x to move the enemy to the right. But how do we move it towards us? ... You are right, we should decrease the y because we are at a negative y since we are at the end of the screen

Now inside the for loop (which is inside of our infinite loop), write this *if statement*:

```python
enemy_speed = 30 # this is the speed of our enemies - You can change it to make them faster/slower

while True:
    for enemy in enemies: 
        if enemy.xcor() > 270: # check if the enemy hit the white line
          y = enemy.ycor() # get the current y location of the enemy
          y -= 40 # change the y location of the enemy by 40
          enemy.sety(y) # move it closer to us by y which is 40
          enemy.speed(0) # this makes the transition seems instant
          enemy.setx(-270) # move the enemy to the left side again
        x = enemy.xcor() 
        x += enemy_speed 
        enemy.setx(x) 
```

GREAT! Now we have the enemies moving in the right direction. If you run the code and wait, you will see them moving slowly towards the bottom of the battle field. *But* the problem is, they keep on going down until they are out of the screen. So we need to stop them when they hit the bottom white line and make them start again from the top.
_We need another if statement_ *but* for checking the y location this time:

```python
enemy_speed = 30 # this is the speed of our enemies - You can change it to make them faster/slower

while True:
    for enemy in enemies: 
        if enemy.xcor() > 270:
            y = enemy.ycor() 
            y -= 40 
            enemy.sety(y) 
            enemy.speed(0) 
            enemy.setx(-270)

        if enemy.ycor() < -260: # check if the enemy hit the bottom white line
            y = 300  # set y to the new location at the top of the screen
            enemy.speed(0) # this makes the transition seems instant
            enemy.sety(y)  # move the enemy to the new location

        x = enemy.xcor() 
        x += enemy_speed 
        enemy.setx(x) 
```

Yaay 🎆 now our enemies move perfectly!
Feel free to change the values of x, y, and enemy_speed to choose the speed that best fits you for the game.

 > Keep on moving the enemies towards us as long as they are not dead ✔ 

Now we still have some work to do with the enemies since we want to change their position if they get hit by our bullet, but this will have to wait until we make the player fire. So lets move to that now.

There are few things we need to do:
 - First, since all objects in our game are actually turtle objects, we will need to create a bullet turtle and hide it from the screen.

 - Second, we will create a function that runs when we press the firing button (the space bar in this case) which displays the bullet we created, move it to where our player is, then make it move forward. 

 - Third, we will create a score variable, display it on the screen, then if the bullet touches any enemy, we will increase the score by one, then move that enemy to the top left of the battle field to start again. (True, our game only ends if we die `:]` )

to create the bullet, write the following code right before our `moveRight()` function:

```python
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90) #this just makes the triangular turtle head towards the top of the screen
bullet.shapesize(2, 2)
bullet.hideturtle()
bullet_speed = 50
bullet_state = 'ready' #???
```

Most code above looks familiar, right? But why exactly did we add the bullet_state thing?
Since there are more than just one function responsible for the bullet, this helps us know when we can fire and when not. The goal is to fire one bullet every time we hit the space bar. So we will change the bullet_state once we hit the bar and change it again once our bullet reaches the end of the battle field. 
(I understand that this might not make a lot of sense right now. Do not worry about it. You will understand more later when we use it)

Now if you run this code, you will not really see anything new. That is because our bullet is hidden and we did not show it yet. Lets create the function that fires.

Right below our `moveBackward()` function, add this:

```python
def fire_bullet():
    # the global word makes bullet_state accessible from whitin the function. If you remove it, the code breaks
    global bullet_state 
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor() # get the x location of the player
        y = player.ycor() + 10 # get the y location of the player
        bullet.setposition(x, y) # move the bullet to where the player is
        bullet.showturtle() # show the bullet
```

Great. The function is now ready but it does not run.
We need to tell Python to run it when we press space. You know how to do that right?
Add this blow its `wn.onkey` friends.
```python
wn.onkey(fire_bullet, 'space')
```

This is how our game code looks like now:

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

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90) #this just makes the triangular turtle head towards the top of the screen
bullet.shapesize(2, 2)
bullet.hideturtle()
bullet_speed = 50
bullet_state = 'ready' #???

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

def fire_bullet():
    # the global word makes bullet_state accessible from whitin the function. If you remove it, the code breaks
    global bullet_state 
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor() # get the x location of the player
        y = player.ycor() + 10 # get the y location of the player
        bullet.setposition(x, y) # move the bullet to where the player is
        bullet.showturtle() # show the bullet

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
        
        x = enemy.xcor() # get the current x location of the enemy
        x += enemy_speed # change the x location of the enemy by its speed which is 30
        enemy.setx(x) # move the enemy to its new x location

turtle.done() #this just keeps the window open until we close it.
turtle.close() #this just fixes issues related to closing the window
```

Try running the code and pressing the space bar.
What happens? Do you see the yellow bullet? does it move?

If you think we missed something or did something wrong, then thing again 😉 
This  function should not be responsible for moving the bullet. It only fires the bullet. Thats why we have the `bullet_state` variable. When we press the space bar and fire the bullet, we change its state from 'ready' to 'fire'. But moving it should happen in the *infinite loop* (the infinite loop is responsible for moving stuff. Remember moving the enemies?).

What we want to do now is the following:
if the bullet state is fire, move the bullet towards the top. Keep on moving the bullet up until it either hits the top white line or one of the enemies. If so, change its state to 'ready' and hide it again.

So we need two new _if statements_ in the body of the infinite while loop.
one that moves the bullet if the state is ready, and another that changes the state to 'ready' if the bullet hits the top white line (dont worry about hitting the enemies for now. We will create a new function for that).

Change the while loop to this:
```python
while True:
    for enemy in enemies: 
        if enemy.xcor() > 270: 
          y = enemy.ycor() 
          y -= 40 
          enemy.sety(y) 
          enemy.speed(0) 
          enemy.setx(-270) 

        if enemy.ycor() < -260: 
            y = 300  
            enemy.speed(0)
            enemy.sety(y)  

        if bullet_state == 'fire': #chech if the state of the bullet is fire
            y = bullet.ycor() # get the y location of the bullet
            y += bullet_speed # increase the y location of the bullet by its speed
            bullet.sety(y) # move the bullet to the new location

        if bullet.ycor() > 275: # check if the bullet hit the top white line
            bullet.hideturtle() # hide the billet
            bullet_state = 'ready' # change its state to ready to enable the player to fire again
        
        x = enemy.xcor() 
        x += enemy_speed 
        enemy.setx(x) 
```

Yayy 🎆 Now we can actually fire!
Lets now hurt our enemies 😠 
if the bullet hits an enemy, we want to move the enemy back to the top and increase the score.
To know if a collision between the bullet and an enemy happened, we will we will make a function called `isCollision()` and run it in the infinite loop.
Add the function below right above this line: 
`wn = turtle.Screen()`

```python
def isCollosion(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 35:
        return True
    else:
        return False
```

The function above is a bit complex. You are not expected to understand how exactly this work but you might wanna ask your parent about it if you are a math geek 😄
In short, the function creates a circle with certain dimensions. Then it check if the distance between t1 and t2 (when we call the funtion, we can make t1 the bullet and t2 the enemy) is less than 35. If so, it means they are close enough and so they touched.
Also, since this is math stuff, we need to tell Python to bring the math tools (you know calulators and stuff) so at the top of your code add `import math`
(did you notice something? changing 35 to a smaller number makes it more difficult to hit an enemy as you would need to be more accurate - where as making it a bigger number makes killing easier)

Now it is time to run the function inside hte infinite loop.
Somewhere in the body of the for loop which is inside of while loop, write this:
```python
while True:
    for enemy in enemies: # go through the enemies one by one
        if isCollosion(bullet, enemy):
          bullet.hideturtle()
          bullet_state = 'ready' #make the state ready to allow firing again
          enemy.setposition(-300, 300)
```

EVERYTHING IS WORKING REALLY PERFECTLY 🙌 
> Allow the player to fire ✔ 
> Sure enough, emenies die if our bullet hits them ✔ 

You are way closer to becoming a realy game developer!
Only few things left. We need somewhere to show how many enemies we killed, and we need to stop the game if an enemy hits us.
Lets start with the first

At the top of our code, lets make a variable called *score* and make it equal to zero (no enemies killed at the beginning!)
`score = 0`

At the begining of the game, lets create a turtle that writes the score to the screen:

```python
turtle.color("white")
turtle.penup()
turtle.setposition(-300, 250)
turtle.write("Your score is: {}".format(score), move=False, align="left", font=("Arial", 18, "normal"))
turtle.hideturtle()
```

Great. Now we need to increase the score every time a collision happens between a bullet and an enemy. To do so, we will have to clear what we wrote, increase the score, and write the score to the screen again. So lets update the function `isColision()` in the infinite loop to the following:

```python
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
```
Amazing! now we can see how many enemies we have killed so far.
We are almost there!
> Display our score on the screen ✔ 

Our code currently looks like this:

```python
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
```
We are only a step away from getting this game done!
We need to make sure that if any of the enemies touches us, we will stop the game, and print out the final score. Can you guess how we are gonna know if we touched an enemy??
AAh right, we will use the `isCollision()` function!
Lets insert this function inside the for loop in our inifinite loop:


```python
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
```

AND this was our last touch 🙋
lets review the whole code one last time:

```python
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
```

> Keep on moving the enemies towards us as long as they are not dead ✔ 
> Allow the player to fire ✔ 
> We die if an enemy touches us ✔ 
> Display our score on the screen ✔ 
> Sure enough, emenies die if our bullet hits them ✔ 

MISSION ACCOMPLISHED
Now you just run it and enjoy 🎆 🎆 🎆 !!!