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
    """class for connect-4 game"""

    def __init__(self):
        window = make_window("Connect 4", "light sky blue", 800, 600)
        cturt = make_turtle("classic", "white", 1, 1, 0, 0)
        super().__init__(window, cturt)
        self.turn = 1
        self.grid = []

        for rows in range(5):
            self.grid.append([0] * 7)

        self.window.onscreenclick(self.play)
        self.window.listen()

        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50

        self.draw_grid(self.x_offset, self.y_offset)

    def draw_grid(self, x_pos, y_pos):
        """impletments the abstract method "draw" from parent game class
        draws a grid at x, y with a specific tile_size"""

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

    def check_win(self, player):
        """checks the winner in the grid
        returns true if player won
        returns false if player lost
        """
        count = 0

        # check rows
        for row in range(len(self.grid)):
            count = 0
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # check columns
        for col in range(len(self.grid[0])):
            count = 0
            for row in range(len(self.grid)):
                if self.grid[row][col] == player:
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
                        self.grid[row][col] == 1
                        and self.grid[row + 1][col + 1] == 1
                        and self.grid[row + 2][col + 2] == 1
                        and self.grid[row + 3][col + 3] == 1
                    ):
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

            if self.turn == 1:
                self.grid[selected_row][selected_col] = 1
            else:
                self.grid[selected_row][selected_col] = 2

        self.draw_grid(-150, 200)
        self.window.update()

        self.print_winner()
        self.swtich_turn()

    def play(self, x_pos, y_pos):
        """updates the grid in playing"""
        row = int(abs((y_pos - self.y_offset - 25) // (self.tile_size) + 1))
        col = int(abs((x_pos - self.x_offset - 25) // (self.tile_size) + 1))
        print(row, col)
        self.grid[row][col] = self.turn
        self.draw_grid(self.x_offset, self.y_offset)
        self.window.update()

        self.print_winner()
        self.swtich_turn()

    def swtich_turn(self):
        """change turns in the game between two players"""
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


def main():
    """the main function where the game events take place"""

    connect4 = Connect4Game()
    while True:
        connect4.iterate()


if __name__ == "__main__":
    main()
