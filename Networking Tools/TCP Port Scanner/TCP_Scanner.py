import socket


def TCP_Scanner():

    destination = input("Enter in a domain name or IPv4 Address: ")

    try:
         resolved_ip = socket.gethostbyname(destination)
    except socket.gaierror:
         print("Invalid address/domain")
         return

    open_ports = []
    closed_ports = []


    for port in range (1, 65536):


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)

        try:
            s.connect((resolved_ip, port))
            service_name = socket.getservbyport(port)
            open_ports.append(port)
            print(f"Port is open! {port}, and the service name for the port is {service_name}")
        except (socket.timeout, ConnectionRefusedError):
             closed_ports.append(port)
             print(f"Port closed! {port}")
        except socket.error as e:
            print(f"Error scanning {port}: {e}")
        finally:
            s.close()



    print("\nScan results:")
    print(f"Open ports: {sorted(open_ports)}")
    print(f"Closed ports: {len(closed_ports)}")


if __name__ == "__main__":
    TCP_Scanner()