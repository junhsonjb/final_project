import random
import square

class Snake:
	def __init__(self, boardSize, length=1, color=1):
		#CONSIDER REMOVING THE length VARIABLE
		#IF YOU DO, YOU COULD SEE LENGTH BY CHECKING len(self.bodycoords)
		self.length = length
		self.color = color

		self.boardSize = boardSize#should be a tuple with board's x and y coords
		#self.xCor = ( boardSize[0] ) / 2
		#self.yCor = ( boardSize[1] ) / 2
		#Initialize the first body part coordinate in the center of screen
		self.bodycoords = [ [(self.boardSize[0] / 2), (self.boardSize[1] / 2)] ]

	# def getXCor(self):
	# 	return self.xCor

	# def getYCor(self):
	# 	return self.yCor

	def getbodycoords(self):
		return self.bodycoords

	def getLength(self):
		return self.length

	#RETURN BOOLEAN VALUE BASED ON IF SNAKE PARTS ARE IN BOUNDS OF BOARD
	def inBounds(self):
		for i in range(len(self.bodycoords)):
			#IF: the x and y coords of each body part is within the x and y coords of the board:
			if (self.bodycoords[i][0] < self.boardSize[0] and self.bodycoords[i][1] < self.boardSize[1]):
				return True
			else:
				return False

	#MOVEMENT FUNCTIONS
	def moveRight(self):
		while ( inBounds() ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][0] += 1

	def moveLeft(self):
		while ( inBounds() ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][0] -= 1

	def moveUp(self):
		while ( inBounds() ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][1] -= 1

	def moveDown(self):
		while ( inBounds() ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][1] += 1

	#GROWTH FUNCTION
	def grow(self):
		#add another list to bodycoords, where x and y are += 1 of its previos list element
		self.bodycoords += [(self.bodycoords[-1][0] + 1), (self.bodycoords[-1][1] + 1)]

	def __str__(self):
		return "head x coorindate: " + str(self.bodycoords[0][0]) + "\nbody y coordinate: " + str(self.bodycoords[0][1])
