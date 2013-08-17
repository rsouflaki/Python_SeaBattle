from SeaBattle import Board, Utils, Position
import os

class User:
    def __init__(self, name, clientSocket):
        self.name = name
        self.board = Board.Board(Utils.BOARDSIZE)
        self.board.setupBoard(Utils.BOATSIZES)
        self.counter = 0
        self.clientSocket = clientSocket
            
    def getName(self):
        return self.name
    
    def tellUser(self, message):
        self.clientSocket.send(message)
        
    def getAttackPosition(self, opponent):
        rocketPosition = None
        self.tellUser(self.name + ' here is your opponent\'s board . You have tried: ' + str(self.counter) + ' times')
        boardInString = opponent.board.getBoardInString()
        self.tellUser(boardInString)
        while(1):
            self.tellUser('send a rocket to which row')
            rocketRow = self.getPositionFromUser(Utils.BOARDSIZE)  
            self.tellUser('send a rocket to which column')
            rocketColumn = self.getPositionFromUser(Utils.BOARDSIZE)
            rocketPosition = Position.Position(rocketRow, rocketColumn)
            cell = opponent.board.getCellInPosition(rocketPosition)
            if not cell.getIsHit():
                break
            self.tellUser('you already tried that sucker!')
        os.system('cls') #on windows
        return rocketPosition
    
    
    def sendRocket(self, rocketPosition, opponent):
        return opponent.board.sendRocket(rocketPosition)    
           
    def getPositionFromUser(self, boardSize):
        while(1):
            pos = self.clientSocket.recv(1024)
            if(pos.isdigit()):
                if self.board.isValidRange(int(pos)):
                    return int(pos)
                
            self.tellUser ('Invalid number, please enter a positive number between 0 and '+str(boardSize - 1))
            
    def isDefeated(self):
        return self.board.allBoatsSunk()
    
    def getPromptForAttack(self):
        prompt = self.name + ', here is your opponent\'s board. You have tried: ' + str(self.counter) + ' times'
        return prompt
    

    