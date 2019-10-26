import turtle as tl

tl.shape("turtle")
tl.pencolor("black")

def _prepare_distion(x,y,color):
    tl.penup()
    tl.goto(x,y)
    tl.pendown()
    tl.setheading(0)
    tl.fillcolor(color)
    tl.begin_fill()

def draw_tooth(x, y, color="black"):
    _prepare_distion(x,y,color)
    tl.right(60)
    tl.forward(60)
    for i in range(2):
        tl.left(120)
        tl.forward(30)
        tl.right(120)
        tl.forward(30)
    tl.left(120)
    tl.forward(60)
    tl.left(120)
    tl.forward(abs(2*x))
    tl.end_fill()


def draw_face(x,y, color = "red"):
    _prepare_distion(x,y,color)
    tl.circle(150)
    tl.end_fill()

def draw_eye(x,y, color):
    _prepare_distion(x,y,color)
    for i in range(3):
        tl.forward(60)
        tl.left(120)
    tl.end_fill()

def draw_eyes(x,y,color="black"):
    draw_eye(x,y,color)
    x +=100
    draw_eye(x,y,color)

def draw_head(x,y,color="green"):
    _prepare_distion(x,y,color)
    for i in range(2):
        tl.forward(20)
        tl.right(90)
        tl.forward(40)
        tl.right(90)
    tl.end_fill()


def write_helloI(x,y):
    tl.penup()
    tl.goto(x,y)
    tl.write("Happy,Halloween!!", True,align="center",font=("Arial", 48, "normal"))
    tl.stamp()



if __name__ =="__main__":
    import time

    while True:
        draw_face(0,-150)
        draw_tooth(-60,-20)
        draw_eyes(-80,40)
        draw_head(-10,150+30)
        write_helloI(-10,-260)
        time.sleep(5)
        tl.clear()


