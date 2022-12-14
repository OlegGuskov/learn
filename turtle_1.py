

import turtle

joe = turtle.Turtle()
joe.speed(2)
color = ['red', 'orange', 'green', 'blue']


def move(L, H, a=90):
    joe.forward(L)
    joe.left(a)
    joe.forward(H)
    joe.left(a)


def draw_figure(count=4):
    for k in range(count):
        joe.color(color[k])
        joe.begin_fill
        for i in range(2):
            move(
                200,
                100,
            )
        joe.goto(-110 * (k + 1), -110 * (k + 1))
        joe.end_fill


draw_figure()
