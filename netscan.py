from scapy.all import ARP, Ether, srp
import sys

# Professional ARP Network Scanner
class NetScanner:
    def __init__(self, target_range):
        self.target_range = target_range

    def scan(self):
        print(f"[*] Scanning range: {self.target_range}...")
        # Create ARP request packet
        arp = ARP(pdst=self.target_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        # Send and receive packets
        result = srp(packet, timeout=3, verbose=0)[0]

        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        return devices

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python netscan.py <ip_range> (e.g. 192.168.1.0/24)")
        sys.exit(1)

    scanner = NetScanner(sys.argv[1])
    active_devices = scanner.scan()

    print(f"[+] Found {len(active_devices)} devices:")
    for device in active_devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']}")
