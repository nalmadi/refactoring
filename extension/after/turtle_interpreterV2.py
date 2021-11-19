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
        ht = HelperTurtle()

        self.stack = []
        self.colorstack = []

    def drawString(self, dstring, distance, angle, circle_size, scale): 
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

        for c in dstring:
            if c == 'F':
                turtle.forward(distance)
            elif c == '-':
                turtle.right(angle)
            elif c == '+':
                turtle.left(angle)
            elif c == 'T':
                self.draw_leaves("red", "brown", circle_size)
            elif c == '[':
                self.save_location_header()
            elif c == ']':
                self.get_location_header()
            elif c == 'L':
                turtle.circle(circle_size)
            elif c == '<':
                self.colorstack.append(turtle.color()[0])
            elif c == '>': 
                k = self.colorstack.pop()
                turtle.color(k)
            elif c == 'g': 
                turtle.color('green')
            elif c == 'y': 
                turtle.color(0.8,0.8,0.3)
            elif c == 'r':
                turtle.color('red')
            elif c == 'b':
                turtle.color('blue')
            elif c == 'C': 
                self.big_circle(scale, circle_size)
            elif c == '?': 
                self.draw_square(distance)
            elif c == '!': 
                self.draw_triangle(distance)

    #TODO: addded methods to clean up if statement 
    def draw_leaves(self, color1, color2, circle_size):
        '''Draws leaves'''
        turtle.color(color1)
        turtle.begin_fill()
        turtle.circle(circle_size)
        turtle.color(color2)
        turtle.end_fill()

    def save_location_header(self):
        '''Saves the current location and header to the stack'''
        self.stack.append(turtle.position())
        self.stack.append(turtle.heading())

    def get_location_header(self):
        '''Returns the location and header previously saved to the stack'''
        turtle.penup()
        x = self.stack.pop()
        y = self.stack.pop()
        turtle.goto(y)
        turtle.setheading(x)
        turtle.pendown()
    
    def big_circle(self, scale, size):
        '''Draws a circle with the ability to scale it up to be bigger'''
        turtle.circle(size*scale)
    
    def draw_square(self, distance):
        '''Draws a square'''
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.right(90)
        turtle.forward(distance)
    
    def draw_triangle(self, distance):
        '''Draws a triangle'''
        turtle.forward(distance)
        turtle.right(240)
        turtle.forward(distance)
        turtle.right(240)
        turtle.forward(distance)



#TODO: Broke up god-class 
class HelperTurtle:

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
        self.xpos = xpos
        self.ypos = ypos

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
    
