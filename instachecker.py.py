#!/usr/bin/python
# Behdad Ahmadi Code Developed <3 By icg

# Respect To all Coders !
# pip install requests
# pip install colorama

import requests, sys, random, string, time, os, hmac, hashlib, json
from colorama import Fore, Style

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                  _           _               _               _             
                 (_)         | |             | |             | |            
                  _ _ __  ___| |_ __ _    ___| |__   ___  ___| | _____ _ __ 
                 | | '_ \/ __| __/ _` |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
                 | | | | \__ \ || (_| | | (__| | | |  __/ (__|   <  __/ |   
                 |_|_| |_|___/\__\__,_|  \___|_| |_|\___|\___|_|\_\___|_|                                                                                    
                        Iran-Cyber.NeT - Instagram id Checker V1.0                                        
                              instagram.com/localroot



"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



cls()
print_logo()
try:
    __lan = int(sys.argv[1])
except IndexError:
    print Fore.YELLOW + '-----------------------------------------'
    print Fore.RED + '[*]' + Fore.YELLOW + ' Python ' + Fore.GREEN + 'Script.py ' + Fore.WHITE + 'length'
    print(Style.RESET_ALL)
    sys.exit()



def HMAC(keyz):
    key = '3f0a7d75e094c7385e3dbaa026877f2e067cbd1a4dbcf3867748f6b26f257117'
    hash = hmac.new(key, msg=keyz, digestmod=hashlib.sha256)
    return hash.hexdigest()

def randomString(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def randomword(__lan):
   return ''.join(random.choice(string.lowercase) for i in range(__lan))

sys.stdout.write(Fore.GREEN + '    [' + Fore.RED + '~' + Fore.GREEN + ']' + Fore.YELLOW + ' Please Wait')
for n in range(3):
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(0.2)
print ''

while True:
    Headers = {
        'User-Agent': 'Instagram 7.1.1 Android (21/5.0.2; 480dpi; 1080x1776; LGE/Google; Nexus 5; hammerhead; hammerhead; en_US)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1'}
    username = randomword(__lan)
    sess = requests.Session()
    sess.get('https://instagram.com', headers=Headers)
    guid = randomString(8) + '-' + randomString(4) + "-" + randomString(4) + '-' + randomString(4) + '-' +randomString(12)
    device_id = 'android-' + str(HMAC(str(random.randint(1000, 9999))))[0:min(64, 16)]
    information = {'username': username, 'first_name': 'joseph', 'password': 'Lo3', 'email': 'James@gmail.com', 'device_id': device_id, 'guid': guid}
    js = json.dumps(information)
    payload = {'signed_body': HMAC(js) + '.' + js, 'ig_sig_key_version': '4'}
    postHeaders = {'Host': 'i.instagram.com',
                    'User-Agent': 'Instagram 7.1.1 Android (21/5.0.2; 480dpi; 1080x1776; LGE/Google; Nexus 5; hammerhead; hammerhead; en_US)',
                    'Accept-Language': 'en-US',
                    'Accept-Encoding': 'gzip',
                    'Cookie2': '$Version=1',
                    'X-IG-Connection-Type': 'WIFI',
                    'X-IG-Capabilities': 'BQ=='
                    }
    try:
        x = sess.post('https://i.instagram.com/api/v1/accounts/create/', headers=postHeaders, data=payload, timeout=10)
        result = json.loads(x.content)
        if result['status'] != 'fail':
            if "This username isn't available" in x.content:
                print Fore.GREEN + '    [' + Fore.RED + '-' + Fore.GREEN + ']' + Fore.YELLOW + ' username: ' + Fore.RED + username + Fore.YELLOW + ' Not Available'
            else:
                print Fore.GREEN + '    [' + Fore.RED + '-' + Fore.GREEN + ']' + Fore.YELLOW + ' username: ' + Fore.RED + username + Fore.GREEN + ' Available'
                open('Results__.txt', 'a').write(username + '\n')
    except requests.exceptions.ConnectTimeout:
        pass
