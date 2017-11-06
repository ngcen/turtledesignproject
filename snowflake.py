import turtle
import random
 
wn = turtle.Screen()
wn.bgcolor("#4984D1")
 
snow = turtle.Turtle()
snow.speed(15)
snow.width(3)
sfcolor = ["green", "blue", "white", "#FA650E", "magenta"]
 
def snowflake(size):
 
    snow.penup()
    snow.forward(10*size)
    snow.left(45)

    snow.pendown()
    snow.color(random.choice(sfcolor))
 
    for i in range(8):
        branch(size)   
        snow.left(45)
     
 
def branch(size):
    for i in range(3):
        for i in range(3):
            snow.forward(10.0*size/4)
            snow.backward(10.0*size/4)
            snow.right(45)
    snow.left(90)
    snow.backward(10.0*size/3)
    snow.left(45)
    snow.right(90) 
    snow.forward(10.0*size)
 
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    snow.penup()
    snow.goto(x, y)
    snow.pendown()
    snowflake(sf_size)
 
wn.exitonclick()  
