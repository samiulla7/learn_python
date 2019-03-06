
# Workes with python3
import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

'''
socket.socket() creates a socket object
socket type :  
AF_INET is the Internet address family for IPv4. 
SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport our messages in the network.

The values passed to bind() depend on the address family of the socket. In this example, we’re using socket.AF_INET (IPv4). 
So it expects a 2-tuple: (host, port).

host can be a hostname, IP address, or empty string. 
If an IP address is used, host should be an IPv4-formatted address string. 
The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface, 
so only processes on the host will be able to connect to the server. 
If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind() is used to associate the socket with a specific network interface and port number
    s.bind((HOST, PORT))
    # listen() enables a server to accept() connections. It makes it a “listening” socket
    s.listen()
    #accept() blocks and waits for an incoming connection. When a client connects, 
    # it returns a new socket object representing the connection and a tuple holding the address of the client. 
    # client socket object conn from accept()
    conn, addr = s.accept()
    print(conn,addr)
    with conn:
        print('Connected by', addr)
        while True:
            '''
            If conn.recv() returns an empty bytes object, b'', 
            then the client closed the connection and the loop is terminated. 
            The with statement is used with conn to automatically close the socket at the end of the block.
            '''
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)