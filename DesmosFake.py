import turtle
import math

def sqrt(j):
    return math.sqrt(j)

def sin(j):
    return math.sin(j)

def cos(j):
    return math.cos(j)

def tan(j):
    return math.tan(j)

def arcsin(j):
    return math.asin(j)

def arccos(j):
    return math.acos(j)

def arctan(j):
    return math.atan(j)

def log(a, b):
    return math.log(a, b)

def ln(a):
    return math.log(a)

exp = input("What is your function? ")
expression = exp.replace(")(", ")*(").replace("^", "**")

#Window
wn=turtle.Screen()
wn.title("Desmos 2.0")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Axises
x_axis = turtle.Turtle()
x_axis.speed(0)
x_axis.shape("square")
x_axis.color("white")
x_axis.goto(0, 0)
x_axis.shapesize(stretch_wid = 0.1, stretch_len = 40)

y_axis = turtle.Turtle()
y_axis.speed(0)
y_axis.shape("square")
y_axis.color("white")
y_axis.goto(0, 0)
y_axis.shapesize(stretch_wid = 30, stretch_len = 0.1)

#Letters
x_let = turtle.Turtle()
x_let.speed(0)
x_let.color("red")
x_let.penup()
x_let.hideturtle()
x_let.goto(380, 10)
x_let.write("x", align = "center", font = ("Comic Sans MS", 10, "normal"))

y_let = turtle.Turtle()
y_let.speed(0)
y_let.color("red")
y_let.penup()
y_let.hideturtle()
y_let.goto(20, 275)
y_let.write("y", align = "center", font = ("Comic Sans MS", 10, "normal"))

#X-Discrete
for i in range(-9, 10):
    ment = turtle.Turtle()
    ment.speed(0)
    ment.shape("square")
    ment.color("white")
    ment.goto(40*i, 0)
    ment.shapesize(stretch_wid = 1, stretch_len = 0.1)

#Y-Discrete
for i in range(-7, 8):
    incre = turtle.Turtle()
    incre.speed(0)
    incre.shape("square")
    incre.color("white")
    incre.goto(0, 40*i)
    incre.shapesize(stretch_wid = 0.1, stretch_len = 1)

#Number
xy0 = turtle.Turtle()
xy0.speed(0)
xy0.color("orange")
xy0.penup()
xy0.hideturtle()
xy0.goto(-15, -25)
xy0.write("0", align = "center", font = ("Comic Sans MS", 10, "normal"))

#Graph
for i in range(-800, 800):
    try:
        try:
            x = i / 40
            y = eval(expression)
            plot = turtle.Turtle()
            plot.speed(0)
            plot.shape("square")
            plot.color("cyan")
            plot.up()
            plot.goto(i, 40*y)
            plot.down()
            plot.shapesize(stretch_wid = 0.05, stretch_len = 0.05)
        
        except ZeroDivisionError:
            continue
    except ValueError:
        continue

#Main Graph Loop
while True:
    wn.update()