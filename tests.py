import snake
import square

SAMPLE_BOARD_SIZE = (200, 200)

print("##### Testing Models #####")
tSnake = snake.Snake(SAMPLE_BOARD_SIZE)
tSquare = square.Square(SAMPLE_BOARD_SIZE)

print("Models have been instantiated: ")
print("tSnake (test Snake): \n", tSnake)
print("tSquare (test Square): \n", tSquare)
print("##### End Testing Models #####")
print()

print("##### Testing Standart Input #####")
print("Snake object being placed at center of board. Board Size: " + str(SAMPLE_BOARD_SIZE))
print(tSnake)
print() #empty print statement to generate a new line
print("Square object being placed at random cooardinates in board. Borad Size: " + str(SAMPLE_BOARD_SIZE))
print(tSquare)
print("##### End Testing Standart Input #####")
print()

print("##### Testing Different Snake Placements #####")

#tSnake.moveRight()
#print(tSnake)

#tSnake.moveLeft()
#print(tSnake)

#tSnake.moveUp()
#print(tSnake)

tSnake.moveDown()
print(tSnake)

#ALL OF THE ABOVE METHODS CANNOT BE CALLED SIMULTANEOUSLY OR THEY WILL STOP EACH OTHER FROM RUNNING

print("##### End Testing Different Snake Placements #####")
print()

print("##### Testing Getter functions #####")
print("snake xcor - " + str(tSnake.getXCor()))
print("snake y cor - " + str(tSnake.getYCor()))


print("square x cor - " + str(tSquare.getXCor()))
print("square y core - " + str(tSquare.getYCor()))

print("##### End Testing Getter Functions #####")
print()

print("##### Testing Grow Function #####")
tSnake.grow()
print("snake length - " + str(tSnake.getLength()))
print("##### End Testing Grow Function #####")
print()
print("##### End of Testing #####")
