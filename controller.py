#the Project's controller
import pygame
import view
import snake
import square

#Global Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 120, 0)
SCREENWIDTH = 900
SCREENHEIGHT = 500
SQUARESIZE = 10
SNAKESIZE = 10
FPS = 30
CLOCK = pygame.time.Clock()

def destroy():
    pygame.quit()
    quit()

def make_snake(view, mod):
    for cords in mod.snakelist:
        view.drawSnake(mod.blockSize, GREEN, (cords[0], cords[1]))

def main():
    mamba = snake.Snake((SCREENWIDTH, SCREENHEIGHT), SNAKESIZE)
    vis = view.View(mamba.boardSize)
    food = square.Square((SCREENWIDTH, SCREENHEIGHT), SQUARESIZE)

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
                if(event.key == pygame.K_UP):
                    mamba.up()
                elif(event.key == pygame.K_DOWN):
                    mamba.down()
                elif(event.key == pygame.K_LEFT):
                    mamba.left()
                elif(event.key == pygame.K_RIGHT):
                    mamba.right()

        #Logic Loop:
        if (mamba.xcord >= mamba.boardSize[0] or mamba.xcord < 0 or mamba.ycord >= mamba.boardSize[1] or mamba.ycord < 0):
            menu = True

        mamba.xcord += mamba.xchange
        mamba.ycord += mamba.ychange

        vis.drawSquare(SQUARESIZE, RED, (food.xcord, food.ycord))

        mamba.snakehead = []
        mamba.snakehead.append(mamba.xcord)
        mamba.snakehead.append(mamba.ycord)
        mamba.snakelist.append(mamba.snakehead)

        if (len(mamba.snakelist) > mamba.snakelength):
            del mamba.snakelist[0]

        if (mamba.snakehead in mamba.snakelist[:-1]):
            menu = True

        make_snake(vis, mamba)

        vis.flip()

        if (mamba.xcord == food.xcord and  mamba.ycord == food.ycord):
            food.resetSquareCoords(SQUARESIZE)
            mamba.snakelength += 1

        CLOCK.tick(FPS)


    destroy()

main()
