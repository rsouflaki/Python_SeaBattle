from SeaBattle import Position, Utils, User
import socket
import os

def playTurn(attackUser, defendUser):
    # ask attacker for input
    inputPrompt = attackUser.getPromptForAttack()
    sendMessageToUser(attackUser.clientSocket, inputPrompt)
    boardStr = defendUser.board.getBoardInString()
    sendMessageToUser(attackUser.clientSocket, boardStr)
    cell = None
    while(1):
        responseRow = getUserCoordinate(attackUser, 'row')
        responseColumn = getUserCoordinate(attackUser, 'column')
        rocketPosition = Position.Position(responseRow, responseColumn)
        
        # check if cell is tried
        cell = defendUser.board.getCellInPosition(rocketPosition)
        if not cell.getIsHit():
            break    
        sendMessageToUser(attackUser.clientSocket, 'you already tried that sucker!')
    
    # update defender's board
    responseString = attackUser.sendRocket(rocketPosition, defendUser)
    
    # send response to attacker
    sendMessageToUser(attackUser.clientSocket, responseString)
    
    # resend the defender's board
    boardStr = defendUser.board.getBoardInString()
    sendMessageToUser(attackUser.clientSocket, boardStr)
    

def getUserCoordinate(user, coordinateName):
    response = None
    while(1):
        sendMessageToUser(user.clientSocket, 'send a rocket to which ' + coordinateName)
        response = getMessageFromUser(user.clientSocket)
        if response.isdigit():
            if Utils.isValidCoordinate(int(response), Utils.BOARDSIZE):
                break;
        sendMessageToUser(user.clientSocket, 'Invalid input, please enter a positive number between 0 and ' + str(Utils.BOARDSIZE - 1))
    return int(response)
        
def sendMessageToUser(socket, message):
    socket.send(message)

def getMessageFromUser(socket):
    return socket.recv(1024)

def notifyEndOFGame(winner, loser):
    sendMessageToUser(winner.clientSocket, "You win the Game")
    sendMessageToUser(loser.clientSocket, "You lose, stinking loser")
            
if __name__ == '__main__': 
    #def playGame():        
    os.system('cls') #on windows

#Adding connectivity
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    clientSockets = []
    s.listen(2)
    names = []                 # Now wait for client connection.
#Accept connections from 2 users and ask for names
    for i in range(2):
        c, addr = s.accept()     # Establish connection with client.
        clientSockets.append(c)
        print 'Got connection from', addr
        clientSockets[i].send('Thank you for connecting to SeaBattle server :) \n\n\n\nEnjoy the game!')
        clientSockets[i].send('input name for player ' + str(i))      
        clientSockets[i].send('Please wait for the second player to connect')
        names.append( clientSockets[i].recv(1024))

#Create the users    
    userA = User.User(names[0],clientSockets[0])
    userB = User.User(names[1],clientSockets[1])
    
    userA.tellUser(' you will be playing against ' + userB.getName())
    userB.tellUser(' you will be playing against ' + userA.getName())
    
    while(1):
        playTurn(userA, userB)
        if(userB.isDefeated()):
            notifyEndOFGame(userA, userB)
            break
        playTurn(userB, userA)
        if(userA.isDefeated()):
            notifyEndOFGame(userB, userA)
            break

#Closing all opened clients        
    for client in clientSockets:
        client.send('Closing connection')
        client.close()


# TODO:
# AI opponent (stupid)
# Network 
# Graphics
# User should be able to place his own boats
# Response should notify if a boat is sunk


# OPTIONAL
# better display

