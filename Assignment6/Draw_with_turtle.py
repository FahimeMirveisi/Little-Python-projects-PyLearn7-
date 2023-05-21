import turtle
import time

turtle.title("Welcome to my program... You can see the art that turtle draw here")

p = turtle.Pen()

# My turtle shape
p.shape("turtle")
p.shapesize(1.5, 1.5, 1.5)
p.fillcolor("green")

side = 3

while True:
    degree = ((side - 2) * 180) / side
    p.left(180 - degree / 2)

    for i in range(side):
        p.forward(70 * (1 + side / 10))
        p.left(180 - degree)

    p.right(180 - degree / 2)
    p.penup()
    p.forward(12 * (1 + side / 10))
    p.pendown()

    side = side + 1


turtle.done()
#time.sleep(10)

