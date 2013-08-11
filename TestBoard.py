import unittest

from SeaBattle import Position

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass
    
    def testPositive(self):
        self.assertTrue(True, "What?")
        
    def testNegative(self):
        self.assertTrue(False, "Failed as expected")
        
    def testGetRelativePosition(self):
        start = Position(0, 0)
        orientation = "East"
        end = start.getRelativePosition(1, orientation)
        end.printPosition()
        self.assertTrue(end.getRow() == 0 and end.getColumn() == 1)

if __name__ == '__main__':
    unittest.main()