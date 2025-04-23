import argparse

# Intializing Argument

parser = argparse.ArgumentParser(description="A Program to find available subdomains via lists or APIs")

# Command to add a user chosen wordlist

parser.add_argument('-wordlist', help="Enter in a wordlist to scan specific subdomains")