import socket
import ssl


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


    # Total open and closed ports
    print("\nScan results:")
    print(f"Open ports: {sorted(open_ports)}")
    print(f"Closed ports: {len(closed_ports)}")


if __name__ == "__main__":
    TCP_Scanner()
