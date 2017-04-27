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
INCREASE_BY = 1
CLOCK = pygame.time.Clock()

def destroy():
    pygame.quit()
    quit()

def make_snake(view, mod):
    for cords in mod.snakelist:
        view.drawSnake(mod.blockSize, GREEN, (cords[0], cords[1]))

def message(font_obj, disp, color, msg):
    text = font_obj.render(msg, True, color)
    disp.blit(text, [SCREENWIDTH / 2, SCREENHEIGHT / 2])

def main():
    mamba = snake.Snake((SCREENWIDTH, SCREENHEIGHT), SNAKESIZE)
    vis = view.View(mamba.boardSize)
    food = square.Square((SCREENWIDTH, SCREENHEIGHT), SQUARESIZE)


    start = True
    hardmode = False
    leaveGame = False
    menu = False
    score = 1
    mamba.snakelist = []
    mamba.snakelength = 1

    #Main Game Loop (when this stops the whole game is over -- the program stops running)
    while (not leaveGame):
        vis.fillWhite()

        #loop for starting screen
        while (start):
            hardmode = False
            startText = "Welcome to Snake! Press Space to begin. Q to quit"
            message(vis.font, vis.display, RED, startText)
            vis.flip()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    destroy()
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        start = False
                    elif (event.key == pygame.K_q):
                        start = False
                        leaveGame = True

        while(menu):

            menuText = "Game Over. Score: " + str(score) + " "
            menuText += "Press C to play again and Q to quit and H for hard mode"
            message(vis.font, vis.display, RED, menuText)
            vis.flip()

            #menu event loop
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    destroy()
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_c):
                        main()
                    elif (event.key == pygame.K_q):
                        leaveGame = True
                        menu = False
                    elif (event.key == pygame.K_h):
                        menu = False
                        hardmode = True

        #hard mode loop #UNDER CONSTRUCTION
        # while (hardmode):
        #
        #     #hard mode state event loop
        #     for event in pygame.event.get():
        #         if (event.type == pygame.QUIT):
        #             destroy()
        #         elif(event.type == pygame.KEYDOWN):
        #             if(event.key == pygame.K_UP):
        #                 mamba.d_up()
        #             elif(event.key == pygame.K_DOWN):
        #                 mamba.d_down()
        #             elif(event.key == pygame.K_LEFT):
        #                 mamba.d_left()
        #             elif(event.key == pygame.K_RIGHT):
        #                 mamba.d_right()
        #
        #     #Logic Loop:
        #     if (mamba.xcord >= mamba.boardSize[0] or mamba.xcord < 0 or mamba.ycord >= mamba.boardSize[1] or mamba.ycord < 0):
        #         menu = True
        #
        #     mamba.xcord += mamba.xchange
        #     mamba.ycord += mamba.ychange
        #
        #     vis.drawSquare(SQUARESIZE, RED, (food.xcord, food.ycord))
        #
        #     mamba.snakehead = []
        #     mamba.snakehead.append(mamba.xcord)
        #     mamba.snakehead.append(mamba.ycord)
        #     mamba.snakelist.append(mamba.snakehead)
        #
        #     if (len(mamba.snakelist) > mamba.snakelength):
        #         del mamba.snakelist[0]
        #
        #     if (mamba.snakehead in mamba.snakelist[:-1]):
        #         menu = True
        #
        #     make_snake(vis, mamba)
        #
        #     vis.flip()
        #
        #     if (mamba.xcord == food.xcord and  mamba.ycord == food.ycord):
        #         food.resetSquareCoords(SQUARESIZE)
        #         mamba.snakelength += INCREASE_BY
        #         score += INCREASE_BY
        #
        #     CLOCK.tick(FPS)
        #

        #Game State event loop
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                destroy()
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
            mamba.snakelength += INCREASE_BY
            score += INCREASE_BY

        CLOCK.tick(FPS)



    destroy()

main()
