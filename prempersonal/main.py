import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(100)
n=36
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(360)
        t.left(144)
turtle.done()

