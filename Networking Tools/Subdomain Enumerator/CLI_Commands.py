import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--default", action="store_true", help="Use default prefix list")
    group.add_argument("-w", "--wordlist", type=str, help="Path to custom wordlist file")
    parser.add_argument("domain", help="Target domain name")
    return parser.parse_args()
