# imports
from scapy.all import *

# arbitrarily defining ports to scan
ports = [25, 80, 53, 443, 445, 8080, 8443]

# scans ports by using a syn-ack packet to test if a port is open
def syn_scan(h):
    ans,_ = sr(IP(dst=h)/TCP(sport=5555, dport=ports,flags="S"), timeout=2, verbose=0)

    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        # if we get a response packet from the destination port, the port is open
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)

# here we specifically check for a DNS server on port 53
def dns_scan(h):
    ans,_ = sr(IP(dst=h)/UDP(sport=5555, dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")), timeout=2, verbose=0)
    if ans:
        print("DNS Server at %s:" % h)

# this ultimately throws an error as 8.8.8.8 does not return a packet containing a TCP layer
if __name__ == "__main__":
    host = "8.8.8.8"

    syn_scan(host)
    dns_scan(host)