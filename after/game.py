from abc import abstractmethod
import turtle

def make_window(window_title, bgcolor, width, height):
    """this function creates a screen object and returns it"""

    window = turtle.getscreen()  # Set the window size
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(width, height)
    window.tracer(0)  # turns off screen updates for the window Speeds up the game
    return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    """ creates a turtle and sets initial position """

    turt = turtle.Turtle()
    turt.speed(0)  # Speed of animation, 0 is max
    turt.shape(shape)  # square defualt is 20,20
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length)
    turt.penup()
    turt.goto(x_pos, y_pos)  # Start position
    return turt

class Game:
    def __init__(self, window, turtle):
        self.window = window
        self.turt = turtle

    @abstractmethod
    def iterate(self):
        pass

    @staticmethod
    @abstractmethod
    def play_game(self):
        pass
