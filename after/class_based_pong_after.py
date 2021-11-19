'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

import turtle

#TODO: Created the game class 
class Game:

    def __init__(self, p1_score, p2_score, border_1, border_2, top_border, bottom_border):

        self.p1_score = p1_score
        self.p2_score = p2_score
        self.border_1 = border_1
        self.border_2 = border_2
        self.top_border = top_border
        self.bottom_border = bottom_border
        self.pen = None

    #TODO: Added to the game class 
    def make_window(self, window_title, bgcolor, width, height):
        '''this function creates a screen object and returns it'''

        window = turtle.getscreen() #Set the window size
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(width, height)
        window.tracer(0) #turns off screen updates for the window Speeds up the game
        return window

    def set_game_score(self, x_position):
        '''Updates the gams score when someone scores'''
        if x_position > self.border_1:     
            self.p1_score +=1 
            return True
        if x_position < self.border_2:
            self.p2_score += 1
            return True

    #TODO: Made part of the game class 
    def make_pen(self, shape, color, width, length, x_pos, y_pos):
        '''Creates a pen to draw the score board'''

        pen = make_turtle(shape, color, width, length, x_pos, y_pos)
        self.pen = pen
        return pen

    def create_Scoreboard(self, scoreCard, align, font):
        '''Creates the scoreboard'''

        self.pen.write(scoreCard, align=align, font=font)
        self.pen.hideturtle()

    def update_Scoreboard(self, message, align, font):
        '''Updates the Scoreboard'''

        self.pen.clear()
        self.pen.write(message, align=align, font=font)
        self.pen.hideturtle()

    #TODO: Moved from to the game class 
    def set_top_bottom_bounds(self, yposition):
        '''Sets the top and bottom borders'''

        if yposition > self.top_border:
            return 1
        if yposition < self.bottom_border:
            return 0


class Paddle:

    #TODO: Added more parameters for color, shape, length and width
    def __init__(self, x_position, y_position, shape, color, length, width):
        ''' initializes a paddle with a position '''

        self.x_position = x_position
        self.y_position = y_position
        self.shape = shape
        self.color = color
        self.length = length
        self.width = width

        self.turt = make_turtle(self.shape, self.color, self.length, self.width, self.x_position, self.y_position)

    def up(self):
        '''Makes the turtle go up'''

        y = self.return_position()[1]
        y += 20
        self.turt.sety(y)
        self.y_position = y


    def down(self):
        '''Makes the turtle go down'''

        y = self.return_position()[1]
        y -= 20            
        self.turt.sety(y)
        self.y_position = y

    #TODO: Combined the xcor and ycor functions
    def return_position(self):
        '''Returns the position of the turtle'''

        return self.x_position, self.y_position


    #TODO: Redundant methods removed 
    # def xcor(self):
    #     ''' returns turtle x_cord '''
    #     return self.turt.xcor()

    
    # def ycor(self):
    #     ''' returns turtle y_cord '''
    #     return self.turt.ycor()


class Ball:

    #TODO: Added more parameters to the ball, also made some names better, got rid of comments since the names were improved
    def __init__(self, shape, color, length, width, x_cordinate, y_cordinate, x_speed = 0.0925, y_speed = 0.0925):
        ''' intializes a ball with default direction and position '''

        self.turt = make_turtle(shape, color, length, width, x_cordinate, y_cordinate)
        self.ball_x_speed = x_speed
        self.ball_y_speed = y_speed 
        self.x_position = x_cordinate
        self.y_position = y_cordinate


    def move(self):
        ''' moves the ball in x and y directions '''

        self.turt.setx(self.turt.xcor() + self.ball_x_speed)
        self.turt.sety(self.turt.ycor() + self.ball_y_speed)

        self.x_position = self.turt.xcor()
        self.y_position = self.turt.ycor()


    #TODO: Combined these tow functions in one position function
    def return_position(self):
        '''Returns the turtle postion'''
        return self.x_position, self.y_position
    
    #TODO: Replaced with return_postion function 
    # def xcor(self):
    #     ''' returns turtle x_cord '''
    #     return self.turt.xcor()

    
    # def ycor(self):
    #     ''' returns turtle y_cord '''
    #     return self.turt.ycor()

    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos

    def setx(self, x_cor):
        ''' sets the ball x position '''
        self.turt.setx(x_cor)
        self.x_position = x_cor

    def sety(self, y_cor):
        ''' sets the ball y position '''
        self.turt.sety(y_cor)
        self.y_position = y_cor

# TODO: Left alone 
def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0)
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos)
    return turt


def main():
    ''' the main function where the game events take place '''
    game = Game(0, 0, 350, -350, 290, -290)

    #TODO: Made window part of the game class 
    window = game.make_window("Pong - A CS151 Reproduction!", "black", 800, 600)

    #TODO: made score part of the game class
    # # Score
    # score_player1 = 0
    # score_player2 = 0

    # paddels
    paddle_1 = Paddle(-350, 0, 'square','white', 5, 1)
    paddle_2 = Paddle(350, 0, 'square','white', 5, 1)

    # ball
    ball = Ball("circle", 'white', 2, 2, 0, 0)

    game.make_pen("square", "white", 1, 1, 0, 260)
    game.create_Scoreboard("Player A: 0  Player B: 0", "center", ("Courier", 24, "normal"))

    #TODO: Made this part of the game class
    # # Pen
    # pen = make_turtle("square", "white", 1, 1, 0, 260)
    # pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    # pen.hideturtle()    
    
    # Keyboard bindings
    window.listen() #Listen for keyboard input
    window.onkeypress(paddle_1.up, "w") #when you press w run paddle_a_up
    window.onkeypress(paddle_1.down, "s")
    window.onkeypress(paddle_2.up, "Up")
    window.onkeypress(paddle_2.down, "Down")

    # Main game loop
    while True:
        window.update() #This is the update to offset the wn.tracer(0)

        ball.move()

        # Border checking    
        #TODO: Left and right, in update_scoreboard method
        if game.set_game_score(ball.x_position):
            game.update_Scoreboard("Player A: "+ str(game.p1_score) + "  Player B: "+ str(game.p2_score), align="center", font=("Courier", 24, "normal"))
            #Added to game class
            # score_player1 += 1
            # pen.clear()
            # pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.ball_x_speed *= -1
        
        #TODO: Used Top and Bottom function (was not being used before)
        if game.set_top_bottom_bounds(ball.y_position) == 1:
            ball.sety(290)
            ball.ball_y_speed *= -1
        elif game.set_top_bottom_bounds(ball.y_position) == 0:
            ball.sety(-290)
            ball.ball_y_speed *= -1


        #TODO: Included in game.update_Scoreboard
        # elif game.set_game_score(ball.x_position):
        #     #Added to game class 
        #     # score_player2 += 1
        #     # pen.clear()
        #     # pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
        #     ball.goto(0, 0)
        #     ball.ball_x_speed *= -1

        # TODO: Paddle and ball collisions (left alone)
        if ball.x_position < -340 and ball.x_position > -350 and ball.y_position < paddle_1.y_position + 50 and ball.y_position > paddle_1.y_position - 50:
            ball.setx(-340)
            ball.ball_x_speed *= -1.5
        
        elif ball.x_position > 340 and ball.x_position < 350 and ball.y_position < paddle_2.y_position + 50 and ball.y_position > paddle_2.y_position - 50:
            ball.setx(340)
            ball.ball_x_speed *= -1.5






if __name__ == "__main__":
	main()
