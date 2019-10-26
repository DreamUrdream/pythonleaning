# Comments like these help explain the program.

# Make a turtle named 'tina' 
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

# This teaches our program how to make triangles of a color
# and x,y coordinates we choose
def make_triangle(x, y, color):
  tina.penup()
  tina.goto(x,y)
  tina.begin_fill()
  tina.color(color)
  tina.pendown()
  for count in range(3):
    tina.forward(50)
    tina.left(120)
  tina.end_fill()

# This teaches our program how to make triangles of a color 
# and x,y squares we choose
def make_square(x, y, color):
  tina.penup()
  tina.goto(x,y)
  tina.begin_fill()
  tina.color(color)
  tina.pendown()
  for count2 in range(3):
    tina.forward(50)
    tina.left(90)
  tina.end_fill()

# The Pumpkin:
tina.penup()
tina.goto(0,-150)
tina.color('#ff6600')
tina.begin_fill()
tina.circle(150)
tina.end_fill()
tina.left(180)

# The Teeth:
make_triangle(-35, -20, '#ffffff')
make_triangle(0, -20, '#ffffff')
make_triangle(35, -20, '#ffffff')
tina.left(180)

# The Eyes:
make_triangle(-70, 50, '#ffffff')
make_triangle(0, 50, '#ffffff')

# The Stump:
make_square(-20, 125, '#663300')

# Happy Halloween!
tina.penup()
tina.goto(-100,-185)
tina.write('Happy Halloween!', None, None, "24pt normal")
tina.goto(-120,-185)
tina.left(180)