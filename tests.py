import snake
import square

def main():
    print("##### SNAKE MODEL TESTING #####")
    kobe = snake.Snake((900, 500),10)
    print("Initial snake length:", kobe.snakelength)
    print("init x change:", kobe.xchange)
    print("init y change:", kobe.ychange)
    print("init x cord:", kobe.xcord)
    print("init y cord:", kobe.ycord)
    kobe.up()
    print("x change after up movement:", kobe.xchange)
    print("y change after up movement:", kobe.ychange)
    kobe.down()
    print("x change after down movement:", kobe.xchange)
    print("y change after down movement:", kobe.ychange)
    kobe.left()
    print("x change after left movement:", kobe.xchange)
    print("y change after left movement:", kobe.ychange)
    kobe.right()
    print("x change after right movement:", kobe.xchange)
    print("y change after right movement:", kobe.ychange)

    print("##### SQUARE MODEL TESTING #####")
    food = square.Square((900, 500), 10)
    print("init food x cord:", food.xcord)
    print("init food y cord:", food.ycord)
    food.resetSquareCoords(10)
    print("food x cord after resetting:", food.xcord)
    print("food y cord after resetting:", food.ycord)


main()
