# Requires the `socket` module (stdlib)
import socket

# Define host and port constants
HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 3103 # Port to listen on (non-privileged ports are > 1023)

# Create a socket instance
# socket(family=FAMILY, type=TYPE, proto=PROTOCOL, fileno=FILENO)
# socket.AF_INET is the address family for ipv4
# socket.SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # bind to host and port
    s.listen() # start listening on port

    print(f"Listening on {HOST}:{PORT}")

    while True:
        # Accept the incoming connection, if any
        # Returns a tuple containing new socket connection and address
        conn, addr = s.accept()
   
        # After a client is connected, new connection
        with conn:
            print(f'New Client Connection: {addr}')
            
            # Loop until all data is read
            while True:
                data = conn.recv(1024) # recieve 1 m

                if not data:
                    break

                print(f"Client Sent: {data}")
                
                conn.sendall(data) # send recieved data back

        print(f"Client Disconnected: {addr}")
