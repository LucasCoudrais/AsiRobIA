import socket
import time
import random



serverAddressPort = ("127.0.0.1", 20002)

bufferSize = 1024


# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
x=1
while True : 

    time.sleep(5/1000)
    msgFromClientMsg = "MESSAGE"+str(x)
    bytesToSend = str.encode(msgFromClientMsg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    x=x+1
        



        

# Send to server using created UDP socket





