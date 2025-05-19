import argparse
from Wordlist import file_upload
from Subdomain_Enumerator import domain
from Port_Scanner import TCP_Port_Scanner

def parse_arguments():
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    
    # Subdomain enumeration options (mutually exclusive with each other)
    enum_group = parser.add_mutually_exclusive_group()
    enum_group.add_argument("-d", "--default", action="store_true", help="Use default prefix list")
    enum_group.add_argument("-w", "--wordlist", type=str, help="Path to custom wordlist file")
    
    # Port scanner option (can be used with enumeration)
    parser.add_argument("-p", "--portscanner", action="store_true", help="Scan ports on discovered subdomains")
    
    # Results path option
    parser.add_argument("--results-path", type=str, default="Port_Results.txt",
                       help="Path to save port scanning results (default: Port_Results.txt)")
    
    # Required domain argument
    parser.add_argument("domain", help="Target domain name")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    # Extract the domain from command line arguments
    domain_main = args.domain
    results_file = None
    
    # Handle subdomain enumeration
    if args.default:
        # Modify domain() to accept and return values
        results_file = domain(domain_main)
    elif args.wordlist:
        results_file = file_upload(args.wordlist, domain_main)
    
    # Handle port scanning if requested
    if args.portscanner:
        # scan_target = results_file if results_file else domain_main
        TCP_Port_Scanner(args.results_path)