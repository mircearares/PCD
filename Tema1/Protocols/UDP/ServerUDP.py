from Protocols.Network import Network
import socket
import time

class ServerUdp(Network):

    def __init__(self):
        super().__init__("UDP")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(self.ADDR)
        print("UDP Server initialized")

        self.messageCount = 0
        self.byteCount = 0

        self.end = 0

    def stream(self):
        self.method = "Stream"
        self.start = time.time()
        
        while True:
            message, addr = self.server.recvfrom(self.BUFFSIZE)
            decodedMessage = message.decode()

            print('Client connection established {}'.format(addr))

            if decodedMessage == "END":
                self.end = time.time()
                break

            self.messageCount += 1
            self.byteCount += 1
            
        self.print_info()


    def stop_wait(self):
        self.method = "Stop & Wait"
        self.start = time.time()

        encodedAck = "ACK".encode()

        while True:
            message, addr = self.server.recvfrom(self.BUFFSIZE)
            decodedMessage = message.decode()
            
            print('Client connection established {}'.format(addr))

            self.server.sendto(encodedAck, addr)

            if decodedMessage == "END":
                self.end = time.time()
                break

            self.messageCount += 1
            self.byteCount += len(decodedMessage)
            
        self.print_info()