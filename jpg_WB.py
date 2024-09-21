import telebot, requests, os
from PIL import Image
bot = telebot.TeleBot('TOKEN')
directory = "/Users/ldlolcl/Downloads"

@bot.message_handler(commands=['start'])
def start(message):
	print_bot = '👋 Добро пожаловать в бот, который поможет скачать JPG картинки с карточки товара Wildberries'
	print(print_bot)
	bot.send_message(message.chat.id, print_bot)
	print_bot = '🔢 Просто пришли мне артикул товара и получи картинки в хорошем качестве'
	bot.send_message(message.chat.id, print_bot)

@bot.message_handler(content_types=['text'])
def article(message):
	art = str(message.text)
	print(art)
	if art.isdigit() == False:
		print_bot = '⚠️ Введен некорректный артикул, пожалуйства введите только цифры'
		print(print_bot)
		bot.send_message(message.chat.id, print_bot)
	else:
		print_bot = '🔄 Пожалуйста подождите, это может занять некоторое время'
		print(print_bot)
		bot.send_message(message.chat.id, print_bot)
		os.mkdir(directory+"/"+art)
		vol = int(art[:-5])
		print(vol)
		if 0 <= vol <= 143: b = '01'
		elif 144 <= vol <= 287: b = '02'
		elif 288 <= vol <= 431: b = '03'
		elif 432 <= vol <= 719: b = '04'
		elif 720 <= vol <= 1007: b = '05'
		elif 1008 <= vol <= 1061: b = '06'
		elif 1062 <= vol <= 1115: b = '07'
		elif 1116 <= vol <= 1169: b = '08'
		elif 1170 <= vol <= 1313: b = '09'
		elif 1314 <= vol <= 1601: b = '10'
		elif 1602 <= vol <= 1655: b = '11'
		elif 1656 <= vol <= 1919: b = '12'
		elif 1920 <= vol <= 2045: b = '13'
		elif 2046 <= vol <= 2189: b = '14'
		elif 2190 <= vol <= 2405: b = '15'
		elif 2406 <= vol <= 2621: b = '16'
		elif 2622 <= vol <= 2837: b = '17'
		else: b = '18'
		print(b)
		for n in range(1,30+1):
			try:
				url = "https://basket-"+str(b)+".wbbasket.ru/vol"+art[:-5]+"/part"+art[:-3]+"/"+art+"/images/big/"+str(n)+".webp"
				img = requests.get(url)
				img_file = open(directory+"/"+art+"/"+str(b)+"_"+str(n)+".webp", "wb")
				img_file.write(img.content)
				img_file.close() 
				im = Image.open(directory+"/"+art+"/"+str(b)+"_"+str(n)+".webp").convert("RGB")
				im.save(directory+"/"+art+"/"+str(n)+".jpg","jpeg")
				bot.send_document(message.chat.id, open(directory+"/"+art+"/"+str(n)+".jpg", 'rb'))
				os.remove(directory+"/"+art+"/"+str(n)+".jpg")
			except:
				continue
			finally:
				try:
					os.remove(directory+"/"+art+"/"+str(b)+"_"+str(n)+".webp")
				except:
					continue
		print_bot = '✅ Выгрузка завершена'
		print(print_bot)
		bot.send_message(message.chat.id, print_bot)
		os.rmdir(directory+"/"+art)

#RUN
bot.polling(none_stop=True)