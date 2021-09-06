# -*- coding: utf8 -*-
from paramiko import SSHClient
from paramiko import AutoAddPolicy
import socket, os, getpass

while True:
    try:
        ip = socket.gethostbynameip = socket.gethostbyname('bo-'+input('Введи сап: ')).split('.')
    except:
        print('Сервер магазина не доступен')
        continue
    p = int(input('Номер кассы: '))-1
    kas= f'{ip[0]}.{ip[1]}.{ip[2]}.{str(int(ip[3]) + 14+p)}'

    user= input('Введите пользователя: ')
    secret=getpass.getpass('Введите пароль: ')

    try:

        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname=kas, username=user, password=secret)
    except:
        print('Касса не доступна')
        continue
    data = input('Введи дату формата 20210115: ')
    chk = input('Номер чека: ')
    chk1 = int(chk)-1
    print("Ожидайте, запрос обрабатывается!!!")
    command = """zcat /usr/local/gkretail/pos/log/std_pos.log-"""+data+"""*.gz |sed -n "/BONNR = """+str(chk1)+"""/,/BONNR = """+chk+"""/p" |grep -a 'keyCode=82\|keyCode=10\|keyCode=48\|keyCode=85\|keyCode=27\|keyCode=87\|keyCode=88\|keyCode=86\|keyCode=84\|keyCode=11\|keyCode=74\|keyCode=12\|keyCode=73\|keyCode=77\|keyCode=79\|keyCode=67\|keyCode=11\|keyCode=11\|keyCode=83\|keyCode=68\|keyCode=73\|keyCode=79\|keyCode=66\|keyCode=56\|keyCode=48\|keyCode=49\|keyCode=57\|keyCode=65\|keyCode=75\|keyCode=76\|keyCode=11\|keyCode=11\|keyCode=11\|keyCode=11\|keyCode=11\|keyCode=49\|keyCode=50\|keyCode=51\|keyCode=52\|keyCode=53\|keyCode=54\|keyCode=55\|keyCode=56\|keyCode=57\|keyCode=57\|keyCode=65\|Add customer with number\|scanData=\|TRANSACTION ERROR\|locus\|RESPONSE:\|REQUEST:\|<email>\|HTTP/1.0\|HTTP/1.1\|   URL:\|Общий\|*;Вам начислено:\|Списание\|Точка\|Дата и время\|Списано\|На счете\|Доступных для списания\|CARD_CVV=\|ERROR <ioc>\|Transport error:\|Deferred transaction\|Timeout connection to CLM server!\|No connection to CLM server!'"""
    a, out, b = client.exec_command(command)
    out = out.read().decode().strip().split('\n')
    # print(out)
    for i in out:
        print(i)

    ch = input("Очистить консоль? д/н:" )
    if ch.lower() == 'д':
       os.system("cls")
        # print("консоль очищена")
    elif ch.lower() == 'н':
        continue
    else:
        print("Пожалуйста, введите д") 

    client.close()


