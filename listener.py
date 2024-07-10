#!/usr/bin/env python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("YOUR IP ADDRESS", 4444)) # Your ıp address and port which is you want to use
listener.listen(0)
print("[+] Waiting for incoming connections")
listener.accept()
print("[+] Got a connection")