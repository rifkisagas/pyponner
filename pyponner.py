import socket
import pyfiglet
import termcolor
import signal
import os
import argparse
import time
word = pyfiglet.figlet_format("PyPonner")

class status:
    x = 0

def desc():
    print("\nPyPonner is a simple program used to scan active ports of the targets inputed.\n")
def exitfunc():
    print('\nProgram Exit...')   
    exit(1)
def check_ip(input):
    if '.' in input:
        if input.strip().isdigit():
            return
    else:
        print(termcolor.colored(("[!]Invalid target input."),'red'))
        time.sleep(2)
        main()
def handler(signum, frame):
    exitfunc()
def scan(target, ports):
    status.x = 0
    print('\n' + '[*] Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)
    if (status.x == 0) :
        print(termcolor.colored(("[-] No Port Opened!"), 'red'))


def scan_port(ipaddress, port):
    sock = socket.socket()
    sock.settimeout(10)
    try:
        sock.connect((ipaddress, port))
        print(termcolor.colored(("[+] Port Opened " + str(port)), 'green'))
        status.x = 1
        sock.close()
    except:
        pass

def main():
    print('\033c')
    print(word)
    # parser = argparse.ArgumentParser(description='Used for scanning active ports of the targets.')
    # parser.parse_args()    
          # prog='pyponner.py',
          # description='Used for scanning active ports of the targets.',
          # epilog)
    print("\nMultiple target example : 192.168.56.1,192.168.56.2")
    targets = input("[+] Enter Targets (split them by ,): ")
    check_ip(targets)
    print("The inputed ports perform as many iteration as input")
    ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
    if ',' in targets:
        print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), ports)
    else:
        scan(targets, ports)
    ask = input("[?] Do you want to scan again? (y/n): ")
    if "y" in ask:
        print('\033c')
        return main()
    else:
        exitfunc()
signal.signal(signal.SIGINT,handler)
main()
