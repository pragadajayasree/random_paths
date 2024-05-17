import turtle
from turtle import Turtle,Screen
import random
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r,g,b)
    return random_colors
t = Turtle()
turtle.colormode(255)
t.shape("circle")
t.pensize(10)
t.speed(0)
colors=["red","blue","pink","orange","violet","green"]
direction =[0, 90, 180, 270]
for i in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()


