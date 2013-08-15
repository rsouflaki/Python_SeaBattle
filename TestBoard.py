import unittest
from SeaBattle import Position, User, Utils

class TestBoard(unittest.TestCase):

    def setUp(self):
        pass
    
    def testPositive(self):
        self.assertTrue(True, "What?")
        
    #def testNegative(self):
    #    self.assertTrue(False, "Failed as expected")
        
    def testGetRelativePosition(self):
        start = Position.Position(0, 0)
        orientation = "East"
        end = start.getRelativePosition(1, orientation)
        end.printPosition()
        self.assertTrue(end.getRow() == 0 and end.getColumn() == 1)

    def testSinkAllBoats(self):
 
        userA = User.User("testUserA")
        boats = userA.board.boats
        for boat in boats:
            for cell in boat.cells:
                userA.board.sendRocket(cell)
        self.assertTrue(userA.isDefeated(), "User should have lost by now")

        
    def testGameLogic(self):
            
        userA = User.User("testUserA")
    
        userB = User.User("testUserB")
           
        while(1):
            rocketPositionA=Utils.getRandomPosition(Utils.BOARDSIZE)
            userA.sendRocket(rocketPositionA, userB)
            if(userB.isDefeated()):
                break
            
            rocketPositionB=Utils.getRandomPosition(Utils.BOARDSIZE)
            userB.sendRocket(rocketPositionB, userA)

            if(userA.isDefeated()):
                break
        self.assertTrue(userA.isDefeated() or userB.isDefeated(), 'Game should have finished now')
        
if __name__ == '__main__':
    unittest.main()    