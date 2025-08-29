# Secure Client-Server Messenger
Project made for Data Communications course (COSC350).

This is a simple **client-server messenger application** that allows multiple clients to communicate securely over a network. The messages are encrypted using **SSL/TLS** to ensure privacy and security.

The program consists of two parts:
- **client.py**: The client-side application where users can send and receive messages.
- **server.py**: The server-side application that handles multiple client connections and broadcasts messages to all connected clients.

---

## Features
- **SSL Encryption**: Communication between the client and the server is encrypted using SSL/TLS for security.
- **Real-time Messaging**: Clients can send and receive messages in real-time.
- **Multiple Clients Support**: The server can handle multiple clients simultaneously.
- **Threaded Messaging**: The client and server use threads to allow continuous listening and message handling.

---

## Requirements

- Python 3.x
- `ssl` module (built-in in Python)
- A valid **server certificate** (`server-cert.pem`) and **private key** (`server-key.pem`) for the server.

---

## How It Works

1. **Server**:
   - Listens for incoming client connections on port `8080`.
   - Once a client connects, it wraps the connection in an SSL context.
   - Listens for messages from each client and broadcasts them to all connected clients.
   - Runs each client handler in a separate thread to support multiple clients.

2. **Client**:
   - Connects to the server over SSL.
   - Continuously listens for incoming messages from the server while allowing the user to send messages.
   - Supports sending messages and quitting by typing `'q'`.
