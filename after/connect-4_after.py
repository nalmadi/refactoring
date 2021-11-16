"""
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
"""

import turtle


def makeWindow(
    width,
    height,
    title="title",
    bgColor="light sky blue",
):
    # creates a screen object and returns it
    window = turtle.getscreen()  # Set the window size
    window.setup(width, height)
    window.tracer(0)
    window.bgcolor(bgColor)
    window.title(title)
    return window


def make_turtle(
    x_pos, y_pos, shape="classic", color="white", stretch_width=1, stretch_length=1
):
    """creates a turtle and sets initial position"""

    turt = turtle.Turtle()
    turt.speed(0)  # Speed of animation, 0 is max
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length)
    turt.penup()
    turt.goto(x_pos, y_pos)  # Start position
    return turt


class Connect4:
    def __init__(self, grid, window, turt, x_offset=-150, y_offset=200):
        self.window = window
        self.turt = turt
        self.turt.penup()
        self.grid = grid
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.tile_size = 50
        self.draw_grid(x_offset, y_offset)
        self.turn = 1
        self.window.onscreenclick(self.play)
        self.window.listen()

    def makeWindow(self, width, height):
        # creates a screen object and returns it
        self.window = turtle.getscreen()  # Set the window size
        self.window.setup(width, height)

    def draw_grid(self, x_pos, y_pos):
        # draws a grid at x, y with a specific tile_size
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                self.turt.up()
                self.turt.goto(
                    x_pos + col * self.tile_size, y_pos - row * self.tile_size
                )
                self.turt.down()

                if self.grid[row][col] == 1:
                    self.turt.dot(self.tile_size - 5, "red")

                elif self.grid[row][col] == 2:
                    self.turt.dot(self.tile_size - 5, "yellow")

                else:
                    self.turt.dot(self.tile_size - 5, "white")

    def check_win(self):

        count = 0

        # check rows
        for row in range(len(self.grid)):
            count = 0
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == self.turn:
                    count += 1

                    if count == 4:
                        return True
                else:
                    count = 0

        # check columns
        for col in range(len(self.grid[0])):
            count = 0
            for row in range(len(self.grid)):
                if self.grid[row][col] == self.turn:
                    count += 1

                    if count == 4:
                        return True
                else:
                    count = 0

        # check diagonal
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                if row + 3 < len(self.grid) and col + 3 < len(self.grid[row]):
                    if (
                        self.grid[row][col] == self.turn
                        and self.grid[row + 1][col + 1] == self.turn
                        and self.grid[row + 2][col + 2] == self.turn
                        and self.grid[row + 3][col + 3] == self.turn
                    ):
                        return True

    # check if statements
    # check self.check_win
    def play(self, x_pos, y_pos):
        row = int(abs((y_pos - self.y_offset - 25) // (50) + 1))
        col = int(abs((x_pos - self.x_offset - 25) // (50) + 1))
        print(row, col)
        self.grid[row][col] = self.turn
        self.draw_grid(self.x_offset, self.y_offset)
        self.window.update()

        if self.check_win():
            print("player ", self.turn, " won")

        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


def main():
    grid = []

    for rows in range(5):
        grid.append([0] * 7)

    turt = make_turtle(0, 0)
    window = makeWindow(800, 600, "Game")
    game = Connect4(grid, window, turt)
    game.window.update()

    while True:
        selected_row = int(input("enter row, player " + str(game.turn) + ": "))
        selected_col = int(input("enter col, player " + str(game.turn) + ": "))

        if game.grid[selected_row][selected_col] == 0:

            if game.turn == 1:
                game.grid[selected_row][selected_col] = 1
            else:
                game.grid[selected_row][selected_col] = 2

        game.draw_grid(-150, 200)

        if game.check_win(1):
            print("player 1 won")
        elif game.check_win(2):
            print("player 2 won")

    # window.exitonclick()


if __name__ == "__main__":
    main()
