import socket
class server:
    def __init__(self):
        pass
    
        self.socket=socket.socket()         # Create a socket object
        self.host = socket.gethostname() # Get local machine name
        self.port = 12345                # Reserve a port for your service.
        
    def startServer(self):    
        self.socket.bind(self.host, self.port)        # Bind to the port
        self.socket.listen(2)
        
        while(1):
            clientSocket, addr = self.socket.accept()     # Establish connection with client.
            print 'Got connection from', addr
            #create a randomNumber to identify the USERID
            clientSocket.send('Connection accepted: UID')  
            

        