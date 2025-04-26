import argparse
from Wordlist import file_upload
from Subdomain_Enumerator import domain  # Only import domain since Windows_script is nested inside it

def parse_arguments():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--default", action="store_true", help="Use default prefix list")
    group.add_argument("-w", "--wordlist", type=str, help="Path to custom wordlist file")
    parser.add_argument("domain", help="Target domain name")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    # Extract the domain from command line arguments instead of asking for input
    domain_main = args.domain
    
    if args.default:
        # If using default list, call domain function but we need to modify it
        # to accept a domain parameter instead of asking for input
        # For now, we can work with the existing code
        domain()  # This will prompt for domain input
    elif args.wordlist:
        # If using custom wordlist, call file_upload with the wordlist path
        # We need to modify file_upload to accept a wordlist path
        # Instead of calling File_Integrity() inside
        file_upload(args.wordlist, domain_main)
