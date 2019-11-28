# Teach Your Kids How To Build Their Own Game with Python - Part 2

So, without further due, lets pickup from where we left last time.
The last piece of code we wrote allowed us to create and move the main player (we still need to make sure it fires :fire:).
The code so far looks like this:

```python
# 🐢🐢🐢
import turtle
pen = turtle.Turtle()

pen.pendown() #this line puts the pen on the paper
for side in range(3): #see number three? its what reminds Python,  THREE times!
  pen.forward(100)
  pen.right(90)
pen.forward(100)

player = turtle.Turtle()
player.penup()

def moveRight():
    x = player.xcor()
    x += 10
    player.setx(x)

def moveLeft():
    x = player.xcor()
    x -= 10
    player.setx(x)  

def moveForward():unicorn
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
```

## Sizes, dimensions, and cleaning
checked
As of now, if you run the code, it will draw a small box in the middle of the screen with small arrow (the player) that you can move.
So couple of things to do here:

 - [ ] draw a bigger box
 - [ ] hide the turtle that drew that box
 - [ ] make the player bigger

so lets start by making our box bigger. You remember how we drew that? all we did was to make the :turtle: move in four directions. Great! so now we know that all we need to do is to position the turtle in the right place before we make it move (and maybe make it walk a bit longer?). the way we position any turtle we create with Python is by using this function `.setposition(x, y)` (_intuitive right?_).
To understand what does x and y actually mean, lets try to implement them first and then see. Right after creating the pen (`pen = turtle.Turtle()`), and before putting the pen down (`pen.pendown()`) we will write this:pen.hideturtle()

```pythyon
border_pen.penup()
border_pen.setposition(-300,300)
```

Try running it, what heppens?
Yess the small box moved to the left top corner! but why there?
Try changing the values of either the first or the second number in the function, run it again, and see what happens.

`.setposition(x, y)pen.hideturtle()` takes two ar> guments. `x` is how far right or left (zero is the center), and `y` is how far up or down (again, zero is the center).

Great, so now we are starting from the left top corner and we have a loop that we already wrote which draws a box. All we need to do is make the sides of that box longer.

```python
for side in range(3): 
  pen.forward(600)
  pen.right(90)
pen.forward(600)
```

Now run the code and check the dimension of the box (Sure feel free to change it the way you like. is is YOUR game :unicorn:)

 > draw a bigger box ✔ 

You still see that annoying arrow at the top left side of the box? Lets hide it before we forget about it.
After the pen has done the job (beneath the loop), lets add this line

```python
pen.hideturtle()
```

Yaay its gone :fireworks:
> draw a bigger box ✔
hide the turtle that drew that box ✔

Now we get to us, the player!
_Currently_ we are a tiny arrow in the middle of a huge box heading east.
_we need to be_ a bigger armory ship heading north :rocket: 
Lets do some changes. First go to this image [here](https://github.com/MustafaAnasKH99/Space-Invaders---Python/blob/master/space_invaders/ship.gif), download it, and save it right next to your python file.

There are three steps for giving a shape to our turtle:
 - Save the picture
 - Make turtle register the picture in its memory
 - tell turtle to give the registered picture to the player

Since you just saved the picture, the first step is done. Now the second step.
Turtle needs to know everything it is dealing with. So it has a command to register new shapes (JUST LIKE OUR PICTURE!)
to reigster our picture as a shape, lets add this line of code before we start drawing the box:

```python 
turtle.register_shape("ship.gif")
``` 
**Notice**, `ship.gif` is the name of the file you just saved. so if you want to download your own ship from the internet, make sure you either change its name or change the code to its name.

Last thing to do is to tell turtle `heyy, this shape is for player`.

below `player = turtle.Turtle()` add:
```python
player.shape('sh or change the code to its name.
```

Last thing to do is to tell turtle `heyy, this shape is for player`.

below `player = turtle.Turtle()` add:
```python
player.shape('ship.gif')
```
__RUN AND SEE HOW GREAT IT FEELS TO RIDE A SPACE SHIP :rocket: :rocket:__

Now that we are in the field, lets start calling enemies in.
Lets give it a thought first. An enemy is basically a new turtle object on the screen. So say we want to have 5 enemies, we create 5 turtle objects and give them a position (sure, later on they'll do more than just standing there!). Since we already know loops, I will introduce lists so we make our development process easier.

## Lists and appending enemies

a list is basically a container. You can think of it as a pencil case for your pencils and pens. a closet for your clothes, or a container for your turtles :smile:

Lets use a loop (like the one we used to create the arena box) to make a list that has 10 of our enemies (again, an enemy is a turtle).

```python
enemies = []
for i in range(10):
    enemies.append(turtle.Turtle())
```

Sure enough, changing the number in the range will change the number of our enemies.
Now we have our enemies stored but not displayed on the screen. Lets create another loop to go over all the enemies in the list and put them somewhere on the screen. Wait, **somewhere** on the screen? this means that we dont even know exactly where!
Yess that is right. We will ask python to pick a random number between a range that we choose. And remember the X and Y system? we will have to tell Python to give each turtle a random `y` and a random `x` value. Thankfully Python has something ready that helps us choose random numbers every time we run the code. It is a package called `random`and a particular function in that package is called `randint`

lets import the package in a new line after importing turtle.

```python
from random import randint
```
Now lets use it. Below the loop that created the enemies in the list, we will write this loop:

```python
for enemy in enemies:
    x = randint(-300, 300)
    y = randint(0, 300)
    enemy.setposition(x, y)
```

what is happening here is basically letting Python choose a random number for x (a number between -300 and 300), and a random number for y (a number between 0 and 300), then giving telling the enemy to go to this random position. The reason x is between -300 and 300 is so that it fits in the box we created, where we want all the game to happen. But why y is only between 0 and 300? well thats because we do not want it to be very close to where we are,since the idea is to have them run towards us to attack (Yess we will do that too :fire:).
Now if you run the code, the result will look like this:

![game image](https://thepracticaldev.s3.amazonaws.com/i/os7ug14fnguu2oy70lls.png)

It turned out that Python first puts the enemy in the middle of the screen then sends it wherever you tell it to. Which results in these lines as if you remember, we previously said that turtles are like pens on papers. To move, we need to take the pen away from the paper before moving it. So lets add this line too.

```python
for enemy in enemies:
    x = randint(-300, 300)
    y = randint(0, 300)
    enemy.penup()
    enemy.setposition(x, y)
```
woww it is starting to look scary :alien:
Lets make it worse by giving those enemies some proper shape.
First go [here](https://github.com/MustafaAnasKH99/Space-Invaders---Python/blob/master/space_invaders/invador.gif), download the invadors picture, and save it next to the other image/python file. Then lets go ahead and register the picture and assign it to the enemies.

```python
turtle.register_shape("ship.gif")
turtle.register_shape("invador.gif")
```


```python
for enemy in enemies:
    x = randint(-300, 300)
    y = randint(0, 300)
    enemy.penup()
    enemy.setposition(x, y)
    enemy.shape('invador.gif')
```
Looks good?
One last thing since we are dealing with pictures already, lets add a background picture to the whole game. Go [here](https://github.com/MustafaAnasKH99/Space-Invaders---Python/blob/master/space_invaders/bg.gif) and download it.

```python
turtle.register_shape("bg.gif")
```
then lets go below to the screen variable we created last time and assign it a background picture.
```python
wn = turtle.Screen()
wn.bgpic("bg.gif")
```

THIS REALLY LOOKS GOOD :fire: :fire:
Next lesson, the way shall begin! 👽
