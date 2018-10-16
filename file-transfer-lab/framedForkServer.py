#! /usr/bin/env python3
import os
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

while True:
    sock, addr = lsock.accept()

    from framedSock import framedSend, framedReceive

    if not os.fork():
        print("new child process handling connection from", addr)
        # This is where the server waits for the header and new data to read
        while True:
            # Data comes out with new lines being represented by the @ sign
            header = framedReceive(sock, debug)
            payload = framedReceive(sock, debug)
            # basically decodes the b
            newFile = open(b'NewTest:' + header, 'wb')
            newFile.write(payload)
            newFile.close()
