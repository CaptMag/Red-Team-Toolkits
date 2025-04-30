import socket
import os

def TCP_Port_Scanner(portscanner_path, combined_file):

    try:
        destination = socket.gethostbyname(combined_file) # Gets the hostname from the combined file in either Wordlist.py or Subdomain_Enumeration.py
    except socket.gaierror:
        print(f"Error! Could not resolve hot {destination}")

        ports = []
        successful_ports = []
        unsuccessful_ports = []


        with open("Port_Results.txt", "w", encoding="utf-8") as results_file: # Creates results file for ports


            for port in range(1, 1001): # Goes through from port 1 to 10000
                    

                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Establishes the beginning of a socket
                        print("TCP Socket has been established!")
                    except socket.error as e:
                        print(f"Error! Socket Not Established {e}")


                    s.connect((destination, port)) # Checks if a port is online based on the desired DNS
                    ports.append(f"Available Ports Online: {ports}")

            if ports:
                successful_ports.append(combined_file)
                result_line = f"Port Is Available! {port}"
                results_file.write(result_line)
            else:
                 unsuccessful_ports.append(combined_file)
                 result_line = f"Port Is Unavailable! {port}"
                 results_file.write(result_line)
                


            if not os.path.exists(portscanner_path): # Checks to see if argparse path exists in main.py
                print(f"Error! File does not exist: {portscanner_path}")
                return
            
    print(f"\nSummary:")
    print(f"Total subdomains checked: {len(ports) + len(ports)}")
    print(f"Subdomains Available: {len(successful_ports)}")
    print(f"Subdomains Not Available: {len(unsuccessful_ports)}")
