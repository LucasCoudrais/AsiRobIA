# echo-client.py

import socket
import time
import random

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True : 
        interval = random.randint(5,10)
        iteration = random.randint(20,100)
        print("On envoie "+str(iteration)+" messages avec un inetervalle de "+str(interval*10)+" millisecondes"  )
        for x in range(0, iteration):
            time.sleep(interval*10/1000)
            msgFromClientMsg = "MESSAGE"+str(x+1)
            bytesToSend = str.encode(msgFromClientMsg)
            s.send(bytesToSend)
        attente = random.randint(5,15)
        print("On attend "+str(attente)+" secondes"  )
        time.sleep(attente)


