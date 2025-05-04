import socket
import os

def TCP_Port_Scanner(portscanner_path, combined_file):

    if not os.path.exists(portscanner_path): # Checks to see if argparse path exists in main.py
        print(f"Error! File does not exist: {portscanner_path}")
        return

    try:
        destination = socket.gethostbyname(combined_file) # Gets the hostname from the combined file in either Wordlist.py or Subdomain_Enumeration.py
    except socket.gaierror as g:
        print(f"Error! Could not resolve host {g}")
        return

    with open("Port_Results.txt", "w", encoding="utf-8") as results_file: # Creates results file for ports

        successful_ports = []
        unsuccessful_ports = []


        for port in range(1, 65535): # Goes through from port 1 to 10000
                

                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Establishes the beginning of a socket
                except socket.error as e:
                    print(f"Error! Socket Not Established {e}")

                    
                try:
                    s.settimeout(0.1)
                    s.connect((destination, port)) # Checks if a port is online based on the desired DNS
                    successful_ports.append(port)
                except socket.error as e:
                     unsuccessful_ports.append(port)
                finally:
                    s.close()
            

        for port in successful_ports:
            result_line = f"Port Is Available! {port}"
            results_file.write(result_line + "\n")

        if port in unsuccessful_ports:
            result_line = f"Port Is Unavailable! {port}"
            results_file.write(result_line + "\n")
                
            
        
    print(f"\nSummary:")
    print(f"Total Ports Checked: {len(successful_ports) + len(unsuccessful_ports)}")
    print(f"Ports Open: {len(successful_ports)}")
    print(f"Ports Not Open: {len(unsuccessful_ports)}")
