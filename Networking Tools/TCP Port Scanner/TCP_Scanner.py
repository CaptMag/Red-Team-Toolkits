import socket
import ssl
import concurrent.futures
from scapy.all import *


def TCP_Scanner(destination, resolved_ip, port):


    # Lists for both open and closed ports
    open_ports = []
    closed_ports = []

    request = b"GET / HTTP/1.0\r\n\r\n" # sends HTTP GET Request to server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # created the socket connections

    try:
        s.settimeout(0.1) # a port wait time or 1 milisecond



        if port in [443, 465, 636, 993, 995, 8443]:

            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            s.connect((resolved_ip, port))
            s = context.wrap_socket(s, server_hostname=destination)
        else:
            s.connect((resolved_ip, port))
        
        service_name = socket.getservbyport(port) # tries to get the service of a running port
        s.sendall(request) # sends data to server

        request = s.recv(4096) # receives answer from server
        open_ports.append(port)
        print(f"[OPEN PORT]: {port} | [SERVICE]: {service_name} | [BANNER]: {request.decode()}") # prints open port and service name and banner
    




    except (socket.timeout, ConnectionRefusedError):
            closed_ports.append(port)
            print(f"[PORT CLOSED] {port}") # prints any closed ports


    except socket.error as e:
        print(f"Error scanning {port}: {e}") # any errors in the process will be printed

    finally:
        s.close() # closes the socket, and then loops back until all 65535 ports are completed



def threadpoolexecutor(destination):
        
        try:
            resolved_ip = socket.gethostbyname(destination) # if they choose a domain name, it will be converted to an IPv4
        except socket.gaierror:
            print("Invalid address/domain")
            return

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:


            open_ports = [] # list for all open ports
        

            future_to_port = {executor.submit(TCP_Scanner, destination, resolved_ip, port): port for port in range (1, 65536)} # goes through TCP function and through the range of ports

            for future in concurrent.futures.as_completed(future_to_port): # For loops the future_to_port through all the ports in order to scan faster
                    # port = future_to_port[future]
                    results = future.result()
                    if results:
                        open_ports.append(results) # Append results

            # Total open and closed ports
            print("\nScan results:")
            print(f"Open ports: {sorted(open_ports)}")
            print(f"Closed ports: {65535 - len(open_ports)}")

def os_fingerprinting(destination, open_ports):
    
    data_sent = IP(dst=destination)/TCP(dport=open_ports, flags="S", seq=102) # Sends a TCP Packet to a specific destination
    result = sr1(data_sent, timeout=2, verbose=0)


    # Checks the Time Till Live for a packet, and depending on the answer, prints its likely operating system
    if result.ttl <= 64:
        print(f"[+] TTL from {destination} | Response Time {result.ttl} | Likely a Linux Machine")
    elif result.ttl == 128:
        print(f"[+] TTL from {destination} | Response Time {result.ttl} | Likely a Windows Machine")
    elif result.ttl == 255:
        print(f"[+] TTL from {destination} | Response Time {result.ttl} | Likely a Cisco Machine")
    else:
         print(f"[-] Error! Could not find TTL for {destination}")
         

if __name__ == "__main__":

    destination = input("Enter in a domain name or IPv4 Address: ") # Asks a user for a specified domain name or IPv4 address

threadpoolexecutor(destination)
os_fingerprinting(destination, 80)
