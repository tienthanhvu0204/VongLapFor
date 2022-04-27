import turtle
from math import cos as cos
from math import pi as pi
screen = turtle.Screen ()
screen.setup (1000, 1000)
screen.bgcolor = ("black")
t = turtle.Turtle ()
t.speed (10)

# vẽ vòng tròn
t.penup ()
t.goto (0, -100)
t.pendown ()
t.circle (100)
print (pi)

# vẽ ngôi sao
#t.lt (72)
t.pendown ()

# for i in range (5):
#     t.fd (2 * cos (pi / 10) * 200)
#     t.lt (144)
# t.rt (72)
# t.circle (200, 5)
for j in range (0, 360, 5):
    for i in range (5):
        t.fd (cos (pi / 10) * 200)
        t.lt (144)
    #t.rt (72)
    t.circle (100, 5)
    #t.lt (72)
t.hideturtle ()
turtle.done ()

