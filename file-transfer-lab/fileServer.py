#! /usr/bin/env python3
import sys

sys.path.append("../lib")  # for params
import re, socket, params

switchesVarDefaults = (
    (('-l', '--listenPort'), 'listenPort', 50001),
    (('-d', '--debug'), "debug", False),  # boolean (set if present)
    (('-?', '--usage'), "usage", False),  # boolean (set if present)
)

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

sock, addr = lsock.accept()

print("connection rec'd from", addr)

from framedSock import framedSend, framedReceive

while True:
    header = framedReceive(sock, debug)
    payload = framedReceive(sock,debug)
    # basically decodes the b 
    newFile = open(b'NewTest:'+header, 'wb')
    newFile.write(payload)
    newFile.close()


