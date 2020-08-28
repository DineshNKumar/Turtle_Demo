import turtle

if __name__ == '__main__':
    star = turtle.Turtle()

    star.color('blue', 'yellow')
    star.speed(10)
    star.begin_fill()
    for i in range(30):
        star.forward(200)
        star.left(165)
    star.end_fill()

    turtle.done()
