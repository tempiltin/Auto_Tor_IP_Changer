# -*- coding: utf-8 -*-

import time
import os
import subprocess

try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
def ma_ip():
    url='http://checkip.amazonaws.com'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;40m \n
 _               _     _         _         _     _ 
| |    ___   ___| |__ (_)_ __   | | _____ ( )___(_)
| |   / _ \ / __| '_ \| | '_ \  | |/ / _ \|/|_  / |
| |__| (_) | (__| | | | | | | | |   < (_) |  / /| |
|_____\___/ \___|_| |_|_|_| |_| |_|\_\___/  /___|_|
                                                   
 Tempiltin   
                V 2.1
from mrFD
''')
print("\033[1;40;31m https://tempiltin.uz/\n")

os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] How many times do you want to change your IP? enter to infinite IP change] >> ") or "0"

try:
    lin = int(lin)

    if lin == 0:
        print("Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            try:
                time.sleep(int(x))  # Assuming 'x' is defined earlier in your code
                change()  # Assuming 'change()' is defined elsewhere
            except KeyboardInterrupt:
                print('\nAuto IP changer is closed.')
                break
    else:
        for _ in range(lin):
            time.sleep(int(x))  # Assuming 'x' is defined earlier in your code
            change()  # Assuming 'change()' is defined elsewhere

except ValueError:
    print("Invalid input. Please enter a valid number.")