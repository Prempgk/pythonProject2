import turtle
import colorsys

t = turtle.Turtle()
x = turtle.Screen()
x.bgcolor('black')
t.speed(0)
n = 50
h = 0
for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h+=1/n
    t.color(c)
    t.width(2)
    t.forward(i*2)
    t.left(145)


