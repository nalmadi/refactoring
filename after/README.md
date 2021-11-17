# Refactored Programs
Game: abstract class to be implemented by the class of the two games; high-level functions for making turtle and initializing windows.

---------
### Pong Game:
Pong Game (implements Game): the object class of the Pong game, contains attributes of the the paddel and ball objects, and methods to start and iterate the game.

PongObject: parent object class for objects used in Pong games with methods primarily for drawing the objects 

Paddle (inherits PongObject)
Ball (inherits PongObject)

----------
### Connect-4:
Connect4Game: object class for the game - contains attributes of the grid and universal variables (such as x and y offsets) and methods to iterate through the game.
