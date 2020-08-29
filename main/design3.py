import turtle
import math


def square(des, size):
    for j in range(50):
        des.forward(100)
        des.left(size)
        size += 1


if __name__ == '__main__':
    des = turtle.Turtle()

    square(des, 100)

    turtle.done()
