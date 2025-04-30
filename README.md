# Red-Team-Toolkit
This Repository is designed to understand, create and develop a wide variety of Red Team Tools

Currently a long-term project that will host over 20 tools once completed

## topic currently in testing : Networking

Currently focusing on TCP Port Scanner

### Current Standings

Subdomain Enumeration is currently working with only minor issues  
TCP Port Scanner has been created and will feed off of the Subdomain Enumeration Tool  
The Port Scanner will collect available Subdomains and scan for any open ports from port 1 to 65535  
Currently in the process of also adding onto the TCP scanner to add in IP scanning and verbosity options  
Currently using `argparse` import to validate this as a CLI based Tool.
