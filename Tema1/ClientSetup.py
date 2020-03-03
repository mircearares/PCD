from Protocols.TCP.ClientTCP import ClientTcp
from Protocols.UDP.ClientUDP import ClientUdp

print("Client setup")
protocol = input("Select protocol:\n   1 -> TCP\n   2 -> UDP\nOption? ")
method = input("Select method:\n   1 -> Streaming\n   2 -> Stop & Wait\nOption? ")

if protocol == "1" and method == "1":
    ClientTcp().stream()
elif protocol == "1" and method == "2":
    ClientTcp().stop_wait()
elif protocol == "2" and method == "1":
    ClientUdp().stream()
elif protocol == "2" and method == "2":
    ClientUdp().stop_wait()