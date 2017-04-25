#import statements
import random
import square

#class definition
class Snake:
	#initalizer function
	def __init__(self, boardSize):
		self.blockSize = 10 #the size of each block to be built, must be same as apple block size
		self.boardSize = boardSize #the width and height dimensions of the board
		self.snakehead = [] #list to be cleared in game loop, holds snake head coordinates
		self.snakelist = [] #list to keep all snake body coordinates
		self.snakelength = 1 #length to allow snake to grow to, MUST start at one
		self.xchange = 0 #amount to change x coord by, constantly added to xcord in game loop
        self.ychange = 0 #amount to change y coord by, constantly added to ycord in game loop
        self.xcord = boardSize[0] / 2 #x coordinate of snake body part, start in center of board
        self.ycord = boardSize[1] / 2 #y coordinate of snake body part, start in center of board

	#the function to move up on the board
	def up(self):
		self.ychange = -self.blockSize
		self.xchange = 0

	#the function to move down on the board
	def down(self):
		self.ychange = self.blockSize
		self.xchange = 0

	#the function to move left on the board
	def left(self):
		self.xchange = -self.blockSize
		self.ychange = 0

	#the function to move right on the board
	def right(self):
		self.xchange = self.blockSize
		self.ychange = 0

	#magic string function
	def __str__(self):
		return "Snake length: " + str(self.snakelength) + ", snake x coordinate: " + str(self.xcord) + ", snake y coordinates: " + str(self.ycord) + "."
