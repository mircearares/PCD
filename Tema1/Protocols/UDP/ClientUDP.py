from Protocols.Network import Network
import socket
import time

class ClientUdp(Network):

    def __init__(self):
        super().__init__("UDP")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("UDP Client initialized")

        self.messageCount = 0
        self.byteCount = 0

        self.end = 0

        self.filesToSend = [self.SMALL_FILE_PATH]

    def stream(self):
        self.method = "Stream"
        
        for file in self.filesToSend:
            self.start = time.time()

            f = open(file, 'rb')
            bytes = f.read(self.BUFFSIZE)
            self.byteCount = len(bytes)

            while bytes:
                self.client.sendto(bytes, self.ADDR)
                self.messageCount += 1

                bytes = f.read(self.BUFFSIZE)
                self.byteCount += len(bytes)

            f.close()

            self.end = time.time()

            encodedEnd = "END".encode()
            self.client.sendto(encodedEnd, self.ADDR)
            self.client.close()

            self.print_info()


    def stop_wait(self):
        self.method = "Stop & Wait"

        for file in self.filesToSend:
            self.start = time.time()

            f = open(file, 'rb')
            bytes = f.read(self.BUFFSIZE)
            self.byteCount = len(bytes)

            while bytes:
                self.client.sendto(bytes, self.ADDR)
                self.messageCount += 1

                bytes = f.read(self.BUFFSIZE)
                self.byteCount += len(bytes)

                try:
                    encodedAck, server = self.client.recvfrom(self.BUFFSIZE)
                    print("Received from Server - {} - : Message - {} -".format(server, encodedAck.decode()))
                except socket.timeout:
                    print("Request timed out")
                    break

            f.close()

            self.end = time.time()

            encodedEnd = "END".encode()
            self.client.sendto(encodedEnd, self.ADDR)
            self.client.close()

            self.print_info()