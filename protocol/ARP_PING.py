from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

from logger.logger import log_fail, log_info,bcolors


class ARP_PING():
    def __init__(self,destination):
        self.destination = destination

    def run(self):
        try:
            ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=self.destination), timeout=3)
            ans.summary(lambda s, r: r.sprintf(bcolors.OKGREEN + "%Ether.src% %ARP.psrc%" ))
        except:
            log_fail('error ARP scan')