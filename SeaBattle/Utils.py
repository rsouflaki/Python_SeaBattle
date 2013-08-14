import random
import os
from SeaBattle import Position

BOARDSIZE = 10
OFFSET = 10
counter = 0
BOATSIZES = [5, 4, 3 ,3, 2]



def tellUser(question):
    print question

def getReply():
    return raw_input()    

def play(board):
    tellUser ( 'Here is your board. You have tried: ' + str(counter) + ' times' )
    board.printBoard() 
    while(1):
        tellUser('send a rocket to which row')
        rocketRow = getPositionFromUser(board)  
        tellUser('send a rocket to which column')
        rocketColumn = getPositionFromUser(board)
        rocketPosition = Position.Position(rocketRow, rocketColumn)
        cell = board.getCellInPosition(rocketPosition)
        if not cell.getIsHit():
            break
        tellUser('you already tried that sucker!')
    os.system('cls') #on windows
    board.sendRocket(rocketPosition)
    
def getPositionFromUser(board):
    while(1):
        pos = raw_input()
        if(pos.isdigit()):
            if board.isValidRange(int(pos)):
                return int(pos)
            
        tellUser ('please enter a positive number between 0 and '+str(board.size - 1))

def getRandomPosition(maxlimit):
    row = random.randint(0, maxlimit - 1)
    column = random.randint(0, maxlimit - 1)
    return Position.Position(row, column)


def getRandomOrientation():
    orientation = {0:'North', 1:'East', 2:'South', 3:'West'}
    i = random.randint(0, 3)
    return orientation[i]