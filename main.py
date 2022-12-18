import argparse
import time

from protocol.ARP_SPOOFING import ARP_SPOOFING
from protocol.ICMP_PING import ICMP_SCAN
from protocol.ARP_PING import ARP_PING
from protocol.TCP_PING import TCP_PING
from protocol.UDP_SCAN import UDP_PING

parser = argparse.ArgumentParser("Scapy сканирование")
parser.add_argument("-d", "--destination", help="host сканирования", required=True)
parser.add_argument("-p", "--ports",type=int, nargs='+', help="port сканирования 21 23 0 ..")
parser.add_argument("-s", "--scantype", help="Scan type, icmp/tcp/udp/arp/arp_spoof", required=True)
parser.add_argument("-gw", "--gateway", help= "Gateway by ARP Spoof")

args = parser.parse_args()

if args.ports:
	ports = args.ports
else:
	# default port range
	ports = range(1, 1024)

scantype = args.scantype.lower()

if scantype == "icmp":
	ICMP_SCAN(args.destination).run()

if scantype == "arp":
	ARP_PING(args.destination).run()

if scantype == "tcp":
	TCP_PING(args.destination,ports).run()

if scantype == "udp":
	UDP_PING(args.destination,ports).run()

if scantype == "arp_spoof":
	arp_spoof = ARP_SPOOFING(args.destination)
	arp_spoof.enable_route()
	if args.gateway:
		host = args.gateway
	else:
		host = "192.168.0.1"
	try:
		while True:
			arp_spoof.spoof(args.destination,host,True)
			arp_spoof.spoof(host,args.destination,True)
			time.sleep(1)
	except KeyboardInterrupt:
		print("[!] Detected CTRL+C ! restoring the network, please wait...")
		arp_spoof.restore(args.destination, host)
		arp_spoof.restore(host, args.destination)