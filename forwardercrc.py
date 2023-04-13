import socket
import sys
import struct
import binascii
import random 
import zlib



def crc32(v):
     r = binascii.crc32(v.encode())
     return r



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


# fmt = "!I1024sI"

print("Forwarding...")

while True:
   
    # receive a message from the client 
    data, addr = client_sock.recvfrom(2048)
    msg, crc_orig = struct.unpack("!50sL", data)
    msg = msg.decode("utf-8").replace("\0", "")
    # Got this line of code from the server.py code, changed msg, crc_orig
    crc_orig = crc_orig & 0xffffffff
    print("Received Message: %s\nCRC32 code: %X" % (msg, crc_orig))
    
    #Modify the message with a 40% probability 
    if random.random() < 0.4:  
        msg = "Modified: "+ msg

    #Repack the modified message into a struct with the original CRC32 code
    crc_mod = binascii.crc32(msg.encode())
    data_mod = struct.pack("!50sL", msg.encode(), crc_orig)

   
    server_sock.sendto(data_mod, ("127.0.0.1", server_port))
   

    # client_sock.close()
    # server_sock.close()


 
    