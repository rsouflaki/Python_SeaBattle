from SeaBattle import Board, Boat, Position, Utils

import os


    

if __name__ == '__main__': 
    #def playGame():        
    os.system('cls') #on windows
    board = Board.Board(Utils.BOARDSIZE)
    board.setupBoard(Utils.BOATSIZES)
    while(board.canStillPlay()):
        Utils.askUser(board)
        Utils.counter += 1
    board.printBoard()
    print ' ' * Utils.OFFSET + 'GAME OVER'


# TODO:
# AI opponent (stupid)
# break ask user



# OPTIONAL
# better display

