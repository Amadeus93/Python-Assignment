from graphics import *
import random

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
for line in datafile: print(line)

window = GraphWin("Visualisation", 500, 500)

    
while True:
    
    posX = random.randint(0,500)
    posY = random.randint(0,500)

    #ball = Circle(Point(posY,posX), 100)
   # ball.setFill(color_rgb(255,55,120))
    #ball.draw(window)

    p = Polygon(Point(posY,posX), Point(450,450))
    p.setFill("red")
    p.setOutline("blue")
    p.setWidth(2)
    p.draw(window)
    
    p = Polygon(Point(450,450), Point(posX,posY))
    p.setFill("red")
    p.setOutline("green")
    p.setWidth(2)
    p.draw(window)

    p = Polygon(Point(-450,-450), Point(posX,posY))
    p.setFill("red")
    p.setOutline("red")
    p.setWidth(2)
    p.draw(window)

    for line in datafile:

        line = Line(Point(200,200),Point(250,280))
        line.setWidth(4)
        line.draw(window)