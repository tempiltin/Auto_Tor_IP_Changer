import os
choice = input('[+] oʻrnatish uchun (Y) ni oʻchirish uchun (N) >> tugmasini bosing')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 lochin.py')
    run('mkdir /usr/share/lochin')
    run('cp lochin.py /usr/share/lochin/lochin.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/lochin/lochin.py "$@"')
    with open('/usr/bin/lochin','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/lochin & chmod +x /usr/share/lochin/lochin.py')
    print('''\n\tabriklaymiz avtomatik Lochin ko'zi Ip Changer muvaffaqiyatli o'rnatildi \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/lochin ')
    run('rm /usr/bin/lochin ')
    print('[!] endi Lochin ko\'zi Ip almashtirgich muvaffaqiyatli olib tashlandi')
