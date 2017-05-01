#the Project's controller
import pygame
import view
import snake
import square
import json
import random

#CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 120, 0)
BLUE = (0, 0, 155)
SCREENWIDTH = 900
SCREENHEIGHT = 500
SQUARESIZE = 10
SNAKESIZE = 10
INCREASE_BY = 5
CLOCK = pygame.time.Clock()

#function to end the entire program
def destroy():
    pygame.quit()
    quit()
#function that handles the game's paused state
def pause(view):
    paused = True
    while (paused):

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                destroy()
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_q):
                    destroy()
                elif (event.key == pygame.K_c):
                    paused = False

#function that handles the start screen and pre-game screen
def intro(view):

    start = True
    while (start):
        view.fillWhite()

        hardmode = False #to begin with, hardmode is disabled
        startText = "Welcome to Snake! Press Space to begin. P to pause. Q to quit"
        view.message(RED, startText)
        view.flip()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                destroy()
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    start = False
                elif (event.key == pygame.K_q):
                    destroy()

#function that accesses view and model to draw the snake to the screen
def make_snake(view, mod):
    for cords in mod.snakelist:
        view.drawSnake(mod.blockSize, GREEN, (cords[0], cords[1]))

#function that reads current high score from scores.txt file and saves it to a variable
def highscore():
    fptr = open("scores.txt", "r")
    data = int( fptr.read() )
    fptr.close()
    return data

#function that sets the new high score
def newhighscore(new):
    fptr = open("scores.txt", "w")
    fptr.write( str(new) )
    fptr.close()

#function that checks new high score and sets it in the scores.txt file
def setscore(score):
    high = highscore()

    if (score > high):
        newhighscore(score)

    high = highscore()
    return high

#function that displays the current score during the game
def showscore(score, view):
    text = view.font.render("Score: " + str(score), True, BLACK)
    view.display.blit(text, [0, 0])

#function that prints some simple text to the screen
def gametext(view, mod):
    text = view.font.render("Press C to continue. P to pause. Q to quit", True, BLACK)
    view.display.blit(text, [0, 15])

#main game function
def main():
    mamba = snake.Snake((SCREENWIDTH, SCREENHEIGHT), SNAKESIZE) #the snake object
    vis = view.View(mamba.boardSize) #the veiw object
    food = square.Square((SCREENWIDTH, SCREENHEIGHT), SQUARESIZE)#the object of the square that the snake eats/collides with
    joke = random.choice(vis.jokes) #a random joke from the view class to display on Game Over Screen

    fps = 30 #Frames per second
    start = True #boolean for start state
    hardmode = False #boolean for hard mode
    leaveGame = False #primary boolean to keep game running (stops when True)
    menu = False #boolean to keep menu state running
    score = 1 #Every player's starting score (since you have to start at one block)
    mamba.snakelist = [] #the list of the coordinates of each body part of the snake [[x, y], [x, y], [x, y]]
    mamba.snakelength = 1 #the maximum length that the snake can be

    #use the into function to run some start code that will only run once
    intro(vis)

    #Main Game Loop (when this stops the whole game is over -- the program stops running)
    while (not leaveGame):
        vis.fillWhite()

        #Loop for the Menu State, which is accessed when a player loses a round
        while(menu):
            #set the new high score and save it to be referred to later
            high = setscore(score)

            #display the Game Menu Text notifying player of score and how to restart
            menuText = "Game Over. Score: " + str(score) + " "
            menuText += "Press C to play again and Q to quit"# and H for hard mode
            vis.message(RED, menuText)

            #notify user of the high score
            msg = "High Score - " + str(high) + "!"
            vis.message2(RED, msg)

            #notify the user of reaching high score
            if (score == high):
                vis.message3(BLUE, "You reached the high score! Kobe Would be so proud")
            #or encouraging them to keep on playing
            else:
                vis.message3(BLUE, "You didn't reach the high score, but keep trying")

            #display a random nice little snake (or kobe) related joke
            vis.message4(GREEN, joke)

            #flip the screen using a flip function made in the view code
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
                        hardmode = True
                        print("hmode is true")

        #Game State event loop
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                destroy()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    mamba.up()
                elif(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    mamba.down()
                elif(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    mamba.left()
                elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    mamba.right()
                elif(event.key == pygame.K_p):
                    pause(vis)

        #Logic Loop:

        #if the snake is outside of the bounds of the window, end that round
        if (mamba.xcord >= mamba.boardSize[0] or mamba.xcord < 0 or mamba.ycord >= mamba.boardSize[1] or mamba.ycord < 0):
            menu = True

        #with each iteration of the loop, add the xchange and ychange values
        # to the current x and y coordinates to simulate a moving image
        mamba.xcord += mamba.xchange
        mamba.ycord += mamba.ychange

        #draw the snake's food in random x and y coordinates
        vis.drawSquare(SQUARESIZE, RED, (food.xcord, food.ycord))

        #reset the x, y list of the the snake head's coordinates
        mamba.snakehead = []
        #append the x and y values to snakehead
        mamba.snakehead.append(mamba.xcord)
        mamba.snakehead.append(mamba.ycord)
        #append snakehead ([x,y]) to snakelist (which will not be reset within the loop)
        mamba.snakelist.append(mamba.snakehead)

        #if the amount of lists in snakelist is less than snakelength,
        #remove the first (least recent) element in the list
        if (len(mamba.snakelist) > mamba.snakelength):
            del mamba.snakelist[0]

        #if the snakehead coordinates math any of the coordinates of any
        #snake body part, end that round
        if (mamba.snakehead in mamba.snakelist[:-1]):
            menu = True

        #run the function that draws all the snake body parts,
        #now that the amount to draw has been verified
        make_snake(vis, mamba)

        #print the score to the screen
        showscore(score, vis)

        #print some other text to the screen
        gametext(vis, mamba)

        #flip the screen, so that all the changes are shown
        vis.flip()

        #if the snake head touches the food, move the square,
        #increase the snake, and increase the player's score
        if (mamba.xcord == food.xcord and  mamba.ycord == food.ycord):
            food.resetSquareCoords(SQUARESIZE)
            mamba.snakelength += INCREASE_BY
            score += INCREASE_BY

        #if hardmode is set to True, make the snake move faster
        if (hardmode == True):
            fps = 30
        CLOCK.tick(fps)



    destroy() #end the program once the primary game loop ends

main() #run the main function
