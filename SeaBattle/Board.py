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
        
    
    def printBoard(self):
        print ' '
        for i in range(self.size):
            print ' ' * Utils.OFFSET,
            for j in range(self.size):
                print str(self.grid[i][j].toString()) + ' ',
            print ''
        print ' '
        
        
    def isAHit(self, hitPosition):
        print 'You send your rocket in: ' + str(hitPosition.getRow()) + ',' + str(hitPosition.getColumn())
        for boat in self.boats:
            for cell in boat.cells:
                if hitPosition.getRow() == cell.getRow() and hitPosition.getColumn() == cell.getColumn():
                    # update the boat cell
                    cell.hit()
                    if(boat.isCaput()):
                        print 'you sunk one of my boats!'
                    return True 
        return False
    
    
    def canStillPlay(self):
        """
        If all the boats are sunk, the game is over
        """
        for boat in self.boats:
            if not boat.isCaput():
                return True
        return False
            
            
    def isValidRange(self, num):
        if num >= 0 and num < self.size:
            return True
        return False
    
    
    def isValidPosition(self, position):
        if self.isValidRange(position.getRow()) and self.isValidRange(position.getColumn()):
            if not self.grid[position.getRow()][position.getColumn()].getIsBoat():
                return True
        return False
    
    
    def getCellInPosition(self, position):
        return self.grid[position.getRow()][position.getColumn()]
    
    
    def sendRocket(self, position):
        cell = self.getCellInPosition(position)
        if (self.isAHit(cell)):
            print 'Aaaargh you hit my boat'
        else:
            print 'You hit Water sucker'
        cell.hit()
    