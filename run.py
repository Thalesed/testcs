import turtle

def left():
    trt.left(10)
def right():
    trt.rt(10)

def back():
    trt.fd(-10)
def move():
    trt.fd(10)

def space():
    trt.penup()
def dspace():
    trt.pendown()



me = turtle.Screen()

trt = turtle.Turtle()
trt.shape('turtle')

me.onkeypress(left, "Left")          
me.onkeypress(move, "Up")     
me.onkeypress(right, "Right")     
me.onkeypress(back, "Down")     
me.onkeypress(space, "space")     
me.onkeyrelease(dspace, "space")

me.listen()

turtle.done()
