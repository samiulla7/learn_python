'''
Socket Programming in Python
Socket programming is a way of connecting two nodes on a network to communicate with each other. 
One socket(node) listens on a particular port at an IP, 
while other socket reaches out to the other to form a connection. 
Server forms the listener socket while client reaches out to the server.
They are the real backbones behind web browsing. In simpler terms there is a server and a client.
'''

# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys 

try: 
    # AF_INET refers to the address family ipv4
    # SOCK_STREAM means connection oriented TCP protocol.
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	print "Socket successfully created"
except socket.error as err: 
	print "socket creation failed with error %s" %(err) 

# default port for socket 
port = 80

try: 
	host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 

	# this means could not resolve the host 
	print "there was an error resolving the host"
	sys.exit() 

# connecting to the server 
s.connect((host_ip, port)) 

print ("the socket has successfully connected to google on port == %s" %(port))
