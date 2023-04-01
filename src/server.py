import sys, socket, threading

try: PORT = sys.argv[2]
except:
    print("The syntax of the command is not correct.", file=sys.stderr)
    quit(0)

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", int(PORT)))
server.listen(5)

clients = []

print(f"Server listening on 0.0.0.0:{PORT}.")

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