from SeaBattle import Board, Boat, Position, Utils, User

import os


    

if __name__ == '__main__': 
    #def playGame():        
    os.system('cls') #on windows
    Utils.tellUser ('Select 1 or 2 players') 
    reply = ''
    while reply != '1' and reply != '2':
        reply = raw_input()

    if reply == '1':
            
        userA = User.User(Utils.BOARDSIZE)
        userA.board.setupBoard(Utils.BOATSIZES)
        while(userA.board.canStillPlay()):
            Utils.play(userA.board)
            Utils.counter += 1
        userA.board.printBoard()
        Utils.tellUser( ' ' * Utils.OFFSET + 'GAME OVER')


# TODO:
# AI opponent (stupid)
# break ask user



# OPTIONAL
# better display

