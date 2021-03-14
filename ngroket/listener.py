import socket
import json
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

def recvall(sock):
    BUFF_SIZE = 128 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

counter = 0
recv_data = {}
while counter < 100000:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = recvall(conn)
            print(data.decode())

            counter += 1
            recv_data[counter] = data.decode().strip()

            with open("dataOut\\l_%s.json" % counter, 'w') as outFile:
                outFile.write(data.decode().strip())

print("Done!")