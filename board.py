import snake
import square

class Board:

    def __init__(self, snake, sqr, bounds, bkgrd):
        self.snake = snake
        self.square = sqr
        self.bounds = bounds
        self.background = bkgrd


    #ACCESSOR METHODS
    def getSnake(self):
        return self.snake
        #RETURNS SNAKE OBJECT

    def getSquare(self):
        return self.square
        #RETURNS SQUARE OBJECT

    def getSnakePlacement(self):
        return self.snake.bodycoords
        #RETURNS A LIST OF LISTS FOR SNAKE BODY COMPONENTS [ [x1, y1], [x2, y2], ..., [xN, yN] ]

    def getSquarePlacement(self):
        return self.square.coords
        #RETURNS A LIST OF X AND Y COORDS FOR SQUARE [x, y]

    def getBounds(self):
        return self.bounds
        #RETURNS A LIST [xBound, yBound]

    def getBack(self):
        return self.background
        #I'm not sure what type this will be yet. First guess - object
    #END ACCESSOR MEHTODS

    def grow(self):
        if (self.snakey.bodycoords[0] == self.apple.coords):
            self.snakey.length += 1#consider making the snake grow by more upon eating
            self.snakey.bodycoords += []
            #SET SAID APPLE TO DISAPPEAR AND MAKE NEW ONE
            self.apple = square.Square()#save new apple in same name deletes the old one!

    def dead(self):
        all_but_head = self.snakey.bodycoords[1:]
        if (self.snakey.bodycoords[0] in all_but_head):
            #How to set the game to be over?
            pass #this will be the code that sets the game to be over
