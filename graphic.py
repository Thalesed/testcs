import turtle

SCALE = 10
XSIZE = 250
YSIZE = 370

class Graphic(turtle.Turtle):
    def __init__(self, name="Graphic", size=(500, 500)):
        dies = turtle.Screen()
        dies.title(name)
        turtle.setup(width=size[0], height=size[1])
        super().__init__()
        super().hideturtle()
        super().speed(1000)
        self.__createX()
        self.__createY()

    def __createX(self):
        for i in range(-XSIZE, XSIZE + 1, SCALE):
            super().penup()
            if(i == 0):
                super().pensize(2)
            super().goto(-YSIZE, i)
            super().pendown()
            super().goto(YSIZE, i)
            super().pensize(1)

    def __createY(self):
        for i in range(-YSIZE, YSIZE + 1, SCALE):
            if(i == 0):
                super().pensize(2)
            super().penup()
            super().goto(i, -XSIZE)
            super().pendown()
            super().goto(i, XSIZE)
            super().pensize(1)

    def __graphic(self, x, y):
        super().goto(x * SCALE, y * SCALE)
        
    def start(self, f, color="red"):
        super().pensize(3)
        super().penup()
        super().color(color)
        for i in range(-YSIZE, YSIZE):
            x, y = i/10, f(i/10)
            if y != None:
                self.__graphic(x, y)
                super().pendown()
            else:
                super().penup()
    def done(self):
        turtle.done()
