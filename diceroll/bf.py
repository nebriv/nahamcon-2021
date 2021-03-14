import socket
import struct
import json
import time
import random
from randcrack import RandCrack
from tqdm import tqdm
rc = RandCrack()

TCP_IP = 'challenge.nahamcon.com'
TCP_PORT = 31784
BUFFER_SIZE = 4096
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


def recvall_header(sock):
    BUFF_SIZE = 256 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if b"> " in part:
            break
    return data


data = recvall_header(s)
# print(data.decode())
s.send(b"2\n")
data = recvall_header(s)

rc = RandCrack()
#
i = 0

for i in tqdm(range(0,624)):
    s.send(b"2\n")
    data = recvall_header(s)
    number = int(data.split(b"sum was")[1].split(b"0.")[0].splitlines()[1])
    rc.submit(number)
    i += 1

print("OUR PREDICTION:")
pred = rc.predict_randrange(0, 4294967295)
print(str(pred))

send_data = "\n"
s.send(send_data.encode())

data = recvall_header(s)
# print(data.decode())
s.send(b"3\n")

send_data = "%s\n" % str(pred)
s.send(send_data.encode())
data = recvall_header(s)
print(data.decode())
send_data = "%s\n" % str(pred)
s.send(send_data.encode())
data = recvall_header(s)
print(data.decode())
