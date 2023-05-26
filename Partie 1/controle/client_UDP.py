import socket
import signal
import sys

msgFromClientStart = "START"
msgFromClientStop = "STOP"

bytesToSend = str.encode(msgFromClientStart)

serverAddressPort = ("127.0.0.1", 20002)

bufferSize = 1024


# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    bytesToSendStop = str.encode(msgFromClientStop)
    UDPClientSocket.sendto(bytesToSendStop, serverAddressPort)

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to Stop')
signal.pause()



