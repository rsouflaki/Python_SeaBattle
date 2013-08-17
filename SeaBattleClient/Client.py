import socket



    

if __name__ == '__main__': 
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                # Reserve a port for your service.
    
    s.connect((host, port))
    while(1):
        message = s.recv(1024)
        print message
        if ('send a rocket to' in message or 'input name for player' in message):
            s.send(raw_input())    
    
    s.close                     # Close the socket when done