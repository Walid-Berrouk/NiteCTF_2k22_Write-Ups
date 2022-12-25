#! /usr/bin/python3

from pwn import *


HOST = '35.204.16.174'
PORT = 1337

while True :
    p = remote(HOST, PORT)
    for i in range (0, 10):
        print(p.recvline())
        print(p.recvline())
        print(p.recvline())
        # p.sendline(b"1")
        p.sendline(b"2")
        result = p.recvline()
        print(result)
        if result == b'Sorry, you lost :(\n' :
            break

    if (i == 9) and (result != b'Sorry, you lost :(\n') :
        break

p.interactive()