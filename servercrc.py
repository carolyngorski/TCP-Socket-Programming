import socket
import sys
import binascii
import struct
import operator

def crc32(v):
    return binascii.crc32(v.encode())

if len(sys.argv) != 2:
    print("Useage: python " + sys.argv[0] + " <liseten port>")
    sys.exit(-1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", int(sys.argv[1])))

print("Waiting..")

while True:
    data, addr = s.recvfrom(2048)
    # hex_data = binascii.hexlify(data).decode('ascii')

    # print("Received from forwarder (hex): ", hex_data)
    message, crc32_code = struct.unpack("!50sL", data)
    message = message.decode("utf-8").replace("\0", "")
    crc32_code = crc32_code & 0xffffffff
    print("Message: %s\nCRC32 code: %X" % (message, crc32_code))

    # Verify the integrity of the message using the CRC32 code
    if crc32(message) == crc32_code:
        print("CRC32 check passed.")
    else:
        print("CRC32 check failed.")

    if message == "bye":
        break







    # str,crc = struct.unpack("!50sL",data)
    # str = str.decode("utf-8").replace("\0","")
    # print("Received from forwarder: str:%s\ncrc:%X" % (str,crc & 0xffffffff))
    # if str == "bye":
    #     break


