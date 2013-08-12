from SeaBattle import Position

UNKNOWN = "0"
BOAT = "B"
WATER = "W"


class BoardCell(Position.Position):
    '''
    A Cell Board
    '''


    def __init__(self, row, column, isBoat):
        Position.Position.__init__(self, row, column)
        self.isBoat = isBoat
        self.isHit = False
        
    def getIsHit(self):
        return self.isHit
    
    def hit(self):
        self.isHit = True
    
    def getIsBoat(self):
        return self.isBoat
    
    def toString(self):
        '''
        If the cell is not hit it appears as Unknown
        Otherwise show water or boat
        '''
        if not self.isHit:
            return UNKNOWN
        
        if self.isBoat:
            return BOAT
        else:
            return WATER 