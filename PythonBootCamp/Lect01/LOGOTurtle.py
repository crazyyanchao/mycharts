"""
Need install package: sudo apt-get install python-tk

"""
import turtle

painter =   turtle.Turtle();
painter.pencolor("red")

for i in range(30):
    painter.forward(100)
    painter.left(118)

painter.pencolor("blue")
for i in range(30):
    painter.forward(100)
    painter.left(118)

turtle.done()