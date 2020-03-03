from Protocols.TCP.ServerTCP import ServerTcp
from Protocols.UDP.ServerUDP import ServerUdp

print("Server setup")
protocol = input("Select protocol:\n   1 -> TCP\n   2 -> UDP\nOption? ")
method = input("Select method:\n   1 -> Streaming\n   2 -> Stop & Wait\nOption? ")

if protocol == "1" and method == "1":
    ServerTcp().stream()
elif protocol == "1" and method == "2":
    ServerTcp().stop_wait()
elif protocol == "2" and method == "1":
    ServerUdp().stream()
elif protocol == "2" and method == "2":
    ServerUdp().stop_wait()