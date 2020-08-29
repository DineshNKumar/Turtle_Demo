import turtle


def make(flag):
    width = 1
    flag.color('black', 'brown')
    flag.begin_fill()
    for i in range(2):
        for j in range(3):
            flag.forward(30 / width)
            flag.right(90)
            flag.forward(15 * width)
            flag.left(90)
        if i == 1:
            flag.end_fill()
            draw_upper(flag)
            break
        flag.back(150)
        flag.left(90)
        width = 2


def draw_upper(flag):
    flag.left(90)
    flag.forward(15)
    flag.right(90)
    flag.forward(240)
    flag.left(90)
    flag.color('orange','orange')
    flag.begin_fill()
    main_flag(flag, 60)
    flag.end_fill()
    flag.color('black')
    flag.back(20)
    flag.left(90)
    flag.color('green', 'green')
    flag.begin_fill()
    main_flag(flag, 60)
    flag.end_fill()


def main_flag(flag, size):
    for i in range(2):
        for j in range(1):
            flag.forward(size)
            flag.left(90)
        if i != 1:
            flag.forward(20)
            flag.left(90)


if __name__ == '__main__':
    flag = turtle.Turtle()

    make(flag)

    turtle.done()
