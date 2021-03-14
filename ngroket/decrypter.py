import os
import time
import json
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
from binascii import hexlify, unhexlify
import pyaes, pbkdf2, binascii, os, secrets
# backend = default_backend()
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Util.Padding import unpad
import os, os.path

key_bytes = 32
#

flag = "______________________________________"
while True:
    path, dirs, files = next(os.walk("dataOut"))
    data = b""
    counter = 1

    flag_hint_count = 0

    while counter < len(files) // 2:

        encrypted_data = unhexlify(open('dataOut\\l_%s.json' % counter).read())
        key_data = json.load(open('dataOut\\s_%s.json' % counter))
        key = unhexlify(key_data['key'])
        iv = unhexlify(key_data['IV'])

        # res = decrypt(key,iv,encrypted_data)
        # print(res)

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
        # print(AES.block_size)
        try:
            original_data = cipher.decrypt(encrypted_data)
            data += original_data
            # print(original_data)
            if b"flag" in original_data:
                # print(original_data)
                flag_hint_count += 1
                index_loc = int(original_data.split(b"index ")[1].split(b" ")[0])
                # print(index_loc)
                character = original_data.split(b"'")[1].split(b"'")[0]
                # print(character)

                flag = flag[:index_loc] + character.decode('ascii') + flag[index_loc + 1:]
                # print("flag{%s}" % flag)

        except ValueError as e:
            print(e)

        counter += 1

    print("FLAG: %s" % flag)
    print("Total Requests: %s" % str(len(files) // 2))
    print("Total Hints: %s" % flag_hint_count)
    print("Sleeping...")
    time.sleep(15)