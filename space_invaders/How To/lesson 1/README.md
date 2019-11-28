# Teach Your Kids How To Build Their Own Game with Python - Part 1 

I used to be a coding trainer few months ago. Our students were former street kids coming from under-privileged societies. You can imagine the lack of education they had. As a teacher there, I had to make my lessons fun and easy for them to grasp, so I would often use games to do so. I was going through my old files and I found this lesson plan I wrote to teach the kids how to build the famous game `Space Invaders`. At the beginning it seemed an impossible mission, but they actually loved it and got to love coding because of it!
Anywho, with no further details, I am going to share this lesson in three posts here. today is the first, hoping that any beginner or parent would find it helpful.

> to follow up with this tutorial, you will need to have Python installed, and a text editor. _OR_, you could use this [online text editor](https://repl.it/) and create a project that uses turtle too (we'll talk more about this in a bit).

## Using Turtle for Graphics
Python itself is just a programming language. It can go deep enough in ordering the computer what to do, but it does no graphics on its own! (_think of it as Javascript, it still needs HTML to display anything_).
For that reason, we will use a Python GUI (_Graphical User Interface_) Library called Turtle. A turtle is a pen that you put on the screen and move it however you want to end up having something drawn on the screen.

to order python to bring the pen which we will use to draw, we can type this line:
```python
Pen = turtle.Turtle()
```
however, as we said, turtle is something that is not part of who Python is, so we will need to tell it to bring it from somewhere outside (do now worry, it knows where to find outside stuff).
So we will always include this line at the top of our file:
```python
import turtle
Pen = turtle.Turtle()

```
GREAT! now that we have the pen, we need to start drawing!
Image your hand is holding the pen and not Python. for example, to draw a straight line to the right, you just move the pen to the right by sticking your hand to the paper and moving it to the right!
So we know we need to tell Python to do two things:
 - Put the pen on the paper (screen in Python's case!)
 - move the pen x amount of distance to the direction we want!
So let do that:
```python
import turtle
pen = turtle.Turtle()

pen.pendown() #this line puts the pen on the paper
pen.forward(100) #now move the pen forward 100 steps!
```
Now if you run your code, you will see a little arrow moving on the screen!
There are few things we should memorize now about how to move the pen. Because we not only have forward, but other things too!
 - pen.forward()
 - pen.backward()
 - pen.left()
 - pen.right()
 - pen.penup()

Now I want you to try each on your own before we continue.
...
...
They seem intuitive right? `.backward()` moves the pen backwards. Except that left and right do not actually move the pen but rotate it a certain degree.
Now try copying the code below and pasting it in your text editor. What do you see?

```python
import turtle
pen = turtle.Turtle()

pen.pendown() #this line puts the pen on the paper
pen.forward(100) #now move the pen forward 100 steps!
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
```

that is right! 
we moved our pen in the right way to draw a square, great. Now lets increase the values in the brackets following `forward` because we want a bigger square! (_this is where our game will be happening_).

.
.
.

But hey wait a second, did you notice that in our code there is two lines that we repeated THREE TIMES! don't you think it is ugly to do so?
I mean there should be a way to tell Python to read something again and again without having to write it many times!

YES you guessed right!
we can actually only write those two lines one time, and tell Python to read them three times! this is how we do it:
```python
import turtle
pen = turtle.Turtle()

pen.pendown() #this line puts the pen on the paper
for side in range(3): #see number three? its what reminds Python,  THREE times!
  pen.forward(100)
  pen.right(90)
pen.forward(100)
```

This is called a _`for loop`_. It allows you to do ONE thing  MANY times without re-writing the same thing!

Great, now we have a big square, and we want our game to be inside it!
> wait! did you know that you can change the color of your pen? just by typing `.color('name_of_color')`. Try it! _ie: try `pen.color('red')`_
Before continuing.

Before continuing, lets make sure we know what we want exactly in our game:

 - Our character that moves and shoots enemies!
 - Enemies characters that move towards us :alien:
 - We get destroyed if an enemy touches us 
 - An enemy dies if our bullet touches it! :rocket:

Great! Now we can finish these one by one! First, lets create US. we are just a pen that moves inside the square. But wait wont we be drawing if we do so?. You are right, but remember when we said we can tell Python to put the pen away from the paper? what happens is, the pen still shows on the screen, but it does not leave trace behind it when it moves. So lets do that!

we create a new pen called `player` (_we_), and put it away from the paper.

```python
import turtle
pen = turtle.Turtle()

pen.pendown() #this line puts the pen on the paper
for side in range(3): #see number three? its what reminds Python,  THREE times!
  pen.forward(100)
  pen.right(90)
pen.forward(100)

player = turtle.Turtle()
player.penup()
```

now if we try to move the player (`player.forward(100)`) it will move leaving nothing behind it. Anyways, we dont want to write the value every time we move it! Instead, we will tell Python to move it only one step every time we press a key!

Lets first tell Python to listen carefully, because when I press the letter `D` on my keyboard, I want the player to move one step ahead!

```python
wn = turtle.Screen() #initiate the window
wn.listen()
wn.onkey(myFunction, `d`) #this waits until you press <kbd>D</kbd>
```

but wait what is `myFunction`??
That is an important question.
In Python, a function is a set of orders we give to the computers. What is an order? EVERY line of code written in Python or any other language is an order! so we could write a function that just says hello! or collect the lines of code we just wrote and draw a square! One special thing about functions, is that they do not happen until we call them!
Just like how your mom calls dad to ask him to get some stuff for home? you call a function to do something. so here, we need to tell `myFunction` to move our player only one step to the right! So each time we press `d`, our player moves a step ahead.
This is how we make this function:

```python
def moveRight():
 x = player.xcor()
 x += 10
 player.setx(x)
```

Lets take a while here to explain this code;
the `def` word is just Python's way of knowing that what's after it is the name of the function (yes because you can name your function whatever you want :smile:). Now we know that `moveRight()` is the name of the function. Now the two dots after the function just indicate that here is where the function starts. If we write them, then we press <kbd>Enter</kbd>, we will notice that the editor will immediately make us start the next line with a bit of space empty. 
Why? _this is how Python know that this line is part of this function_

Great, Now lets see what is part of this function.

`x = player.xcor()` this sentence has some weird math behind it.
(if you happen to know what the Orthonormal system, you will know what this is). But all you really need to know is that this x now has the current position of our `player` (_notice that the code says `player.xcor()`_).
Now we said we wanted to move a step to the right. so we need to increate x by a step!
this is what this line does `x += 10`. You can try a number other than 10 and see how fast/slow your movement is.
Now after increaing the value of x (where our player _used_ to be), we need to assign x again to our player. and this is what the last line does: `player.setx(x)`

Try running the code and moving the player.
Now you should be able to move to the right :fireworks: after pressing <kbd>D</kbd>.

Easy right?
Now lets use the same logic to make to the left. 
HOLD ONE :bell:
notice, when we moved to the right, we increased x, but when we move to the opposite direction, what should we do??

```python
def moveLeft():
 x = player.xcor()
 x -= 10
 player.setx(x)
```

But to run this function, we need to ask Python to run it when we press the letter <kbd>A</kbd> on the keyboard! So lets make Python listen to the letter <kbd>A</kbd> again.

```python
wn.onkey(moveLeft, 'a')
```
Great!
the only thing missing now is moving forward and backward!
To do so we can use the same logic BUT, math plays around a bit here.
When we were moving right and left, we were using `xcor()`. But now we will be moving forward and backward, that's why we will use `ycor()` instead.

```python
wn.onkey(moveForward, 'w')
wn.onkey(moveBackward, 's')

def moveForward():
 y = player.ycor()
 y += 10
 player.sety(y)

def moveBackward():
 y = player.ycor()
 y -= 10
 player.sety(y)
```

now run your code and move around!!!
YAYY!! :fireworks::fireworks::fireworks:
We are free to move now!
this is how our final code looks like:

```python
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

turtle.done() #this just keeps the window open until we close it
```

You have come a long way!
Next tutorial, we will get our enemies in the game, then start the fight!

> I am on a lifetime mission to support and contribute to the general knowledge of the developers community as much as possible. Some of my writings might sound too silly, or too difficult, but no knowledge is ever useless. I urge you to do the same and try to pay back your community your own way :smile: :heart: