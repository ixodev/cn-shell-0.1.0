import socket, threading, sys

SERVER_HOST = sys.argv[2]
SERVER_PORT = sys.argv[3]

s = socket.socket()
print(f"Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("You are connected.")
name = input("Please enter your name: ")

def listen_msgs():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

thread = threading.Thread(target=listen_msgs, daemon=True)
thread.start()

while True:

    msg = input("Message to the server: ")

    if msg == "//quit": break

    s.send(msg.encode())

s.close()