import os 
#print os.sys.path
from scapy.all import *
import textparser
from textparser import Sequence

pkts_dict=[]
count = 0
pkts = rdpcap("main.cap")

for pkt in pkts:
    pkts_dict.append({
        'time': (pkt.time/1000),
        #'packetNumber': pkt.show(dump=true).split('\n')[1] ,
        #'size': pkt.show(dump=true).split('/n')
        'protocol': 1})
