# Red-Team-Toolkit
This Repository is designed to understand, create and develop a wide variety of Red Team Tools

Currently a long-term project that will host over 20 tools once completed

## topic currently in testing : Web Application

Currently focusing on a HTTP Web Crawler

### Current Standings

Subdomain Enumeration is currently working with only minor issues  
TCP Port Scanner has been created and will feed off of the Subdomain Enumeration Tool  
The Port Scanner will collect available Subdomains and scan for any open ports from port 1 to 65535  
Currently in the process of also adding onto the TCP scanner to add in IP scanning and verbosity options  
Currently using `argparse` import to validate this as a CLI based Tool.

## TCP Port Scanner

As of right now, the TCP Port Scanner can be used in 2 ways:  
With a wordlist and by itself

With a wordlist the TCP scanner will be linked with the subdomain enumeration tool, allowing for a multitude of available domains to be ran through the scanner  
for the single TCP Scanner, it will run 1 domain (or IP) at a time, but gives more detailed information such as all the open ports and services (if detected)

currently the TCP Port Scanner has been improved. Through trial and error, the best way to make the program faster was through using concurrent.futures.  
Although the original concept focused around Multithreading, the concurrent.futures provides an easier and faster eay to scan all 65535 ports.  

currently it takes around '30 seconds' to run theough all ports.  
the next step in place is to inplement an 'OS Detection' service for the scanner using 'scapy.all' and focusing on TCP TTL, WindowSize and Headers.  
Added MAC Address pinging through sending an ARP request to a perferred destination

## HTTP(S) Web Crawler

This tool will be used to go through a user selected website and will send `HTTP 1.1 GET/POST REQUESTS`  
This will also try and find any important arguments and pages such as /admin or /dev  
checks for any misconfigured webpages or hidden webpages (may feed in with subdomain enumeration)  
convert HTML files into JSON formatting

## Future Plans

Considering moving `Subdomain Enumeration` into Web Application Tools.  
Adding in a specific tool for `CVE Detection` using parsing from results from the `socket` import
the next steps will likely to be implementing `Firewall Evasion` and `Stealth Scanning` onto Port Scanner.  
Considering changing name of `TCP Port Scanner` to `Network Scanning and Mapping` (basically a mini NMAP)

## Documentation

As of right now, the `subdomain enumeration tool` has an ongoing document being written, specifying how it works, HTTP Requests, A, AAAA, and CNAME records, CT Transparency and more...  
The `TCP Port Scanner` currently does not have an ongoing doc, and will be implemented in the near future.  
Currently ongoing with HTTP(S) Web Crawler Documentation, will be posted with notes and examples alongside the python file itself.

## Current Issues

currently both the `TCP Port Scanner` and `Subdomain Enumeration` are facing printing issues.  
TCP Port Scanner is not properly printing out all the closed ports, what they are and how many open ports and what they are.  
It also faces issues for SSL Wraping certain ports (such as port 443). 

Subdomain Enumeration is currently printing IPv4 Addresses into the `AAAA Records` and not properly printing all IPv6 Addresses
