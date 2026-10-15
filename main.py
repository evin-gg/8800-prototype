from os import write

from scapy import packet
from scapy.all import sniff, IP, AsyncSniffer, wrpcap
import time
from pathlib import Path
import json
from datetime import datetime

# global
ip_collection = set()
connection_list = []

# connection object
class Connection:
    def __init__(self, src, dst, protocol, timestamp):
        self.src = src
        self.dst = dst
        self.protocol = protocol
        self.timestamp = timestamp


# can grab information with this function
def process_packet(p):
    formatted_time = datetime.fromtimestamp(float(p.time)).strftime('%H:%M:%S')
    if IP in p:
        src = p[IP].src
        dst = p[IP].dst
        proto = p[IP].proto

        ip_collection.add(src)
        print(f"{src} -> {dst} proto={proto} len={p[IP].len}")

        c = Connection(src, dst, proto, formatted_time)
        connection_list.append(c)

def main():

    #create the folder of IP addresses
    folder = Path("Addresses")
    folder.mkdir(parents=True, exist_ok=True)

    packets = sniff(offline = "capture.pcap")


    # non blocking sniffer
    # t1 = AsyncSniffer(
    #     filter = "ip",
    #     prn = process_packet,
    #     count = 10,
    #     store = False
    # )
    # t1.start()


    for p in packets:
        process_packet(p)

    print("-----------------------IP Record List -----------------------")
    for ip in ip_collection:
        print(ip)

        directory = ("./Addresses/" + str(ip) + ".json")
        data = {
                "ip": str(ip),
                "connections": []
        }

        for c in connection_list:
            if(str(c.src) == str(ip)):

                connection = {
                    "dst": c.dst,
                    "protocol": c.protocol,
                    "timestamp": c.timestamp
                }

                data["connections"].append(connection)
                

                

        with open(str(directory), "w") as file:
            json.dump(data, file, indent = 4)

    # end of packet processing
    
    # interface (text)
    while True:
        selectIP = input("Enter IP (default 192.168.1.73): ")

        if not selectIP:
            selectIP = "192.168.1.73"
            break
        elif selectIP not in ip_collection:
            print("Invalid IP, not one of the options.")
            selectIP = "192.168.1.73"
            continue
        else:
            break

    print("\n\nList Of Connections for " + selectIP + ":")
    
    with open("./Addresses/" + selectIP + ".json") as file:
        data = json.load(file)

        for c in data["connections"]:
            print("["+ c["timestamp"] + "]\t" + f"{data["ip"]} -> {c["dst"]}\tprotocol={c["protocol"]}")

if __name__ == "__main__":
    main()

