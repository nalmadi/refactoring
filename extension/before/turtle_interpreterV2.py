'''
John Connors 
Lab 8 
Creates the turtle interpreter class
so that we can speak turtle and draw L systems. 
4/11/19 
Version 2
'''

import turtle
import random
import sys

#Creates the turtle interpreter class
class TurtleInterpreter: 
    def __init__(self, dx = 800, dy = 800): 
        turtle.setup(dx, dy)
        turtle.tracer(False)

    def drawString(self, dstring, distance, angle): 
        """     
        Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list of 
        turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        T : Draws some berries as red circles. 
        [: save position and heading 
        ]: return to position and heading
        L : Draws some leaves 
        < : saves the color of the turtle
        >: returns the color
        g: sets the turtle to green 
        y: sets the turtle to yellow 
        r: sets the turtle to red 
        b: sets the turtle to blue
        C: Draws some cocnuts 
        ?: Draws a square
        !: Draws a triangle 
        """
        stack = []
        colorstack = []

        for c in dstring:
            if c == 'F':
                turtle.forward(distance)
            elif c == '-':
                turtle.right(angle)
            elif c == '+':
                turtle.left(angle)
            elif c == 'T':
                turtle.color('red')
                turtle.begin_fill()
                turtle.circle(2)
                turtle.color('black')
                turtle.end_fill()
            elif c == '[':
                stack.append(turtle.position())
                stack.append(turtle.heading())
            elif c == ']':
                turtle.penup()
                x = stack.pop()
                y = stack.pop()
                turtle.goto(y)
                turtle.setheading(x)
                turtle.pendown()
            elif c == 'L':
                turtle.circle(3)
            elif c == '<':
                colorstack.append(turtle.color()[0])
            elif c == '>': 
                k = colorstack.pop()
                turtle.color(k)
            elif c == 'g': 
                turtle.color('green')
            elif c == 'y': 
                turtle.color(0.8,0.8,0.3)
            elif c == 'r':
                turtle.color('red')
            elif c == 'C': 
                turtle.circle(10)
            elif c == 'b':
                turtle.color('blue')
            elif c == '?': 
                turtle.forward(distance)
                turtle.right(90)
                turtle.forward(distance)
                turtle.right(90)
                turtle.forward(distance)
                turtle.right(90)
                turtle.forward(distance)
            elif c == '!': 
                turtle.forward(distance)
                turtle.right(240)
                turtle.forward(distance)
                turtle.right(240)
                turtle.forward(distance)





    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()
        turtle.update()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a click
        turtle.exitonclick()
	

    #Places the turtle and sets the angle heading 
    def place(self, xpos, ypos, angle=None):
        turtle.penup()
        turtle.goto(xpos, ypos)
        if angle != None: 
            turtle.setheading(angle)
        turtle.pendown()
        
    #Sets the turtle's angle heading 
    def orient(self, angle):
        turtle.setheading(angle)

    #Tells the turtle to go somewhere 
    def goto(self, xpos, ypos):
        turtle.penup()
        turtle.goto(xpos, ypos)
        turtle.pendown()
    
    #Sets the color of the turtle 
    def color(self, c): 
        turtle.color(c)

    #Sets the pen width of the turtle
    def width(self, w): 
        turtle.width(w)
    
