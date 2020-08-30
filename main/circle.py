import turtle


def rect(color):
    c.fillcolor(color)
    c.begin_fill()
    for i in range(2):
        c.forward(200)
        c.left(90)
        c.forward(50)
        c.left(90)
    c.end_fill()

if __name__ == '__main__':
    width = 1
    c = turtle.Turtle()
    c.pencolor('blue')
    c.speed(10)
    c.width(2)
    c.goto(0, 200)
    rect('orange')
    c.goto(0,150)
    rect('white')
    c.forward(100)
    c.circle(25)
    c.left(90)
    c.forward(50)
    for i in range(24):
        c.back(25)
        c.left(15)
        c.forward(25)
    c.left(90)
    c.forward(100)
    c.left(90)
    c.forward(100)
    c.left(90)
    rect('green')
    c.right(90)
    c.forward(200)
    c.left(90)
    c.back(25)
    c.fillcolor('brown')
    c.begin_fill()
    for i in range(2):
        for j in range(3):
            c.forward(40 / width)
            c.right(90)
            c.forward(20 * width)
            c.left(90)
        if i == 1:
            c.end_fill()
            break
        c.back(200)
        c.left(90)
        width = 2
    c.end_fill()


turtle.done()
