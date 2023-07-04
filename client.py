import socket
from tkinter import *
from threading import Thread

window = Tk()   # window for chat-app
window.title("MyChat")
window.configure(bg="lightyellow")
message_frame = Frame(window, height=100, width=100, bg="lightgrey")
message_frame.pack()    # to adjust window according to the msg frame

my_message = StringVar()
my_message.set("")

scroll_bar = Scrollbar(message_frame)
message_list = Listbox(message_frame, height=50, width=100, bg="white", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
message_list.pack(side=LEFT, fill=BOTH)
message_list.pack()

label = Label(window, text="Enter message: ", fg='blue', font='Arial', bg="white")
label.pack()
entry_field = Entry(window, textvariable=my_message, fg="black", width=50)

send_button = Button(window, text="Send", font="Arial", fg="black", command=send)
send_button.pack()

quit.Button = Button(window, text="Quit", font="Arial", fg="black", command=on_closing)
quit.Button.pack()

host='localhost'
port=8080

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # establish TCP connection with server
mySocket.connect((host, port))     # bind host and port

rcv_thread = Thread(target=receive)
rcv_thread.start()

#responsible for all kinds of events
mainloop()

"""
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
"""