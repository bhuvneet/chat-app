import socket
import time
import tkinter
from tkinter import *
from threading import Thread

def receive():
    while True:
        try:
            message = mySocket.recv(1024).decode("utf8")
            message_list.insert(tkinter.END,message)
            if message == "quitting chatroom...":
                shutdown_app()
        except ConnectionError:
            break    # add errno to display msg
            
def send():
    message = my_message.get()
    my_message.set(" ")  # enables typing of new msgs
    mySocket.send(bytes(message, "utf8"))

def shutdown_app():
    time.sleep(5)
    mySocket.close()    #close socket
    window.destroy()      #close chat window

def on_closing():
    my_message.set("quit")
    send()
    
window = Tk()   # window for chat-app
window.title("MyChat")
window.configure(bg="lightyellow")

message_frame = Frame(window, height=50, width=50, bg="lightgrey")
message_frame.pack()    # to adjust window according to the msg frame

my_message = StringVar()
my_message.set("")

scroll_bar = Scrollbar(message_frame)
message_list = Listbox(message_frame, height=15, width=65, bg="lightgrey", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
message_list.pack(side=LEFT, fill=BOTH)
message_list.pack()

label = Label(window, text="Enter message: ", fg='blue', font='Arial', bg="lightyellow")
label.pack()

entry_field = Entry(window, textvariable=my_message, fg="black", width=50)
entry_field.pack()

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

greetingMsg = 0

#responsible for all kinds of events
mainloop()
