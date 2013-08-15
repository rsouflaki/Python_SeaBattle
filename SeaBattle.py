from SeaBattle import Board, Boat, Position, Utils, User

import os


    

if __name__ == '__main__': 
    #def playGame():        
    os.system('cls') #on windows
    print 'input name for player 1'

    name = raw_input()
    userA = User.User(name)

    print 'input name for player 2'
    nameB = raw_input()
    userB = User.User(nameB)

    
    while(1):
        rocketPositionA = userA.getAttackPosition(userB)
        userA.sendRocket(rocketPositionA, userB)
        userB.board.printBoard()
        if(userB.isDefeated()):
            Utils.tellUser( ' ' * Utils.OFFSET + 'Player ' + userA.getName() + 'won! GAME OVER')
            break
        
        rocketPositionB = userB.getAttackPosition(userA)
        userB.sendRocket(rocketPositionB, userA)
        userA.board.printBoard()
        if(userA.isDefeated()):
            Utils.tellUser( ' ' * Utils.OFFSET + 'Player ' + userB.getName() + 'won! GAME OVER')
            break
        


# TODO:
# AI opponent (stupid)
# Network 
# Graphics
# User should be able to place his own boats



# OPTIONAL
# better display

