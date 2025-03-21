# imports
import dns
import dns.resolver
import socket

# this function checks if the IP is valid and returns the information if true
def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        # otherwise returns nothing
        return []
    return [result[0]] + result[1]

# Resolves DNS names to IP addresses
def dns_request(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s" % reverse_dns(answer.to_text()))

    # if the resolver finds no existing DNS query name or hits a timeout
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

# searches for active subdomains (the prefix to the domain) e.g admin.google.com where "admin" is the subdomain
def subdomain_search(domain, dictionary, nums):
    for word in dictionary:
        subdomain = word +"." + domain
        dns_request(subdomain)
        if nums:
            # simple example brute force for fuzzing subdomains by simply adding numbers
            for i in range(0,10):
                subdomain = word + str(i) +"." + domain
                dns_request(subdomain)

if __name__ == '__main__':
    domain = "google.com"
    d = "subdomains.txt"
    dictionary = []

    with open(d,"r") as f:
        dictionary = f.read().splitlines()

    subdomain_search(domain, dictionary, True)