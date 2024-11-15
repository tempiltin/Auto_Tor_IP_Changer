# -*- coding: utf-8 -*-

import time
import os
import subprocess

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if 'install ok installed' in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print("[!] pip3 muvaffaqiyatli o'rnatildi")

try:
    import requests
except ImportError:
    print("[+] python3 so'rovlari o'rnatilmagan")
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed!')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print("[!] tor muvaffaqiyatli o'rnatildi")

os.system("clear")

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
    get_ip = requests.get(url, proxies=proxies)
    return get_ip.text

def change():
    os.system("service tor reload")
    print('[+] Your IP has been changed to: ' + str(ma_ip()))

print(r''' 
                        
 _               _     _         _         _     _ 
| |    ___   ___| |__ (_)_ __   | | _____ ( )___(_)
| |   / _ \ / __| '_ \| | '_ \  | |/ / _ \|/|_  / |
| |__| (_) | (__| | | | | | | | |   < (_) |  / /| |
|_____\___/ \___|_| |_|_|_| |_| |_|\_\___/  /___|_|
                                                   
 Tempiltin                                         
                                                   
            https://tempiltin.uz/                   
Dastur o'quv mashg'ulotlari maqsadida ishlab chiqilgan! 
        ILTIMOS YOMON MAQSADDA FOYDALANMANG!
      
''')
print("\033[1;40;31m https://www.tempiltin.uz /\n")

print("Lochin ko'zi dasturi ishga tushdi!")

time.sleep(3)
print("\033[1;32;40m change your SOCKS to 127.0.0.1:9050 \n")

x = input("[+] Sec ichida IP o'zgartirish vaqti [type=60] >> ")
lin = input("[+] cheksiz IP oʻzgartirish turiga [type=1000] IP-ni necha marta oʻzgartirmoqchisiz [0] >> ")

try:
    x = int(x)
    lin = int(lin)
except ValueError:
    print("Iltimos, butun son kiriting.")
    quit()

if lin == 0:
    while True:
        try:
            time.sleep(x)
            change()
        except KeyboardInterrupt:
            print("\nLochin ko'zi is closed")
            quit()
else:
    for i in range(lin):
        time.sleep(x)
        change()
