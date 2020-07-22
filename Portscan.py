#!/usr/bin/python3
# Resources used: https://pythonprogramming.net/python-port-scanner-sockets/
#       https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python

import socket
import sys

ip = sys.argv[1]
fp = int(sys.argv[2])
lp = int(sys.argv[3])

def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((ip,port))
        return True
    except:
        return False

for x in range(int(fp),(int(lp)+1)):
    if scan(x):
        print("Port ", x, " on ", ip, " is open.")
    else:
        print("Port ", x, " on ", ip, " is closed.")