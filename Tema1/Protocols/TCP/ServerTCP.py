from Protocols.Network import Network
import socket
import time

class ServerTcp(Network):

    def __init__(self):
        super().__init__("TCP")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen(5)

        self.messageCount = 0
        self.byteCount = 0
        self.start = 0
        self.end = 0

        print("TCP Server initialized")


    def stream(self):
        self.method = "Stream"

        while True:
            conn, addr = self.server.accept()

            print('Client connection established {}'.format(addr))

            self.start = time.time()

            while True:
                dataReceived = conn.recv(self.BUFFSIZE)
                self.messageCount += 1
                self.byteCount += len(dataReceived)

                if not dataReceived:
                    break
            
            self.end = time.time()

            self.print_info()

            conn.close()

    def stop_wait(self):
        self.method = "Stop & Wait"
        encodedAck = "ACK".encode()

        while True:
            conn, addr = self.server.accept()

            print('Client connection established {}'.format(addr))

            self.start = time.time()

            conn.sendall(encodedAck)
            while True:
                dataReceived = conn.recv(self.BUFFSIZE)
                self.messageCount += 1
                self.byteCount += len(dataReceived)

                conn.sendall(encodedAck)

                if not dataReceived:
                    break
            
            self.end = time.time()

            self.print_info()

            conn.close()