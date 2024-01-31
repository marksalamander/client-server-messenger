from socket import *
from threading import Thread
import ssl

SERVER_HOST = ''
SERVER_PORT = 8080

client_sockets = set()
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((SERVER_HOST,SERVER_PORT))
s.listen(5)
print ('The server is ready to receive')

# This function keeps listening for a message from `cs` socket.
# When a message is received it is sent to all other clients.
def listen_for_client(cs):
    while True:
        try:
            message = cs.recv(1024).decode()
            if not message:
                # Removes client after they disconnect
                client_sockets.remove(cs)
                break
            print(message)

        except Exception as e:
            print(f"Error occurred: {e}")
            client_sockets.remove(cs)
            break

        # iterates over all connected sockets
        for client_socket in client_sockets:
            client_socket.send(message.encode())

# Continuosly listens for new connections
while True:
    connectionSocket, addr = s.accept()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="./server-cert.pem", keyfile="./server-key.pem")
    ssl_connection = context.wrap_socket(connectionSocket, server_side=True)
    client_sockets.add(ssl_connection)

    t = Thread(target=listen_for_client, args=(ssl_connection,))
    t.daemon = True
    t.start()

