import os.path

class Network:

    def __init__(self, protocol):
         self.HOST = '127.0.0.1'
         self.PORT = 1111
         self.ADDR = (self.HOST, self.PORT)
         self.BUFFSIZE = 2048
         self.protocol = protocol

         self.SMALL_FILE_PATH = os.path.join("Files", "5mb.txt") 
         self.MEDIUM_FILE_PATH = os.path.join("Files", "500mb.txt")
         self.BIG_FILE_PATH = os.path.join("Files", "1gb.txt")

         self.SERVER_RESULTS_PATH = os.path.join("Files", "Results", "server.txt")
         self.CLIENT_RESULTS_PATH = os.path.join("Files", "Results", "client.txt")


    def print_info(self):
        outputList = [
            "{} - {}".format(self.protocol, self.method),
            "Message Count: {}".format(self.messageCount),
            "Bytes Count: {}".format(self.byteCount),
            "Total Time: {}s".format(round(self.end - self.start, 2))
        ]

        isServer = self.__class__.__name__.startswith("Server")

        fileToOpen = self.SERVER_RESULTS_PATH if isServer else self.CLIENT_RESULTS_PATH
        file = open(fileToOpen, 'a')
        file.write("\n")

        for output in outputList:
            print(output)
            file.write("{}\n".format(output))

        file.close()