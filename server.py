import socket
from threading import Thread

host='localhost'
port=8080

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # establish TCP connection with server
mySocket.bind((host, port))     # bind host and port

# using dictionary to store clients
connectedClients={}
clientAddresses={}

def accept_connection():
    while True:
        client_connection, client_address = mySocket.accept()
        print(client_address, " has connected!")
        client_connection.send("Welcome to iChat. Please enter your name".encode('utf8'))
        clientAddresses[client_connection]=client_address   # store client object and address in dictionary 

if __name__=="__main__":
    mySocket.listen(10)
    print("server listening to client reqs")
    
    # by using threads, the server can handle multiple clients
    serverThread = Thread(target=accept_connection)
    serverThread.start()
    serverThread.join() # join function lets multiple executions to take place at once