'''
John Connors 
Project 8 
This code produces an image of a tree
growing. To run this code type py growth.py the names of the
2 L systems you want to use, the side length and the angle
into the For the first and second arguments use 
systemML and systemLL in that order. Please use a length of 10 
and an angle of 90 degrees. For the extension use the systemExt1 and 
systemExt2 with the lenght of 10 and the angle of 60. To draw a the triangle the square
use the systemTriangle and systemSqu.  
4/16/19 
'''

import sys
import lsystem1 
import turtle_interpreterV2 as terp

def main(argv): 
    ''' Draws baby fractal trees growing up into adult trees.'''
    if len(argv) < 4: #Checks to see if the correct amount of arguments are entered.
        print("MALFUNCTION!!!!! NEED 2 <lsystem files> <distance> <angle> PLEASE")
        exit()

    #Calls the Lsystem class as the first and second argument
    tree = lsystem1.Lsystem(argv[1])
    tree2 = lsystem1.Lsystem(argv[2])
    distance = float(argv[3])
    angle = float(argv[4])


    #Defines the size of the window 
    ndx = 800
    ndy = 600

    #Calls the turtleInterpreter class 
    turtles = terp.TurtleInterpreter(ndx, ndy)

    #Calls the buildString method from the lsystem class with a certain amount of iterations 
    qstr = tree.buildString(3)
    qstr1 = tree.buildString(4)
    qstr2 = tree.buildString(5)

    mstr = tree2.buildString(1)
    mstr1 = tree2.buildString(3)
    mstr2 = tree2.buildString(4)
    
    #Defines x and y as the coordinates and z as the angle. 
    x = -100
    y = -400
    z = 90

    #Draws the trees and fractals 
    turtles.width(2)
    turtles.color((0.5, 0.4, 0.3))
    turtles.place(x-150, y, z)
    turtles.drawString(qstr, distance, angle)
    turtles.place(x, y, z)
    turtles.drawString(qstr1, distance, angle)
    turtles.place(x + 150, y, z)
    turtles.drawString(qstr2, distance, angle)
    turtles.place(x-650, y+500, z)
    turtles.drawString(mstr, distance, angle)
    turtles.place(x, y+500, z)
    turtles.drawString(mstr1, distance, angle)
    turtles.place(x+650, y+600, z)
    turtles.drawString(mstr2, distance, angle)

    #Keeps the window open until the user clicks or presses q. 
    turtles.hold()

#This is where the main code is run from
if __name__ == "__main__":
    main(sys.argv)

