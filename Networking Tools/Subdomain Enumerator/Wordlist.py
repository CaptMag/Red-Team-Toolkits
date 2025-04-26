import os
import subprocess


def file_upload(wordlist_path, domain_main):
    # Read the wordlist file directly
    if not os.path.exists(wordlist_path):
        print(f"Error! File does not exist: {wordlist_path}")
        return
    
    # Initialize counters
    successful_subdomains = []
    failed_subdomains = []
    A_Records = []
    AAAA_Records = []
    CNAME_Records = []
    
    # Read and process the file
    try:
        with open(wordlist_path, "r", encoding="utf-8") as f:
            # Add a period to each prefix if it doesn't already have one
            prefixes = []
            for line in f:
                prefix = line.strip()
                if prefix:  # Skip empty lines
                    if not prefix.endswith('.'):
                        prefix += '.'
                    prefixes.append(prefix)
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Process each prefix
    with open("Subdomain_Results.txt", "w", encoding="utf-8") as results_file:
        for prefix in prefixes:
            combined_file = prefix + domain_main
            
            try:
                output = subprocess.check_output(["nslookup", combined_file], stderr=subprocess.DEVNULL)
                decoded = output.decode('utf-8').replace("\r", "")
                lines = decoded.splitlines()  # Fixed: added parentheses
                
                has_record = False
                record_info = []
                
                for line in lines:
                    if line.startswith("Address:") and "." in line:  # A Record (IPv4)
                        ip = line.split("Address:")[1].strip()
                        A_Records.append((combined_file, ip))
                        record_info.append(f"A: {ip}")
                        has_record = True
                        
                    elif line.startswith("Address:") and ":" in line:  # AAAA Record (IPv6)
                        ip = line.split("Address:")[1].strip()
                        AAAA_Records.append((combined_file, ip))
                        record_info.append(f"AAAA: {ip}")
                        has_record = True
                        
                    elif "canonical name" in line:  # CNAME Record
                        cname = line.split("canonical name")[1].strip().rstrip(".")
                        CNAME_Records.append((combined_file, cname))
                        record_info.append(f"CNAME: {cname}")
                        has_record = True
                
                if has_record:
                    successful_subdomains.append(combined_file)
                    result_line = f"Subdomain exists: {combined_file} [{', '.join(record_info)}]\n"
                    results_file.write(result_line)
                    print(result_line.strip())
                else:
                    failed_subdomains.append(combined_file)
                    result_line = f"Subdomain does not exist: {combined_file}\n"
                    results_file.write(result_line)
                    
            except subprocess.CalledProcessError:
                failed_subdomains.append(combined_file)
                results_file.write(f"Lookup failed for: {combined_file}\n")
                print(f"Lookup failed for: {combined_file}")

    # Print summary
    print(f"\nSummary:")
    print(f"Total subdomains checked: {len(successful_subdomains) + len(failed_subdomains)}")
    print(f"Subdomains Available: {len(successful_subdomains)}")
    print(f"Subdomains Not Available: {len(failed_subdomains)}")
    print(f"A Records found: {len(A_Records)}")
    print(f"AAAA Records found: {len(AAAA_Records)}")
    print(f"CNAME Records found: {len(CNAME_Records)}")
