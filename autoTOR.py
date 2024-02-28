# -*- coding: utf-8 -*-

import time
import os
import subprocess




try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print("[!] pip3 muvaffaqiyatli o'rnatildi")



try:

    import requests
except Exception:
    print("[+] python3 so'rovlari o'rnatilmagan")
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print("[!]tor muvaffaqiyatli o'rnatildi" )

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;40m \n
                _         
    ,..-,
         ,;;f^^"""-._
        ;;'          `-.
       ;/               `.
       ||  _______________\_______________________
       ||  |HHHHHHHHHHPo"~~\"o?HHHHHHHHHHHHHHHHHHH|
       ||  |HHHHHHHHHP-._   \,'?HHHHHHHHHHHHHHHHHH|
        |  |HP;""?HH|    """ |_.|HHP^^HHHHHHHHHHHH|
        |  |HHHb. ?H|___..--"|  |HP ,dHHHPo'|HHHHH|
        `| |HHHHHb.?Hb    .--J-dHP,dHHPo'_.rdHHHHH|
         \ |HHHi.`;;.H`-./__/-'H_,--'/;rdHHHHHHHHH|
           |HHHboo.\ `|"\"/"\" '/\ .'dHHHHHHHHHHHH|
           |HHHHHHb`-|.  \|  \ / \/ dHHHHHHHHHHHHH|
           |HHHHHHHHb| \ |\   |\ |`|HHHHHHHHHHHHHH|
           |HHHHHHHHHb  \| \  | \| |HHHHHHHHHHHHHH|
           |HHHHHHHHHHb |\  \|  |\|HHHHHHHHHHHHHHH|
           |HHHHHHHHHHHb| \  |  / dHHHHHHHHHHHHHHH|
           |HHHHHHHHHHHHb  \/ \/ .fHHHHHHHHHHHHHHH|
           |HHHHHHHHHHHHH| /\ /\ |HHHHHHHHHHHHHHHH|
           |""""""""""""""""""""""""""""""""""""""| \n
           
      |##########| |########| |########| 
          |##|     |#|    |#| |#|    |#| 
          |##|     |#|    |#| |#| /###/
          |##|     |#|    |#| |#| \#\
          |##|     |########| |#|  \#\

Dastur o'quv mashg'ulotlari maqsadida ishlab chiqilgan! \n
        ILTIMOS YOMON MAQSADDA FOYDALANMANG ! \n
      
      
''')
print("\033[1;40;31m https://www.tempiltin.uz /\n")

os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] Sec ichida IP o'zgartirish vaqti [type=60] >> ")
lin = input("[+] cheksiz IP oʻzgartirish turiga [type=1000] IP-ni necha marta oʻzgartirmoqchisiz [0] >>")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\nauto tor is closed ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
