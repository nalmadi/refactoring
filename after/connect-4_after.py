"""
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
"""

import turtle
from game import *


class Connect4Game(Game):
    """ class for connect-4 game """

    def __init__(
        self,
        win_w: int = 1200,
        win_h: int = 900,
        win_title: str = "Connect 4",
        bg_color: str = "light sky blue",
        grid_h: int = 5,
        grid_w: int = 7,
        connect_n: int = 4,
        turn: int = 1,
    ):

        self.grid_h, self.grid_w = grid_h, grid_w
        self.connect_n = connect_n
        self.turn = turn

        window = make_window(win_title, bg_color, win_w, win_h)
        turt = make_turtle("classic", "white", 1, 1, 0, 0)
        super().__init__(window, turt)

        self.tile_size = min(win_w // 16, win_h // 12)
        self.dot_colors = {1: "red", 2: "yellow", 0: "white"}
        self.dot_size = int(0.9 * self.tile_size)
        self.x_offset = int(-self.tile_size * self.grid_w / 2)
        self.y_offset = win_h - int(self.tile_size * (self.grid_h + 3))

        self.grid = [[0] * self.grid_w for _ in range(self.grid_h)]

        self.window.onscreenclick(self.play)
        self.window.listen()
        self.draw_grid()

    def teleport(self, x: int, y: int):
        self.turt.up()
        self.turt.goto(x, y)
        self.turt.down()

    def draw_grid(self):
        """impletments the abstract method "draw" from parent game class
        draws a grid at the offset location of tile_size"""

        self.teleport(self.x_offset, self.y_offset)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.teleport(
                    self.x_offset + col * self.tile_size,
                    self.y_offset - row * self.tile_size,
                )

                self.turt.dot(self.dot_size, self.dot_colors[self.grid[row][col]])

    def check_win(self, player: int):
        """checks the winner in the grid
        returns true if player won
        returns false if player lost
        """

        count = 0

        # check rows
        for row in range(self.grid_h):
            count = 0
            for col in range(self.grid_w):
                if self.grid[row][col] == player:
                    count += 1
                    if count == self.connect_n:
                        return True

                else:
                    count = 0

        # check columns
        for col in range(self.grid_w):
            count = 0
            for row in range(self.grid_h):
                if self.grid[row][col] == player:
                    count += 1
                    if count == self.connect_n:
                        return True

                else:
                    count = 0

        # check diagonal
        for row in range(self.grid_h):
            for col in range(self.grid_w):

                if row + (self.connect_n - 1) < self.grid_h:
                    diagonal_left = diagonal_right = True

                    if col + (self.connect_n - 1) < self.grid_w:
                        for i in range(self.connect_n):
                            if self.grid[row + i][col + i] != player:
                                diagonal_left = False
                                break

                        if diagonal_left:
                            return True

                    if col - (self.connect_n - 1) > -1:
                        diagonal_right = True
                        for i in range(self.connect_n):
                            if self.grid[row + i][col - i] != player:
                                diagonal_right = False
                                break

                        if diagonal_right:
                            return True

    def print_winner(self):
        if self.check_win(1):
            print("player 1 won")

        elif self.check_win(2):
            print("player 2 won")

    def iterate(self):
        """inside the while loop to keep the game playing"""
        selected_row = int(input("enter row, player " + str(self.turn) + ": "))
        selected_col = int(input("enter col, player " + str(self.turn) + ": "))

        if self.grid[selected_row][selected_col] == 0:
            self.grid[selected_row][selected_col] = self.turn

        self.draw_grid()
        self.window.update()

        self.print_winner()
        self.swtich_turn()

    def play(self, x_pos: float, y_pos: float):
        """updates the grid in playing"""
        row = int(
            abs((y_pos - self.y_offset - self.tile_size // 2) // (self.tile_size) + 1)
        )
        col = int(
            abs((x_pos - self.x_offset - self.tile_size // 2) // (self.tile_size) + 1)
        )
        print(row, col)

        if self.grid[row][col] == 0:
            self.grid[row][col] = self.turn
            self.print_winner()
            self.swtich_turn()

        self.draw_grid()
        self.window.update()

    def swtich_turn(self):
        """change turns in the game between two players"""
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


def main():
    """the main function where the game events take place"""

    connect4 = Connect4Game(1200, 900)
    while True:
        connect4.iterate()


if __name__ == "__main__":
    main()