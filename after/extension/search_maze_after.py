import turtle
import time
from playsound import playsound
from multiprocessing import Process


class SearchMaze:
    """SearchMaze Game class"""

    def __init__(self):
        self.turt = turtle.Turtle()
        self.window = turtle.getscreen()
        self.grid = []
        self.steps = 0

        # set offsets and tile size for drawing the grid
        self.x_offset = -150
        self.y_offset = 200
        self.tile_size = 50

        self.window.bgcolor("slate gray")
        turtle.hideturtle()
        self.turt.hideturtle()
        self.turt.shape("square")
        self.turt.shapesize(2.5, 2.5)

    def goto(self, x, y):
        """move turtle to a position without drawing"""
        self.turt.up()
        self.turt.goto(x, y)
        self.turt.down()

    def draw_grid(self, x_pos, y_pos):
        """draws a grid at x_pos, y_pos"""

        # turn off tracer for fast drawing
        self.window.tracer(False)

        # move turtle to initial drawing position
        self.goto(x_pos, y_pos)

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                # move turtle to the position of the cell in the grid
                self.goto(x_pos + col * self.tile_size, y_pos - row * self.tile_size)

                # if the cell is an obstacle (X) draw a black dot
                if self.grid[row][col] == "X":
                    # self.turt.dot(self.tile_size-5, "Black")
                    self.turt.color("grey", "black")
                    self.turt.stamp()

                # if the cell is the start drawing position (S) draw a yellow dot
                elif self.grid[row][col] == "S":
                    # self.turt.dot(self.tile_size-5, "yellow")
                    self.turt.color("grey", "yellow")
                    self.turt.stamp()

                # if the cell is the End position (E) draw a Red dot
                elif self.grid[row][col] == "E":
                    # self.turt.dot(self.tile_size-5, "red")
                    self.turt.color("grey", "red")
                    self.turt.stamp()

                # if the cell is part of a path (P) draw a royalblue dot
                elif self.grid[row][col] == "P":
                    # self.turt.dot(self.tile_size-5, "royalblue")
                    self.turt.color("grey", "royalblue")
                    self.turt.stamp()

                # if the cell has been tried before (T) draw a light blue dot
                elif self.grid[row][col] == "T":
                    # self.turt.dot(self.tile_size-5, "light blue")
                    self.turt.color("grey", "light blue")
                    self.turt.stamp()

                # if the cell is part of a deadend (D) draw a gray dot
                elif self.grid[row][col] == "D":
                    # self.turt.dot(self.tile_size-5, "gray")
                    self.turt.color("gainsboro", "gray")
                    self.turt.stamp()

                # else draw a white dot
                else:
                    # self.turt.dot(self.tile_size-5, "white")
                    self.turt.color("grey", "white")
                    self.turt.stamp()

        # turn tracer back on
        self.window.tracer(True)

    def find_start(self):
        """finds the start position (S) in the grid
        returns a tuple of start row and col
        """
        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                # cell at row, col is 'S' return row and col as a tuple
                if self.grid[row][col] == "S":
                    return (row, col)

    def set_grid(self, file_name):
        """reads a maze file and initializes a gird with its contents"""
        # create an empty grid (an empty list called grid)
        grid = []

        # open the text file
        file = open(file_name)

        # read a line from the file
        line = file.readline()

        # replace \n with nothing
        line = line.replace("\n", "")

        while line:
            # split the line into tokens
            tokens = line.split(",")

            # add the tokens to the grid as a single row
            grid.append(tokens)

            line = file.readline()

            # replace \n with nothing
            line = line.replace("\n", "")

        self.grid = grid

    def search_from(self, row, col):
        """recursive function to search the grid for the end (E)"""
        self.steps += 1

        # make sure row and col are valid points on the grid
        if row < 0 or col < 0 or row == len(self.grid) or col == len(self.grid[0]):
            # return False if not valid
            return False

        # check that the grid cell at row and col is not obstacle, tried, or deadend
        if (
            self.grid[row][col] == "X"
            or self.grid[row][col] == "T"
            or self.grid[row][col] == "D"
        ):
            # return False if obstacle, tried, or deadend
            return False

        # If end is found at row, col return True
        if self.grid[row][col] == "E":
            return True

        # If the cell at row, col is not the start cell, mark the cell as tried (T)
        if self.grid[row][col] != "S":
            self.grid[row][col] = "T"

        # draw the grid
        self.draw_grid(self.x_offset, self.y_offset)

        # pause the program for a short duration, try 0.5 and 0.01 seconds
        time.sleep(0.25)

        # recursively search differnt directions adjacent to current row, col (up, down, left, right)
        found = (
            self.search_from(row - 1, col)
            or self.search_from(row + 1, col)
            or self.search_from(row, col - 1)
            or self.search_from(row, col + 1)
        )

        # if any of the 4 directions returns True, mark the cel at row, col as part of the path and return True
        if found and self.grid[row][col] != "S":
            self.grid[row][col] = "P"
            return True
        # else, if the cell at row, col is not the start cell (S), mark it as a deadend
        elif self.grid[row][col] != "S":
            self.grid[row][col] = "D"

    def create_path(self):
        """create a list of tuples representing the path"""
        path = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == "P":
                    path.append((row, col))
        return path

    def background_music(self, filename):
        """plays tetris music in the background"""
        playsound(filename)

    def start_game(self, grid_file):
        """reads a maze file and sets the search parameters"""

        # read maze file and create playground grid
        self.set_grid(grid_file)

        # find start position
        row, col = self.find_start()

        # call the search function, it takes row and column
        self.search_from(row, col)

        # print path length
        created_path = self.create_path()
        print("path length:", len(created_path))

        # draw the final grid
        self.draw_grid(self.x_offset, self.y_offset)

        # pause the grid drawing for 4 seconds
        time.sleep(4)

        # print the number of steps taken to find the path
        print("number of steps taken to reach answer:", self.steps)


def main():
    """the main function where the game events take place"""
    sm = SearchMaze()

    # play bg music and iterates the process
    # p = Process(target=sm.background_music, args=('Tetris.mp3'))
    # p.start()

    sm.start_game("maze2.txt")
    # p.terminate()


if __name__ == "__main__":
    main()
