import turtle


def star(des, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            des.forward(size)
            star(des, size/3)
            des.left(216)


if __name__ == '__main__':
    des = turtle.Turtle()

    des.getscreen().bgcolor('#444677')

    des.speed(20)

    star(des, 360)


    turtle.done()

