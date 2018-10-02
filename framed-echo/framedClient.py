#! /usr/bin/env python3

# Echo client program
import sys

sys.path.append("../lib")  # for params
import re, params, socket

from framedSock import framedSend, framedReceive

# To use proxy server it means that  we need to use  50000 server
# 50001 for normal
switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False),  # boolean (set if present)
    (('-?', '--usage'), "usage", False),  # boolean (set if present)
)

progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

while True:
    # Send server User Input
    userInput = input('Input Name of File to transport: ')
    framedSend(s, b"Filename=" + userInput.encode(), debug)
    # print(framedReceive(s, b"Filename=" + userInput.encode()))
    # Get file ready to send to server
    with open(userInput, 'rb') as f:
        # grab the lines
        data = f.read()
        # replaces new line charcters with temp character to signify new line
        data = data.replace(b'\n', b'@')
        framedSend(s, data, debug)
        f.close()
        print(framedReceive(s, data + userInput.encode()))

        while len(data) >= 100:
            # grab every 100 bites
            firstHalf = data[:100]
            data = data[100:]
            # Send first half
            framedSend(s, firstHalf, debug)
            print(framedReceive(s, b"FirstPart" + firstHalf + userInput.encode()))

            if len(data) > 0:
                framedSend(s, data, debug)
                print(framedReceive(s, b"Rest" + data + userInput.encode()))
