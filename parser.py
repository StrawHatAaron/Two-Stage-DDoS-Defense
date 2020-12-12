#Aaron Miller and Lang Le CSc 154 Project
import os 
from scapy.all import *
import textparser
from textparser import Sequence

pkts_dict=[]
count = 0
pkts = rdpcap("../smtp.cap")

for pkt in pkts:
    pkts_dict.append({
        'time': (pkt.time/1000),
        #'packetNumber': pkt.show(dump=true).split('\n')[1] ,
        #'size': pkt.show(dump=true).split('/n')
        'protocol': pkt.show(dump=True).split("###[ IP ]###", 1),
        'id': count
        })
    pkt.show()
    print pkts_dict[count]['protocol']
    print "\n"
    count = count + 1


