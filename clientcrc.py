import socket
import struct
import sys
import binascii

# defining the crc32() function 
def crc32(v):
     r = binascii.crc32(v.encode())
     return r



if len(sys.argv) != 3:
    print("Useage: python " + sys.argv[0] + " <forwarder_ip> <forward port>")
    sys.exit(-1)

forwarder_ip = sys.argv[1]
forwarder_listen_port = int(sys.argv[2])

# create a udp socket to send messages through to the forwarder
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:   
    print("Input text:")
    text = sys.stdin.readline().strip()
    ss = struct.pack("!50sL",text.encode(),crc32(text))
    s.sendto(ss,(forwarder_ip,forwarder_listen_port))
    if text == "bye":
        break
