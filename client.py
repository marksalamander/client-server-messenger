from socket import *
from threading import Thread
import ssl

SERVER_NAME = ''
SERVER_PORT = 8080

client_socket = socket(AF_INET, SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# SSL socket made from client_socket
ssl_client_socket = context.wrap_socket(client_socket, server_hostname="")
ssl_client_socket.connect((SERVER_NAME,SERVER_PORT))

name = input("Enter your name: ")

# Continuosly listens for messages from other clients
def listen_for_messages():
    while True:
        message = ssl_client_socket.recv(1024).decode()
        print("\n" + message)

# Thread that listens for messages & prints them
t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

print("Enter your message ('q' to quit): ")

# User sends message to server while true
while True:
    message = input()
    if message == 'q':
        break
    message = f'{name}{": "}{message}'
    ssl_client_socket.send(message.encode())

ssl_client_socket.close()
client_socket.close()