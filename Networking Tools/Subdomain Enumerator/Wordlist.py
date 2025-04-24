from Subdomain_Enumerator import Windows_script
import os
import subprocess

def List():
    file_input = input("Enter File: ")
    if not os.path.exists(file_input):
        print(f"Error! File does not exist: {file_input}")
    else:
        with open(file_input) as f:
            content = f.readlines()
            print(content)

def file_upload(content, domain_main):
    Windows_script()
    for f in List():

        combined_file = content + domain_main

        count = 0

        try:

            check_wordlist = subprocess.run(["nslookup", combined_file], stderr=subprocess.DEVNULL)

            check_wordlist = check_wordlist.decode('utf-8').replace("\r", "")

            if "Name:" in check_wordlist or "Addresses:" in check_wordlist:
                count += 1

            if count >= 1:
                print(f"Subdomains Available: {count}")
            else:
                print(f"Subdomains Not Available: {count}")

        except subprocess.CalledProcessError:
            print(f"Subdomain does not exist: {check_wordlist}")
