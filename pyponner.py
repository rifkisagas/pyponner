import socket
import pyfiglet
import termcolor
import signal
from ping import Ping
import time
word = pyfiglet.figlet_format("PyPonner")

class status:
    x = 0

def desc():
    print("\nPyPonner is a simple program used to scan active ports of the targets inputed.\n")

def exitfunc():
    print('\nProgram Exit...')   
    exit(1)

def error_input():
    time.sleep(2)
    main()

def check_ip(input):
    if '.' in input:
        if input.strip().isdigit():
            return
    else:
        print(termcolor.colored(("[!] Invalid target input."),'red'))
        error_input()

def handler(signum, frame):
    exitfunc()

def scan(target, ports):
    status.x = 0
    print('\n' + '[*] Starting Scan For ' + str(target))
    ping = Ping(target)
    if ping.returncode < 1:
        for port in range(1, ports):
            scan_port(target, port)
        if (status.x == 0) :
            print(termcolor.colored(("[-] No Port Opened!"), 'red'))
    else :
        if target.replace('.','').isdigit():
            print(termcolor.colored((f"[-] Target : {target} is unreachable!"), 'red'))
        else :
            print(termcolor.colored((f"[-] Target : {target} is not an IP Address!"), 'red'))


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
    print("\nMultiple target example : 192.168.56.1,192.168.56.2")
    targets = input("[+] Enter Targets (split them by ,): ")
    check_ip(targets)
    print("\nThe inputed ports perform as many iteration as input")
    ports = int(input("[*] Enter How Many Ports You Want To Scan (Max : 65535): "))
    if ports > 65535:
        print(termcolor.colored(('[-] Maximum port input reached!'),'red'))
        error_input()
    else:
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
