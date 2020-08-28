import turtle

if __name__ == '__main__':
    obj = turtle.Turtle()

    obj.color('black', 'cyan')

    obj.begin_fill()

    obj.forward(100)
    obj.left(90)
    obj.forward(100)
    obj.left(90)
    obj.forward(100)
    obj.left(90)
    obj.forward(100)

    obj.penup()
    obj.forward(100)
    obj.pendown()

    obj.forward(100)
    obj.left(90)
    obj.forward(100)
    obj.left(90)
    obj.forward(100)
    obj.left(90)
    obj.forward(100)

    obj.end_fill()



    turtle.done()
