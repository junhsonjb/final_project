import random

class Square:
	def __init__(self, boardSize):
		self.boardSize = boardSize
		# self.xCor = random.randint(0, boardSize[0])
		# self.yCor = random.randint(0, boardSize[1])
		self.coords = [(random.randint(0, boardSize[0])), (random.randint(0, boardSize[1]))]

	# def getXCor(self):
	# 	return self.xCor
	#
	# def getYCor(self):
	# 	return self.yCor

	def getCoords(self):
		return self.coords

	def __str__(self):
		return "x coorindate: " + str(self.getXCor()) + "\ny coordinate: " + str(self.getYCor())
