import random
import square

class Snake:
	def __init__(self, boardSize, length=1, color=1):
		self.length = length
		self.color = color

		self.boardSize = boardSize
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

	#MOVEMENT FUNCTIONS
	def moveRight(self):
		while ( """in board bounds""" ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][0] += 1

	def moveLeft(self):
		while ( """in board bounds""" ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][0] -= 1

	def moveUp(self):
		while ( """in board bounds""" ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][1] -= 1

	def moveDown(self):
		while ( """in board bounds""" ):
			for i in range(len(self.bodycoords)):
				self.bodycoords[i][1] += 1

	#GROWTH FUNCTION
	def grow(self):

		#FUNCTION TO BE COMPLETED AND PLACED IN BOARD CLASS
		# if (bodycoords[0] == square.coords)
		# 	self.length += 1
		# 	self.bodycoords += [] #add a new list element ([x, y] -- but its empty right now) to bodycoords
		# 	#CREATE NEW SQUARE

	def __str__(self):
		return "x coorindate: " + str(self.getXCor()) + "\ny coordinate: " + str(self.getYCor())
