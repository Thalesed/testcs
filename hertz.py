import turtle

dies = turtle.Screen()
dies.title('Hertz')

illa = turtle.Turtle()
illa.hideturtle()

illa.speed(1000)
illa.penup()
illa.goto(0, 0)
illa.pendown()

turtle.colormode(255)
def hertz(scale, color):
    illa.fillcolor(color[0], color[1], color[2])
    illa.begin_fill()

    illa.left(40)
    illa.fd(2 * scale)
    illa.circle(1 * scale, 180)

    illa.rt(80)
    illa.circle(1 * scale, 180)
    illa.fd(2 * scale)
    illa.end_fill()

farbe = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 127, 255), (0, 0, 255), (139, 0, 255)]

for i in range(1, 1024):
    hertz(i, farbe[i % 7])
turtle.done()




