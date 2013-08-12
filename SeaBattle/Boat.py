from SeaBattle import Utils, BoardCell

class Boat:
    """Represents a boat"""
    
    cells = []
    def __init__(self, size):
        self.size = size
        self.startCell = None
        self.endCell = None
    
        
    def setPositions(self, cells):
        self.cells = cells
    
    
    def randomizePosition(self,maxlimit):
        self.cells = []
        self.startCell = Utils.getRandomPosition(maxlimit)
        self.orientation = Utils.getRandomOrientation()
        for i in range(self.size):
            relativePosition = self.startCell.getRelativePosition(i, self.orientation)
            cell = BoardCell.BoardCell(relativePosition.getRow(), relativePosition.getColumn(), True)
            self.cells.append(cell)
    
    
    def isCaput(self):
        """
        If all cells of the boat are found, the boat is Sunk
        """
        for cell in self.cells:
            if not cell.getIsHit():
                return False
        return True