from Protocols.Network import Network
import socket
import time

class ClientTcp(Network):

    def __init__(self):
        super().__init__("TCP")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        print("TCP Client initialized")
        print('Server connection established')

        self.messageCount = 0
        self.byteCount = 0
        self.start = 0
        self.end = 0

        self.filesToSend = [self.SMALL_FILE_PATH]


    def stream(self):
        self.method = "Stream"

        for file in self.filesToSend:
            f = open(file, 'rb')
            bytes = f.read(self.BUFFSIZE)
            self.byteCount = len(bytes)
            
            self.start = time.time()

            while(bytes):
                self.client.send(bytes)
                self.messageCount += 1
                print("Message sent. Count: {}".format(self.messageCount))

                bytes = f.read(self.BUFFSIZE)
                self.byteCount += len(bytes)

            f.close()

        self.client.close()

        self.end = time.time()

        self.print_info()


    def stop_wait(self):
        self.method = "Stop & Wait"

        for file in self.filesToSend:
            f = open(file, 'rb')
            bytes = f.read(self.BUFFSIZE)
            self.byteCount = len(bytes)

            ack = self.client.recv(1024)
            decodedAck = ack.decode()

            self.start = time.time()

            while bytes and decodedAck == "ACK":
                self.client.send(bytes)
                self.messageCount += 1
                print("Message sent. Count: {}".format(self.messageCount))

                bytes = f.read(self.BUFFSIZE)
                self.byteCount += len(bytes)

                ack = self.client.recv(1024)
                decodedAck = ack.decode()
               
                print("Received from server: {}".format(decodedAck))

            f.close()

        self.client.close()

        self.end = time.time()

        self.print_info()