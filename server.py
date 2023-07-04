import socket

host='localhost'
port=8080

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # establish TCP connection with server
mySocket.bind((host, port))     # bind host and port

mySocket.listen() # keep listening for connections
connection, address = mySocket.accept()

message = "connection successful..."
connection.send(message.encode())    # send encoded message to connection

connection.close()