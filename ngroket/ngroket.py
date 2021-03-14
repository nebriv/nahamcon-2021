import socket
import struct
import json
import time
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)


def recvall(sock):
    BUFF_SIZE = 256 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

def recvblastoff(sock):
    BUFF_SIZE = 256 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if b"ngrocket!!" in part:
            break
    return data


def recvall_header(sock):
    BUFF_SIZE = 256 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if b"> " in part:
            break
    return data

counter = 0

recv_data = {}
while counter < 100000:

    TCP_IP = 'challenge.nahamcon.com'
    TCP_PORT = 30574
    BUFFER_SIZE = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    # s.send(MESSAGE)
    data = recvall_header(s)

    print(data.splitlines()[-1])
    ngrok = "2.tcp.ngrok.io:16538"
    if data.splitlines()[-1] == b"> ":
        print("SENDING NGROK")
        s.sendall(ngrok.encode())
        d = recvblastoff(s)
        dlines = d.decode().splitlines()
        key = dlines[3].split(" Key:")[1].strip()
        IV = dlines[4].split(" IV:")[1].strip()
        print(key)
        print(IV)

    s.close()

    recv_data = {"key": key, "IV": IV}
    counter += 1

    with open("dataOut\\s_%s.json" % counter, 'w') as outFile:
        json.dump(recv_data, outFile)

print("Done!")