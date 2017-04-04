import random

class Snake:
	def __init__(self, boardSize, length=4, color=1):
		self.boardSize = boardSize	
		self.xCor = ( boardSize[0] ) / 2
		self.yCor = ( boardSize[1] ) / 2

		self.length = length
		self.color = color
		
	def getXCor(self):
		return self.xCor

	def getYCor(self):
		return self.yCor

	def getLength(self):
		return self.length
	
	def moveRight(self):
		while ( (self.xCor > 0 and self.xCor < self.boardSize[0]) and (self.yCor > 0 and self.yCor < self.boardSize[1]) ):
			self.xCor += 1

	def moveLeft(self):
		while ( (self.xCor > 0 and self.xCor < self.boardSize[0]) and (self.yCor > 0 and self.yCor < self.boardSize[1]) ):
			self.xCor -= 1

	def moveUp(self):
		while ( (self.xCor > 0 and self.xCor < self.boardSize[0]) and (self.yCor > 0 and self.yCor < self.boardSize[1]) ):
			self.yCor -= 1

	def moveDown(self):
		while ( (self.xCor > 0 and self.xCor < self.boardSize[0]) and (self.yCor > 0 and self.yCor < self.boardSize[1]) ):
			self.yCor += 1

	def grow(self):
		self.length += 1

	def __str__(self):
		return "x coorindate: " + str(self.getXCor()) + "\ny coordinate: " + str(self.getYCor())
