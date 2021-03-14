import string
import re
with open('hackers.txt', 'r') as in_file:
    text = in_file.read()
    text = ''.join(ch for ch in text if ch.isalnum())

    text = re.sub(r'[a-fA-F0-9]', '', text)
    print(text)