import turtle


def square(des, size):
    if size <= 10:
        return
    else:
        for i in range(1,5):
            des.forward(20)
            des.left(90)


if __name__ == '__main__':

    des = turtle.Turtle()

    des.speed(20)
    square(des, 100)

    turtle.done()
