from SeaBattle import Position, Boat, Utils, BoardCell

class Board:
    boats=[]
    def __init__(self, size):
        self.size = size
        self.grid = []                  
        for i in range (0, size):
            new = []
            for j in range (0, size):
                cell = BoardCell.BoardCell(i, j, False)
                new.append(cell)
            self.grid.append(new)
    
    

    def setupBoard(self, boatSizes):
        for i in boatSizes:
            self.addBoat(i)
        
        
    def addBoat(self, size):
        boat = Boat.Boat(size)
           
        while(1):
            # TODO: check for infinite loop, maybe check for all possible orientations for a given position?
            boat.randomizePosition(self.size)
            if self.canSetupBoat(boat.cells):
                break
        
        self.placeBoatInBoard(boat)
        self.boats.append(boat)
        
    
    def placeBoatInBoard(self, boat):
        for cell in boat.cells:
            self.grid[cell.getRow()][cell.getColumn()] = cell
    
    
    def canSetupBoat(self, positions):
        for position in positions:
            # TODO: check collisions
            if not self.isValidPosition(position):
                return False
        return True
        
    
    def getBoardInString(self):
        message=''
        message += ' \n'
        for i in range(self.size):
            message += ' ' * Utils.OFFSET
            for j in range(self.size):
                message =message + str(self.grid[i][j].toString()) + ' '
            message += '\n'
        message += '\n'
        return message
        
        
    def isAHit(self, hitPosition):
        for boat in self.boats:
            for cell in boat.cells:
                if hitPosition.getRow() == cell.getRow() and hitPosition.getColumn() == cell.getColumn():
                    # update the boat cell
                    cell.hit()
                    if(boat.isCaput()):
                        #Utils.tellUser( 'you sunk one of my boats!' )
                        pass
                    return True 
        return False
    
    
    def allBoatsSunk(self):
        """
        If all the boats are sunk, the game is over
        """
        for boat in self.boats:
            if not boat.isCaput():
                return False
        return True
            
            

    
    
    def isValidPosition(self, position):
        if Utils.isValidCoordinate(position.getRow(), self.size) and Utils.isValidCoordinate(position.getColumn(), self.size):
            if not self.grid[position.getRow()][position.getColumn()].getIsBoat():
                return True
        return False

    
    def getCellInPosition(self, position):
        return self.grid[position.getRow()][position.getColumn()]
    
    #TODO: maybe the board should not define the responseString
    def sendRocket(self, position):
        response = None
        cell = self.getCellInPosition(position)
        if (self.isAHit(cell)):
            response = 'Aaaargh you hit my boat'
        else:
            response = 'You hit Water sucker'
        cell.hit()
        return response
    