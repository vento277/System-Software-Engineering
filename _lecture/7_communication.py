'''
Cooperating Processes require IPC to exchange data and information. IPC primarily uses two models: shared memory and message passing.

1. Shared Memory
- Definition: Allows multiple processes to access a common memory space.
- Access Control: The operating system typically restricts memory access between processes. For shared memory, mutual agreement is necessary to grant access.
- Synchronization: Processes must avoid simultaneous writes to the same memory location to prevent data inconsistency (e.g., the producer-consumer problem).

2. Message Passing
- Definition: Provides a mechanism for processes to communicate and synchronize their actions without sharing variables.
- Key Operations:
  - send(message): Sends a message to another process.
  - receive(message): Receives a message from another process.
- Usage: Particularly useful in distributed environments, such as chat applications.
- Message Queues:
  - Zero Capacity: The sender waits until the receiver is ready.
  - Bounded Capacity: The sender blocks if the queue is full.
  - Unbounded Capacity: The sender never waits, allowing continuous sending.

3. Communication Links
- A communication link must be established, which can be either physical (hardware) or logical (message queue).
- Link Characteristics:
  - Supports multi-process associations.
  - Can have fixed or variable message sizes.
  - Can be unidirectional or bi-directional.

4. Communication Types
- Blocking (Synchronous):
  - send blocks until the message is received.
  - receive blocks until a message is available.

- Non-blocking (Asynchronous):
  - send continues immediately after sending the message.
  - receive may return a valid message or null if none is available.

5. IPC Mechanisms
- Sockets: Key mechanisms for inter-process communication (IPC), allowing two processes to communicate, either locally or remotely.
  - TCP Sockets: Connection-oriented and reliable. Stream
  - UDP Sockets: Connectionless with best-effort delivery. Datagram

- Pipes: 
  - Function as conduits for processes to communicate, supporting the producer-consumer model.
  - Implementation involves ordinary pipes with read (r) and write (w) ends.
  - Example Usage: ls | more in command-line environments.

- Remote Procedure Calls (RPC):
  - Purpose: Allows remote procedure invocation as if it were local.
  - Communication relies on message-based exchanges with structured messages.

6. Client-Server Model
- Definition: A relationship where a server provides services and clients request them.
- Examples include email clients and web browsers.

7. Data Representation Issues
- Endianness: Differences in byte order between clients and servers must be managed.
  - Little-endian: Least significant byte first (e.g., Intel x86).
  - Big-endian: Most significant byte first (e.g., Motorola).
  - Bi-endian: Supports switchable endianness (e.g., ARM architecture).
'''
from socket import *

# Python’s Socket Module
# Reference: https://docs.python.org/3/library/socket.html

# Socket Creation
clientSocket = socket(AF_INET, SOCK_STREAM)  # Creates a new socket

# Socket Families
ipv4_socket = socket(AF_INET, SOCK_DGRAM)      # For IPv4 addresses
ipv6_socket = socket(AF_INET6, SOCK_DGRAM)     # For IPv6 addresses

# Important Methods
# UDP Client
udp_client_socket = socket(AF_INET, SOCK_DGRAM)
udp_client_socket.sendto(b'Hello', ('localhost', 12345))
udp_client_socket.close()

# UDP Server
udp_server_socket = socket(AF_INET, SOCK_DGRAM)
udp_server_socket.bind(('', 12345))
message, client_address = udp_server_socket.recvfrom(2048)
udp_server_socket.sendto(message.upper(), client_address)

# TCP Client
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(('localhost', 12345))
tcp_client_socket.send(b'Hello')
response = tcp_client_socket.recv(1024)
tcp_client_socket.close()

# TCP Server
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind(('', 12345))
tcp_server_socket.listen(1)
connection_socket, addr = tcp_server_socket.accept()
data = connection_socket.recv(1024)
connection_socket.send(data.upper())
connection_socket.close()

# UDP Socket Functions
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.sendto(b'Message', ('localhost', 12345))  # Sending data
data, addr = udp_socket.recvfrom(2048)                # Receiving data

# TCP Socket Functions
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(('localhost', 12345))               # Sending data
tcp_socket.send(b'Message')
data = tcp_socket.recv(1024)                           # Receiving data

# Binding and Listening (TCP)
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 12345))                        # Binding to an address
server_socket.listen(1)                                # Listening for incoming connections
connection_socket, addr = server_socket.accept()       # Accepting connections

# Connection Management
server_socket.connect(('localhost', 12345))           # Connecting to server
server_socket.close()                                  # Closing the socket

# Client Interaction Example for UDP
from socket import *

serverName = "hostname"  # Replace with actual server name
serverPort = 12000        # Use an available port

# Create a UDP socket for the client
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get user input
message = input("Input lowercase sentence: ")

# Send message to server
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receive modified message from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Print received message
print(modifiedMessage.decode())

# Close the client socket
clientSocket.close()

# UDP Server Example
"""
Create a UDP socket, bind it to a local port, and loop to handle incoming messages.
"""

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to the local port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    # Read from the UDP socket into message, getting client’s address
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # Convert message to uppercase
    modifiedMessage = message.decode().upper()
    
    # Send uppercased string back to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)