import random #we'll need the random function to randomly place the squares

class Square:
	#initialize the class
	def __init__(self, boardSize, blockSize):
	    self.blockSize = blockSize #the size to draw each block
	    self.boardSize = boardSize #the size of the board -- to know x and y maximum bounds
		#set the x and y coordinates to random values within the bounds of the board
	    self.xcord = round(random.randint(0, self.boardSize[0] - blockSize) / blockSize) * blockSize
	    self.ycord = round(random.randint(0, self.boardSize[1] - blockSize) / blockSize) * blockSize

	def resetSquareCoords(self, blockSize):
		#REset the x and y coordinates to random values within the bounds of the board
		self.xcord = round(random.randint(0, self.boardSize[0] - blockSize) / blockSize) * blockSize
		self.ycord = round(random.randint(0, self.boardSize[1] - blockSize) / blockSize) * blockSize
