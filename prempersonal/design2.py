import turtle

turtle.speed(1000)
turtle.bgcolor('black')
for i in range(30):
    for colors in ('red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white'):
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(4)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
