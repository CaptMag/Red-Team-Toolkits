import socket


def TCP_Scanner():

    destination = input("Enter in a domain name or IPv4 Address: ") # Asks a user for a specified domain name or IPv4 address

    try:
         resolved_ip = socket.gethostbyname(destination) # if they choose a domain name, it will be converted to an IPv4
    except socket.gaierror:
         print("Invalid address/domain")
         return

    # Lists for both open and closed ports
    open_ports = []
    closed_ports = []


    for port in range (1, 65536):


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # created the socket connections
        s.settimeout(0.1) # a port wait time or 1 milisecond

        try:
            s.connect((resolved_ip, port)) # tries to connect a port to the user specified host name
            service_name = socket.getservbyport(port) # tries to get the service of a running port
            open_ports.append(port)
            print(f"Port is open! {port}, and the service name for the port is {service_name}") # prints open port and service name
        except (socket.timeout, ConnectionRefusedError):
             closed_ports.append(port)
             print(f"Port closed! {port}") # prints any closed ports
        except socket.error as e:
            print(f"Error scanning {port}: {e}") # any errors in the process will be printed
        finally:
            s.close() # closes the socket, and then loops back until all 65535 ports are completed


    # Total open and closed ports
    print("\nScan results:")
    print(f"Open ports: {sorted(open_ports)}")
    print(f"Closed ports: {len(closed_ports)}")


if __name__ == "__main__":
    TCP_Scanner()
