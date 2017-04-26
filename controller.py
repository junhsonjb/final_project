#the Project's controller
import pygame
import view
import snake
import square
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)
screenWidth = 900
screenHeight = 500
squareSize = 10
snakeSize = 10
def destroy():
    pygame.quit()
    quit()
def snake(view,mod):
    for cords in mod.snakelist:
        view.drawSnake(mod.blockSize,green, (cords[0],cords[1]))

def main():
    mamba = snake.Snake((screenWidth,screenHeight),snakeSize)
    vis = view.View(mamba.boardSize)
    food = square.Square((screenWidth,screenHeight),squareSize)

    leaveGame = False
    menu = False
    mamba.snakelist = []
    mamba.snakelength = 1

    while (not leaveGame):
        vis.fillWhite()

        while(menu):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    leaveGame = True
                    menu = False

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                menu = True
            elif(event.type == pygame.KEYDOWN):
                if(event.key = pygame.K_UP):
                    mamba.up()
                elif(event.key == pygame.K.DOWN):
                    mamba.down()
                elif(event.key == pygame.K_LEFT):
                    mamba.left()
                elif(event.key == pygame.K_RIGHT):
                    mamba.right()




    destroy()
