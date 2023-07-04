import socket

host='localhost'
port=8080

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # establish TCP connection with server
mySocket.connect((host, port))     # bind host and port

message = mySocket.recv(1024)   # receive 1024 bytes of msg

# decode the message rcvd
while message:
    print(message.decode)
    message = mySocket.recv(1024)

mySocket.close()