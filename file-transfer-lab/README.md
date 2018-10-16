# File-Transfer-Lab by Miguel Nunez

Modified version of Class Code Given

# How to Send Any type of File to server

Make sure the server is working in order for the client ot connect

* Terminal 1: python fileServer.py

* Terminal 2: python fileClient.py
    - Type in client: " test.txt"   //test.txt is file to be copied into server
    - Refresh Directory and the new file is called NewTestFilename

# Multiple Clients Can Connect

*  Terminal 1: python fileServer.py

* Terminal 2: python fileClient.py
    - Type in client: " test.txt"   //test.txt is file to be copied into server
    - Refresh Directory and the new file is called NewTestFilename
 *Terminal 3: Open another client terminal and it should allow you to connect to server

# Proxy Server

* To use proxy server it means that  we need to use  50000 server instead from 50001 for normal

* Terminal 1: Open Proxy terminal - python stammer-proxy.py

* Terminal 2: python fileServer.py

* Terminal 3: python fileClient.py
    _This should allow you to use the proxy and file transfer as normal
    - Type in client: " test.txt"   //test.txt is file to be copied into server
    - Refresh Directory and the new file is called NewTestFilename