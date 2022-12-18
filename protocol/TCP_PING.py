import traceback

from scapy.layers.inet import TCP, ICMP, IP
from scapy.sendrecv import sr

from logger.logger import log_fail, bcolors, log_info


class TCP_PING:
    def __init__(self,destination,ports):
        self.destination = destination
        self.ports = ports

    def run(self):
        log_info("Print Scan TCP")
        try:
            for port in self.ports:
                log_info("Scan Port %s" % port )
                ans, unans = sr(IP(dst=self.destination)/TCP(dport=port, flags="S"),timeout=3)

                ans.summary(lambda s, r:
                            r.sprintf(bcolors.OKGREEN + "%IP.src% is alive, scan %TCP.sport%"))


        except Exception as e:
            log_fail("erro TCP SCAN")
            log_fail(traceback.format_exc())
