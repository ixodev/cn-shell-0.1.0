import socket, sys, threading

ADDRESS, PORT = sys.argv[2], sys.argv[3]

s = socket.socket()
s.connect((str(ADDRESS), int(PORT)))

name = input("Name: ")

def listen():
    while True:
        msg = s.recv(1024).decode()
        print(msg)

t = threading.Thread(target=listen, daemon=True)
t.start()

while True:
    message =  input("Message:")
    if message == "/quit": break
    s.send(message.encode())

s.close()