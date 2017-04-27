import random


class Square:
	def __init__(self, boardSize, blockSize):
	    self.blockSize = blockSize
	    self.boardSize = boardSize
	    self.xcord = round(random.randint(0, self.boardSize[0] - blockSize) / blockSize) * blockSize
	    self.ycord = round(random.randint(0, self.boardSize[1] - blockSize) / blockSize) * blockSize

	def resetSquareCoords(self, blockSize):
		self.xcord = round(random.randint(0, self.boardSize[0] - blockSize) / blockSize) * blockSize
		self.ycord = round(random.randint(0, self.boardSize[1] - blockSize) / blockSize) * blockSize
