"""
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
"""

import turtle
from game import *


class PongGame(Game):
    def __init__(
        self,
        win_w: int = 1200,
        win_h: int = 800,
        win_title: str = "Pong",
        bg_color: str = "black",
    ):
        window = make_window(win_title, bg_color, win_w, win_h)
        turt = make_turtle("square", "white", 1, 1, 0, int(win_h // 2 * 0.85))
        super().__init__(window, turt)

        # paddels
        paddle_speed = 20
        ball_x_speed, ball_y_speed = 0.0925, 0.0925
        self.paddle_stretch_h, self.paddle_stretch_w = 5, 1
        self.collision_multiplier = -1.5

        self.paddle_1 = Paddle(
            -int(win_w / 2 * 0.9),
            0,
            self.paddle_stretch_h,
            self.paddle_stretch_w,
            paddle_speed,
        )
        self.paddle_2 = Paddle(
            int(win_w / 2 * 0.9),
            0,
            self.paddle_stretch_h,
            self.paddle_stretch_w,
            paddle_speed,
        )

        self.paddles = [self.paddle_1, self.paddle_2]
        self.scores = [0, 0]

        # ball
        self.ball = Ball(1, 1, 0, 0, ball_x_speed, ball_y_speed, int(win_h // 2 * 0.85))

        # Pen
        self.font_size = int(win_h // 2 * 0.1)
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
            font=("Courier", self.font_size, "normal"),
        )

    def reset_ball(self):
        self.ball.goto(0, 0)
        self.ball.ball_dx *= -1

    def check_border(self, player: int):
        if (self.paddles[player].xcor() < 0) == (self.ball.xcor() < 0) and abs(
            self.ball.xcor()
        ) > abs(self.paddles[player].xcor()):
            return True

    def handle_border(self, player: int):
        self.scores[1 - player] += 1
        self.draw_score_board()
        self.reset_ball()

    def check_paddle_collision(self, player: int):
        if (
            (self.paddles[player].xcor() < 0) == (self.ball.xcor() < 0)
            and abs(self.paddles[player].xcor()) - 10 * self.paddle_stretch_w
            < abs(self.ball.xcor())
            < abs(self.paddles[player].xcor())
            and self.ball.ycor()
            < self.paddles[player].ycor() + 10 * self.paddle_stretch_h
            and self.ball.ycor()
            > self.paddles[player].ycor() - 10 * self.paddle_stretch_h
        ):
            return True
        return False

    def handle_paddle_collision(self, player: int):
        if self.paddles[player].xcor() > 0:
            self.ball.setx(self.paddles[player].xcor() - 10 * self.paddle_stretch_w)
        else:
            self.ball.setx(self.paddles[player].xcor() + 10 * self.paddle_stretch_w)
        self.ball.ball_dx *= self.collision_multiplier

    def iterate(self):
        self.window.update()
        self.ball.move()

        for player in [0, 1]:
            if self.check_border(player):
                self.handle_border(player)

            if self.check_paddle_collision(player):
                self.handle_paddle_collision(player)

    @staticmethod
    def play_game():
        game = PongGame()
        while True:
            game.iterate()


class PongObject:
    def __init__(self, x_position: int, y_position: int, myturt):
        self.x_position = x_position
        self.y_position = y_position
        self.turt = myturt

    def xcor(self):
        """ returns turtle x_cord """
        return self.turt.xcor()

    def ycor(self):
        """ returns turtle y_cord """
        return self.turt.ycor()

    def setx(self, x_cor: int):
        """ sets x position """
        self.turt.setx(x_cor)
        self.x_position = x_cor

    def sety(self, y_cor: int):
        """set y position"""
        self.turt.sety(y_cor)
        self.y_position = y_cor


class Paddle(PongObject):
    # implements a Pong game paddle

    def __init__(
        self,
        x_position: int,
        y_position: int,
        w_stretch: int,
        h_stretch: int,
        move_speed: int,
    ):
        """ initializes a paddle by inheriting PongObject """
        self.move_speed = move_speed
        turt = make_turtle(
            "square", "white", w_stretch, h_stretch, x_position, y_position
        )
        super(Paddle, self).__init__(x_position, y_position, turt)

    def up(self):
        y = self.turt.ycor() + self.move_speed
        self.sety(y)

    def down(self):
        y = self.turt.ycor() - self.move_speed
        self.sety(y)


class Ball(PongObject):
    # implements a Pong game ball

    def __init__(
        self,
        w_stretch: int,
        h_stretch: int,
        x_position: int,
        y_position: int,
        x_speed: int,
        y_speed: int,
        x_extent: int,
    ):
        """ intializes a ball with default direction and position """
        turt = make_turtle(
            "square", "white", w_stretch, h_stretch, x_position, y_position
        )

        super(Ball, self).__init__(x_position, y_position, turt)

        self.ball_dx = x_speed  # speed in x direction
        self.ball_dy = y_speed  # speed in y direction

        self.x_extent = x_extent

    def move(self):
        """ moves the ball in x and y directions """

        # Move the ball
        self.turt.setx(self.turt.xcor() + self.ball_dx)
        self.turt.sety(self.turt.ycor() + self.ball_dy)

        self.x_position = self.turt.xcor()
        self.y_position = self.turt.ycor()

        # Top and bottom
        if self.turt.ycor() > self.x_extent:
            self.turt.sety(self.x_extent)
            self.ball_dy *= -1

        elif self.turt.ycor() < -self.x_extent:
            self.turt.sety(-self.x_extent)
            self.ball_dy *= -1

    def goto(self, x_pos: int, y_pos: int):
        """ moves ball to new x, y positions """
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


def main():
    """ the main function where the game events take place """

    PongGame.play_game()


if __name__ == "__main__":
    main()
