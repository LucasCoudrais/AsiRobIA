# echo-client.py

import socket
import signal
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        print('Envoie STOP')
        s.send(b"STOP")
        sys.exit(0)


    s.send(b"START")
    print("Envoi START")
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to Stop')
    signal.pause()
