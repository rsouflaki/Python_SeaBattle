import random
import os

OFFSET = 10
counter = 0
board = None

class Board:
    boats=[]
    def __init__(self, size):
        self.size = size
        self.grid = [[0]*size for i in range(size)]
    
    
    #TODO: this should get an array of the boats it should construct
    def setupBoard(self):
        self.addBoat(3)
        
        
    def addBoat(self, size):
        boat = Boat(size)
        
        
        while(1):
            # TODO: check for infinite loop
            boat.startPosition = getRandomPosition()
            boat.orientation = getRandomOrientation()
            positions = []
            for i in range(size):
                positions.append(boat.startPosition.getRelativePosition(i, boat.orientation))
            if self.canSetupBoat(positions):
                boat.positions = positions[:]
                break
        self.boats.append(boat)
        
        
    def canSetupBoat(self, positions):
        for position in positions:
            # check collisions
            if not isValidPosition(position):
                return False
        return True
        
    
    def printBoard(self):
        print ' '
        for i in range(self.size):
            print ' ' * OFFSET,
            for j in range(self.size):
                print str(self.grid[i][j])+' ',
            print ''
        print ' '
        
        
    def isAHit(self, hitPosition):
        print 'You send your rocket in: ' + str(hitPosition.getRow()) + ',' + str(hitPosition.getColumn())
        print "There are: " + str(len(self.boats)) + " boats"
        for boat in self.boats:
            for position in boat.positions:
                print "Comparing hit position with boat position: " + str(position.getRow()) + ',' + str(position.getColumn())
                if hitPosition.getRow() == position.getRow() and hitPosition.getColumn() == position.getColumn():
                    return True 
        return False
    
    def canStillPlay(self):
        for boat in self.boats:
            for position in boat.positions:
                if (board.grid[position.getRow()][position.getColumn()]) == 2:
                    return False
        return True

class Position:
    """The position in the board"""
    
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getRelativePosition(self, size, orientation):
        endPosition = None
        if orientation == 'North':
            endPosition = Position(self.getRow() - size, self.getColumn())
        elif orientation == 'East':
            endPosition = Position(self.getRow(), self.getColumn() + size)
        elif orientation == 'South':
            endPosition = Position(self.getRow() + size, self.getColumn())
        elif orientation == 'West':
            endPosition = Position(self.getRow(), self.getColumn() - size)
        return endPosition
    
    def printPosition(self):
        print("Position is: " + str(self.getRow()) + "," + str(self.getColumn()))
        


        
class Boat:
    """Represents a boat"""
    
    positions = []
    def __init__(self, size):
        self.size = size
        self.startPosition = None
        self.endPosition = None

                
    def isValidBoat(self):
        if isValidPosition(self.endPosition):
            return True
        return False
            

def sendRocket(position):
    value = -1
    if (board.isAHit(position)):
        print 'Aaaargh you hit my boat'
        value = 2
    else:
        print 'You hit Water sucker'
        value = 1
    board.grid[position.getRow()][position.getColumn()] = value


def askUser():
    print 'Here is your board. You have tried: ' + str(counter) + ' times'
    board.printBoard()
    print 'send a rocket to which row'
    rocketRow = getPositionFromUser()
    
    print 'send a rocket to which column'
    rocketColumn = getPositionFromUser()
    
    os.system('cls') #on windows
    rocketPosition = Position(rocketRow, rocketColumn)
    sendRocket(rocketPosition)
    
def getPositionFromUser():
    while(1):
        pos = raw_input()
        if(pos.isdigit()):
            if isValidRange(int(pos)):
                return int(pos)
            
        print 'please enter a positive number between 0 and '+str(board.size-1)

def getRandomPosition():
    row = random.randint(0, board.size - 1)
    column = random.randint(0, board.size - 1)
    return Position(row, column)


def getRandomOrientation():
    orientation = {0:'North', 1:'East', 2:'South', 3:'West'}
    i = random.randint(0, 3)
    return orientation[i]



def isValidRange(num):
    if num >= 0 and num < board.size:
        return True
    return False
    
def isValidPosition(position):
    if isValidRange(position.getRow()) and     isValidRange(position.getColumn()):
        return True
    return False

    
board = Board(4)
if __name__ == '__main__': 
    #def playGame():        
    os.system('cls') #on windows
    board.setupBoard()
    while(board.canStillPlay()):
        askUser()
        counter += 1
    
    board.printBoard()


# TODO:
# Finish games when all boats are sunk
# add more boats
# AI opponent (stupid)
# Check if position is already tried

# OPTIONAL
# custom board size and amount of boats per board size  
# better display

