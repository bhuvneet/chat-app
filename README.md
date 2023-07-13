# chat-app

The client-server application uses socket programming to communicate with each other over a TCP stream. The program uses Python's Tkinter library for a simple GUI. The broadcast of messages is done without delay.
Connected clients are stored in the dictionary data structure to be able to broadcast messages effectively.
The client can shut down by clicking on the Quit button, which also closes the chat window. Similarly, a server is able to gracefully shut down when there are no connected clients.

1. One server and multiple clients connected
   ![image](https://github.com/bhuvneet/chat-app/assets/78770635/0dc21c4f-c5eb-4598-95bd-b1cf1abc901e)

2. Enter your name to continue to the chatroom
   ![image](https://github.com/bhuvneet/chat-app/assets/78770635/9a78d561-63f6-4f37-8a4b-13df3c860bbb)

3. Broadcasting messages to all clients without delay
  ![image](https://github.com/bhuvneet/chat-app/assets/78770635/586f8791-10a1-45be-adfe-5a37a44f94c1)

4. Quitting the program and broadcasting to other connected clients that the user has disconnected
   ![image](https://github.com/bhuvneet/chat-app/assets/78770635/658d0924-a81e-4559-b405-d9b0e7536ade)



