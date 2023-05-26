import socket
import time
import random



serverAddressPort = ("127.0.0.1", 20002)

bufferSize = 1024


# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True : 
    interval = random.randint(5,10)
    iteration = random.randint(20,100)
    print("On envoie "+str(iteration)+" messages avec un inetervalle de "+str(interval*10)+" millisecondes"  )
    for x in range(0, iteration):
        time.sleep(interval*10/1000)
        msgFromClientMsg = "MESSAGE"+str(x+1)
        bytesToSend = str.encode(msgFromClientMsg)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    attente = random.randint(5,15)
    print("On attend "+str(attente)+" secondes"  )
    time.sleep(attente)


        

# Send to server using created UDP socket





