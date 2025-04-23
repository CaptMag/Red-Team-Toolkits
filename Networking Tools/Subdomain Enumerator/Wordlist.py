from Subdomain_Enumerator import Windows_script, Linux_script
import os

def Wordlist():
    file_input = input("Enter File: ")
    if not os.path.exists(file_input):
        print(f"Error! File does not exist: {file_input}")
    else:
        with open(file_input) as f:
            content = f.readlines()
            print(content)