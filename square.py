import random

class Square:
	def __init__(self, boardSize, blockSize):
        self.blockSize = blockSize
        self.boardSize = boardSize
        self.xcord = round(random.randint(0, self.boardSize[0] - blockSize) / 10.0) * 10.0
        self.ycord = round(random.randint(0, self.boardSize[1] - blockSize) / 10.0) * 10.0

	def resetAppleCoords(self, blockSize):
		self.xcord = round(random.randint(0, self.boardSize[0] - blockSize) / 10.0) * 10.0
        self.ycord = round(random.randint(0, self.boardSize[1] - blockSize) / 10.0) * 10.0
