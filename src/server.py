import sys, socket, threading

try: HOSTNAME, PORT = sys.argv[2], sys.argv[3]
except:
    print("The syntax of the command is not correct.", file=sys.stderr)
    quit(0)

server = socket.socket()
server.bind((str(HOSTNAME), int(PORT)))
server.listen(5)

clients = []

print(f"Server listening on {HOSTNAME}:{PORT}.")

def listen() -> None:
    while True:
        client, client_adress = server.accept()
        for client in clients:
            try: msg = client.recv(1024).decode()
            except:
                print("One client left the server.")
                clients.remove(client)
            else: client.send(msg.encode())




thread = threading.Thread(target=listen, args=(), daemon=True)
thread.start()