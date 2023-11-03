import os , requests , telebot , telebot ; from telebot import types ; from uuid import uuid4 ; ud = str(uuid4()) ; from user_agent import generate_user_agent ; gd = str(generate_user_agent())
import requests;import json;cookies = {
    '_ga': 'GA1.1.868853150.1686571031',
    'uid': '0ab9d21b837ac3f8',
    'clickAds': '53',
    'pushNotification': '92',
    'pushPage': '19',
    'XSRF-TOKEN': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
    'aig_session': 'eyJpdiI6IlFPaGc0UnY2bjNIWmxKeTBIbDVjXC9BPT0iLCJ2YWx1ZSI6IktVck9mTWF5UDdxY3RFXC9WeW5kR0ZTOTM5U3RjalBaSnlSd05mUlhkanN2NStldDhaSWtFXC9IeXFlbFFFNHNrS09VS3J4V2NDVWVpd0lncFljWEhJMGlERWpHSGZ4bWZGQTN5RVF0Mm9jT0NhR0xnRGFEaEs5eTRLSFlCd01OckkiLCJtYWMiOiIwNDEzNDBkNTc2NTRkMTkxODc2ZmUxZTIzOGQ0ODU1MWZmYWQyM2NmNGQ3MGQwZGU0OWUyMjEzMmRhOGU2ODAyIn0%3D',
    '_ga_2S9JP0SPEL': 'GS1.1.1686741984.2.1.1686742384.0.0.0',
};headers = {
    'authority': 'storiesig.info',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"376-nN5i4Qu/s4Ex/bnNvBcI5Wa+U3U"',
    'referer': 'https://storiesig.info/en/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-token': 'null',
    'x-xsrf-token': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
}
import requests;from user_agent import generate_user_agent as ee
def gmail(email):
	try:
		tl=requests.get('https://tlqredes.bbbbbfbbbb.repl.co/').json()['tl'];url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={tl}&_reqid=481859&rt=j';headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '1146',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Google-Accounts-Xsrf': '1',
        'Origin': 'https://accounts.google.com',
        'Referer':
        'https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJvNCbbAigRHG5Ypddwgp39mKdyniOE3D3uLi3iK805IzUq1NNSbRnz7QQ6b_tTu',
        'User-Agent': ee(),
    };data = {
        'datcontinue': 'https://uc.appengine.google.com/_ah/conflogin?state=~AJKiYcGoPiLJb7FyAN6mbCNCjMH037vL_6C39BUsJA2GF6P5lw1fJ6zYEHHUw663dDmmWQqnSQj6F1H89kr0oAzGCTf1OVJVmr9O71L1w89w388Qo8F51B0AsXfY4lW59yc42hfwocycpD-KrQxXpL_wNY1CXqq7EwVgxTdIeLOVnU-5xSbZ8812E9pDOYWDOi2xFjrP52ODHXY16KTZWlHmcwb4WPbjByt1nT71cz8msPMP1rVSoXY',
        'dsh': 'S2080850673:1689863726476816',
        'flowEntry': 'ServiceLogin',
        'ifkv': 'AeDOFXgxTTjgoRCMuYvMYScwDmQo7816fmgZo5HW-2qv1sxmBtxR8_QpcokS3oMTn4QP3Fp_J3h15Q',
        'f.req': '["TL:{}","{}",0,0,1]'.format(tl, email),
        'azt': 'AFoagUWjPq1xG8LVoJkd3pOHgMJrOj0MAA:1689863743434',
        'cookiesDisabled': 'false',
        'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
        'gmscoreversion': 'undefined',
        'flowName': 'GlifWebSignIn',
        'checkConnection': 'youtube:452:0',
        'checkedDomains': 'youtube',
        'pstMsg': '1',
    };req = requests.post(url, headers=headers, data=data).text
		if ('"gf.uar",1') in req:
			pp='ok';return pp
		else:
			pp='stef';return pp
	except:gmail(email)
def info(user):
	try:
		
		url = requests.get(f'https://storiesig.info/api/ig/profile/{user}', cookies=cookies, headers=headers)
		data = json.loads(url.content)
		id = data['result']['id']
		user = data['result']['username']
		bio = data['result']['biography']
		name = data['result']['full_name']
		mn = data['result']['edge_owner_to_timeline_media']['count']
		followed = data['result']['edge_followed_by']['count']
		follow = data['result']['edge_follow']['count']
		img = data['result']['profile_pic_url']
		date=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()['date']
		url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/';head ={
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'Cookie': 'mid=YgzPXAABAAFpu2FvBU3Nz814ooE5; csrftoken=DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW',
'Cookie2': '$Version=1',
'Accept-Language': 'en-GB, en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip'
};data ={
"user_email":f"{user}",
"device_id":"android-ae9d37a73aa41d00",
"guid":"d038a34e-1663-4f2b-af9d-aae995d105c4",
"_csrftoken":"DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW"
};req =requests.post(url,headers = head, data = data)
		if '"status":"ok"' in req.text:
            					rest = req.json()['obfuscated_email']
            					
		else:
            					rest = 'ملاوي'
            				

		tlg = f'''
ᥙ᥉ᥱᖇ —> {user}
ꪀᥲꪔᥱ —> {name}
Ꭵძ —> {id}
ᥱꪔᥲᎥᥣ —> {user}@gmail.com
ƒ᥆ᥣᥣ᥆᭙ᥱᖇ —> {followed} 
ƒ᥆ᥣᥣ᥆᭙Ꭵꪀg —> {follow} 
ხᎥ᥆ —> {bio}
ძᥲƚᥱ—> {date}
 ᖇᥱ᥉ᥱƚ —> {rest}
 ხy : @D_C_F
    ''';return tlg
		
	except:
		
		tlg = f'''

ᥙ᥉ᥱᖇ —>{user}
ꪀᥲꪔᥱ —> H
ᥱꪔᥲᎥᥣ —> {user}@gmail.com
ƒ᥆ᥣᥣ᥆᭙ᥱᖇ -> H 
ƒ᥆ᥣᥣ᥆᭙Ꭵꪀg —> H 
Ꭵძ —> H
ხᎥ᥆ —> H
ძᥲƚᥱ—> H
   BY : @D_C_F
    '''
	return tlg
bot = telebot.TeleBot(input("- Enter Token : "))
@bot.message_handler(commands=['start'])
def srt(message):
	check = types.InlineKeyboardButton(text='دخول ',callback_data='check')
	hg = types.InlineKeyboardMarkup(row_width=1);hg.add(check)
	bot.send_message(message.chat.id,text='مرحبا بك صديقي في بوت صيد متاحات انستغرام اضغط -دخول-للدخول الى البوت',reply_markup=hg)
@bot.callback_query_handler(func=lambda call:True)
def Call(call):
	if call.data=='check':
		sTo = bot.send_message(call.message.chat.id,text=f'- اهلاً بَك عزيزي ارسل الملف الان .')
		bot.register_next_step_handler(sTo,check)
def check(message):
	hit = 0
	unlink = 0
	num = 0
	unava = 0
	try:
		filename = message.document.file_name
		fil = bot.get_file(message.document.file_id)
		dow = bot.download_file(fil.file_path)
		with open(filename, 'wb') as f0:
			f0.write(dow)
			p_file = open(filename, "r")
			mssg=bot.send_message(message.chat.id,text="انتظر قليلا  ...")
	except:
		bot.send_message(message.chat.id,text='''*ارسل ملف صحيح *''',parse_mode="Markdown")
		return
	with open(filename, "r") as f4:
		all_line = f4.readlines()
		allline = len(all_line)
	file = open(filename,'r').read().splitlines()
	for user in file:
		try:
			email = user + '@gmail.com'
			if '_' in user:
				unlink+=1
				num+=1
				continue
			else:
						if requests.get(f'https://apinsta.bbbbbfbbbb.repl.co/Qredes/email={email}').json()['available_instagram']=='good':
							if gmail(user) == 'ok':
								nn = user
								hit+=1
								num+=1
								Ronaldo = types.InlineKeyboardMarkup(row_width=1)
								zr1=types.InlineKeyboardButton(text='- غير متاح في انستغرام : {}'.format(unlink),callback_data='zr1')
								zr2=types.InlineKeyboardButton(text='- غير متاح في جيميل : {}'.format(unava),callback_data='zr2')
								zr3=types.InlineKeyboardButton(text='- متاح : {}'.format(hit),callback_data='zr3')
								zr4=types.InlineKeyboardButton(text='- عدد الفحص : {} \ {}'.format(num,allline),callback_data='zr4')
								zr5=types.InlineKeyboardButton(text='- Contact the developer',url='https://t.me/D_C_F')
								Ronaldo.add(zr3,zr2,zr1,zr4,zr5)
								bot.edit_message_text(chat_id=message.chat.id,message_id=mssg.message_id,text="- بداء الفحص... .",parse_mode='markdown',reply_markup=Ronaldo)
								bot.send_message(message.chat.id,info(user))
							else:
								unava+=1
								num+=1
								Ronaldo = types.InlineKeyboardMarkup(row_width=1)
								zr1=types.InlineKeyboardButton(text='-  غير مرتبط في انستغرام : {}'.format(unlink),callback_data='zr1')
								zr2=types.InlineKeyboardButton(text='- غير متاح في انستغرام : {}'.format(unava),callback_data='zr2')
								zr3=types.InlineKeyboardButton(text='- متاح : {}'.format(hit),callback_data='zr3')
								zr4=types.InlineKeyboardButton(text='- عدد الفحص : {} \ {}'.format(num,allline),callback_data='zr4')
								zr5=types.InlineKeyboardButton(text='-To contact the developer click here',url='https://t.me/D_C_F')
								Ronaldo.add(zr3,zr2,zr1,zr4,zr5)
								bot.edit_message_text(chat_id=message.chat.id,message_id=mssg.message_id,text="- بداء الفحص ...",parse_mode='markdown',reply_markup=Ronaldo)
						else:
							unlink+=1
							num+=1
							Ronaldo = types.InlineKeyboardMarkup(row_width=1)
							zr1=types.InlineKeyboardButton(text='-  غير مرتبط في انستغرام : {}'.format(unlink),callback_data='zr1')
							zr2=types.InlineKeyboardButton(text='- غير متاح في جيميل : {}'.format(unava),callback_data='zr2')
							zr3=types.InlineKeyboardButton(text='- متاح : {}'.format(hit),callback_data='zr3')
							zr4=types.InlineKeyboardButton(text='- عدد الفحص : {} \ {}'.format(num,allline),callback_data='zr4')
							zr5=types.InlineKeyboardButton(text='- -To contact the developer click here',url='https://t.me/D_C_F')
							Ronaldo.add(zr3,zr2,zr1,zr4,zr5)
							bot.edit_message_text(chat_id=message.chat.id,message_id=mssg.message_id,text="- بداء الفحص  .",parse_mode='markdown',reply_markup=Ronaldo)
		except:
		   continue
	bot.send_message(message.chat.id,'تم االانتهاء من الفحص')
if __name__=="__main__":
	bot.infinity_polling()
