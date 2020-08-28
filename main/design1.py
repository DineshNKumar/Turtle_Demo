import random
import turtle
import math

if __name__ == '__main__':

    d = turtle.Turtle()

    d.speed(10)

    for i in range(300):
        d.forward(40)
        d.left(math.sin(i) * 25)
        d.left(50)

    turtle.done()
