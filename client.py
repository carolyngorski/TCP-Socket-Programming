import socket
import sys

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
    s.sendto(text.encode(),(forwarder_ip ,forwarder_listen_port))
    if text == "bye":
        break



