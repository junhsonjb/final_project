#THe view class code
import pygame
import random
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)

class View:
    def __init__(self, boardSize=(900,500)):
        self.boardSize = boardSize
        self.fontSize = 25

        pygame.init()
        self.display = pygame.display.set_mode(self.boardSize)
        pygame.display.set_caption("Snake: The Black Mamba")
        self.font = pygame.font.SysFont("comicsansms",self.fontSize)
    def fillWhite(self):
        self.display.fill(white)

    def flip(self):
        pygame.display.flip()

    def drawSnake(self, blocksize, color, dims):
        pygame.draw.rect(self.display,color,[dims[0],dims[1],blocksize,blocksize])

    def drawSquare(self, blocksize, color, dims):
        pygame.draw.rect(self.display,color,[dims[0],dims[1],blocksize,blocksize])
