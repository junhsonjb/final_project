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
        self.font = pygame.font.SysFont("comicsansms", self.fontSize)
        self.jokes = [
        "What's the best language: Python!!",
        "What's a snake's favorite subject : HISSSS-tory!!!",
        "How would a snake shoot something? With BOA and Arrow!!!",
        "What do you call a snake that works for the government? A civil SERPENT!!!"
        ]

    def fillWhite(self):
        self.display.fill(white)

    def flip(self):
        pygame.display.flip()

    def drawSnake(self, blocksize, color, dims):
        pygame.draw.rect(self.display,color,[dims[0],dims[1],blocksize,blocksize])

    def message(self, color, message):
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 0])

    def message2(self, color, message):
        #kobeText = "Kobe Would be so proud"
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 15])

    def message3(self, color, message):
        #jokeText = random.choice(self.jokes)
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 30])

    def message4(self, color, message):
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 45])



    def drawSquare(self, blocksize, color, dims):
        pygame.draw.rect(self.display,color,[dims[0],dims[1],blocksize,blocksize])
