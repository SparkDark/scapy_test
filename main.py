import argparse
from protocol.ICMP_PING import ICMP_SCAN
from protocol.ARP_PING import ARP_PING
from protocol.TCP_PING import TCP_PING
from protocol.UDP_SCAN import UDP_PING

parser = argparse.ArgumentParser("Scapy сканирование")
parser.add_argument("-d", "--destination", help="host сканирования", required=True)
parser.add_argument("-p", "--ports",type=int, nargs='+', help="port сканирования 21 23 0 ..")
parser.add_argument("-s", "--scantype", help="Scan type, icmp/tcp/udp/arp", required=True)

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