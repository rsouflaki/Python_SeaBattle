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
        

