# chat-app

The client-server application uses socket programming to communicate with eachother over TCP stream. The program uses Python's Tkinter library for a simple GUI. The broadcast of messages is done without a delay.
Connected clients are stored in dictionary data structure to be able to effectively broadcast messages.
Client can shutdown by clicking on Quit button, which also closes the chat window. Similarly, server is able to gracefully shutdown when there are no connected clients.

1. One server and multiple clients connected
   ![image](https://github.com/bhuvneet/chat-app/assets/78770635/74768467-2380-4cfb-82be-9d4cc40d7160)

2. Enter name to continue to chatroom
   ![image](https://github.com/bhuvneet/chat-app/assets/78770635/606041d4-236e-4959-b821-ffff30d6a8a2)

3. Broadcasting messages to all clients without delay
  ![image](https://github.com/bhuvneet/chat-app/assets/78770635/3b0c2908-e349-45c6-9258-2505ec1d5ee1)

4. Quitting program and broadcasting to other connected clients that the user has disconnected
   ![image](https://github.com/bhuvneet/chat-app/assets/78770635/866248f6-7f5e-42df-b2fd-3e863902ced2)


