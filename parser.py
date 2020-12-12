#Aaron Miller and Lang Le CSc 154 Project
import os 
import re
from scapy.all import *
import textparser
from textparser import Sequence

pkts_dict=[]
count = 0
#pkts = rdpcap("../smtp.cap")
pkts = rdpcap("../dns.cap")
#pkts = rdpcap("../smb.cap") 

for pkt in pkts:
    pkts_dict.append({
        'time': (pkt.time/1000),
        #'packetNumber': pkt.show(dump=true).split('\n')[1] ,
        'size': re.split("\D",(pkt.show(dump=True).split("len")[1].split("=")[1]))[1],
        #'protocol': pkt.show(dump=True).split("###[ IP ]###", 1),
        'count': count,
        'unique': 'TBD',
        'ith-frame': (pkt.time/1000) - 6,
        'protocol': 'dns'
        })
    #pkt.show()
    print "header for count"
    print count
    print "\n"
    print "size"
    print pkts_dict[count]['size']
    print "\n"
    count = count + 1


