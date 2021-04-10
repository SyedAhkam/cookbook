# Requires the `socket` module (stdlib)
import socket

# Define host and port constants
HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 3103 # The port used by the server

# Create a socket instance
# socket(family=FAMILY, type=TYPE, proto=PROTOCOL, fileno=FILENO)
# socket.AF_INET is the address family for ipv4
# socket.SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # Connect to an existing socket server
   
    while True:
        message = bytes(input(">> "), 'utf-8')

        s.sendall(message) # Send some data

        data = s.recv(1024) # Recieve response

        print(f'Received From Server: {data}')
