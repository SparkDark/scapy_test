from scapy import *
from scapy.all import *
from scapy.layers.inet import TCP, ICMP, IP
from logger.logger import *

class ICMP_SCAN:
    def __init__(self,destination):
        self.destination = destination

    # syn scan
    def run(self):
        try:
            pkt = sr1(IP(dst=self.destination)/ICMP()/"XXXXXXXXXXX", timeout=3)
            if pkt != None:
                log_info(hexdump(pkt))
                log_info(str(pkt.summary()))
            else:
                 log_fail("Host %s not answer" % self.destination)
        except:
            log_fail('error ICMP scan')