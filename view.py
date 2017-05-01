#THe view class code
import pygame
WHITE = (255, 255, 255)

class View:
    #initialize the class
    def __init__(self, boardSize=(900,500)):
        self.boardSize = boardSize #the size of the board (width, height)
        self.fontSize = 25 #set a font size
        self.display = pygame.display.set_mode(self.boardSize)#make a pygame display variable
        #these are some corny jokes for the controller to choose from and display
        #at the end of a round. This data is not specific to the snake class nor
        #the square class. For those reasons and because it is not expansive enough
        #to merit its own model, it is specified in the view.
        self.jokes = [
        "What's the best language: Python!!",
        "What's a snake's favorite subject : HISSSS-tory!!!",
        "How would a snake shoot something? With BOA and Arrow!!!",
        "What do you call a snake that works for the government? A civil SERPENT!!!",
        "What's the difference between Kobe Bryant and time: TIME PASSES!!!",
        "What does Kobe do with milk and Oreos? DUNK THEM!!!!",
        "Who cools Kobe down after he heats up during a game? HIS FANS!!!!",
        ]

        pygame.init() #initialize pygame
        #set a pygame font. This had to be done after pygame.init()
        self.font = pygame.font.SysFont("comicsansms", self.fontSize)
        #set the window's caption
        pygame.display.set_caption("Snake: The Black Mamba Strikes Again")


    #function that fills the entire screen with white
    def fillWhite(self):
        self.display.fill(WHITE)

    #fuction that flips the display (updating all the changes)
    def flip(self):
        pygame.display.flip()

    #function that actually draws the snake blocks
    def drawSnake(self, blocksize, color, dims):
        pygame.draw.rect(self.display,color,[dims[0],dims[1],blocksize,blocksize])

    #function that displays text to the first designated message area
    def message(self, color, message):
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 0])

    #function that displays text to the second designated message area
    def message2(self, color, message):
        #kobeText = "Kobe Would be so proud"
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 15])

    #function that displays text to the third designated message area
    def message3(self, color, message):
        #jokeText = random.choice(self.jokes)
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 30])

    #function that displays text to the fourth designated message area
    def message4(self, color, message):
        text = self.font.render(message, True, color)
        self.display.blit(text, [0, 45])

    #function that draws the square (snake food) blocks
    def drawSquare(self, blocksize, color, dims):
        pygame.draw.rect(self.display,color,[dims[0],dims[1],blocksize,blocksize])
