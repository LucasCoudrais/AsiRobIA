# echo-client.py

import socket
import time
import random

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    x=1
    while True : 
        time.sleep(5/1000)
        msgFromClientMsg = "MESSAGE"+str(x)
        bytesToSend = str.encode(msgFromClientMsg)
        s.send(bytesToSend)
        x=x+1


