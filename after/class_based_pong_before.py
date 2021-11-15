"""
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
"""

import turtle
from abc import abstractmethod


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


class PongObject:
    def __init__(self, x_position, y_position, myturt):
        self.x_position = x_position
        self.y_position = y_position
        self.turt = myturt

    def xcor(self):
        """ returns turtle x_cord """
        return self.turt.xcor()

    def ycor(self):
        """ returns turtle y_cord """
        return self.turt.ycor()

    def setx(self, x_cor):
        """ sets x position """
        self.turt.setx(x_cor)
        self.x_position = x_cor

    def sety(self, y_cor):
        """set y position"""
        self.turt.sety(y_cor)
        self.y_position = y_cor


class Paddle(PongObject):
    # implements a Pong game paddle

    def __init__(self, x_position, y_position):
        """ initializes a paddle by inheriting PongObject """
        turt = make_turtle("square", "white", 5, 1, x_position, y_position)
        super(Paddle, self).__init__(x_position, y_position, turt)

    def up(self):
        y = self.turt.ycor() + 20
        self.sety(y)

    def down(self):
        y = self.turt.ycor() - 20
        self.sety(y)


class Ball(PongObject):
    # implements a Pong game ball

    def __init__(self):
        """ intializes a ball with default direction and position """
        x = 0
        y = 0
        turt = make_turtle("square", "white", 1, 1, 0, 0)

        super(Ball, self).__init__(x, y, turt)

        self.ball_dx = 0.0925  # speed in x direction
        self.ball_dy = 0.0925  # speed in y direction

    def move(self):
        """ moves the ball in x and y directions """

        # Move the ball
        self.turt.setx(self.turt.xcor() + self.ball_dx)
        self.turt.sety(self.turt.ycor() + self.ball_dy)

        self.x_position = self.turt.xcor()
        self.y_position = self.turt.ycor()

        # Top and bottom
        if self.turt.ycor() > 290:
            self.turt.sety(290)
            self.ball_dy *= -1

        elif self.turt.ycor() < -290:
            self.turt.sety(-290)
            self.ball_dy *= -1

    def goto(self, x_pos, y_pos):
        """ moves ball to new x, y positions """
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


class Game:
    def __init__(self, window, turtle):
        self.window = window
        self.turt = turtle

    @abstractmethod
    def iterate(self):
        pass


class PongGame(Game):
    def __init__(self):
        window = make_window("Pong - A CS151 Reproduction!", "black", 800, 600)
        turt = make_turtle("square", "white", 1, 1, 0, 260)

        super().__init__(window, turt)

        # Score
        # self.score_player1 = 0
        # self.score_player2 = 0

        # paddels
        self.paddle_1 = Paddle(-350, 0)
        self.paddle_2 = Paddle(350, 0)

        self.paddles = [self.paddle_1, self.paddle_2]
        self.scores = [0, 0]

        # ball
        self.ball = Ball()

        # Pen
        self.draw_score_board()
        self.turt.hideturtle()

        # Keyboard bindings
        window.listen()  # Listen for keyboard input
        window.onkeypress(self.paddle_1.up, "w")  # when you press w run paddle_a_up
        window.onkeypress(self.paddle_1.down, "s")
        window.onkeypress(self.paddle_2.up, "Up")
        window.onkeypress(self.paddle_2.down, "Down")

    def draw_score_board(self):
        self.turt.clear()
        self.turt.write(
            "Player A: " + str(self.scores[0]) + "  Player B: " + str(self.scores[1]),
            align="center",
            font=("Courier", 24, "normal"),
        )

    def reset_ball(self):
        self.ball.goto(0, 0)
        self.ball.ball_dx *= -1

    def check_border(self, player):
        if (self.paddles[player].xcor() < 0) == (self.ball.xcor() < 0) and abs(
            self.ball.xcor()
        ) > abs(self.paddles[player].xcor()):
            return True

    def handle_border(self, player):
        self.scores[1 - player] += 1
        self.draw_score_board()
        self.reset_ball()

    def check_paddle_collision(self, player):
        if (
            (self.paddles[player].xcor() < 0) == (self.ball.xcor() < 0)
            and abs(self.paddles[player].xcor()) - 10
            < abs(self.ball.xcor())
            < abs(self.paddles[player].xcor())
            and self.ball.ycor() < self.paddles[player].ycor() + 50
            and self.ball.ycor() > self.paddles[player].ycor() - 50
        ):
            return True
        return False

    def handle_paddle_collision(self, player):
        self.ball.setx(self.paddles[player].xcor() * 34 / 35)
        self.ball.ball_dx *= -1.5

    def iterate(self):
        self.window.update()
        self.ball.move()

        for player in [0, 1]:
            if self.check_border(player):
                self.handle_border(player)

            if self.check_paddle_collision(player):
                self.handle_paddle_collision(player)


def main():
    """ the main function where the game events take place """
    game = PongGame()

    while True:
        game.iterate()


if __name__ == "__main__":
    main()
