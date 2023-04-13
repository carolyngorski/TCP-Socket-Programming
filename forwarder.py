import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python " + sys.argv[0] + " <client listen port> <server listen port>")
    sys.exit(-1)

client_port = int(sys.argv[1])
server_port = int(sys.argv[2])
# Create a client socket to receive the data that the client sends 
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.bind(("0.0.0.0", client_port))
# Create a server socket to forward the data to the server 
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Forwarding...")

while True:
    # receive a message from the client 
    data, addr = client_sock.recvfrom(1024)
    print('Received the message "',data.decode("utf-8"),'" to forward to the server:')
    
    #forward data to server
    server_sock.sendto(data, ("127.0.0.1", server_port))
    if data.decode("utf-8") == "bye":
        break

client_sock.close()
server_sock.close()
