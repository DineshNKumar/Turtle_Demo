import turtle
import math

if __name__ == '__main__':
    des = turtle.Turtle()

    des.speed(20)

    for i in range(2000):
        des.forward(math.sqrt(i))
        des.left(i % 180)

    turtle.done()
