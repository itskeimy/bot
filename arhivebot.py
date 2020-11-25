from logs import logins
logins = logins('logins.db')
from weather import weathers

from stonks import parser
logn = []
chat = []

import telebot
from telebot import types
bot = telebot.TeleBot('1409123204:AAFIRTO6q5ylxam-f8ANCODsq4n2CJIvnd4')

log = {}
cht = {}
cht1 = {}
nick = {}
stonk= {}
name_pass = {}
admins = []
bans = []

def keyboarde():
	markup = types.ReplyKeyboardMarkup(True, True)
	btn1 = types.KeyboardButton('/menu')
	markup.add(btn1)
	return markup

@bot.message_handler(content_types=['sticker'])
def start(message):
	global nick
	cht[message.from_user.id] = [False]
	for i in chat:
		if i == message.from_user.id:
			cht[message.from_user.id][0] = True
	if cht[message.from_user.id][0] == True:
		for i in chat:
			bot.send_message(i, nick[message.chat.id]+': ')
			bot.send_sticker(i, message.sticker.file_id)
		cht[message.chat.id][0] = False	
	else:	
		bot.send_message(message.from_user.id, 'я тебя не понял) напиши /help')

@bot.message_handler(content_types=['voice'])
def start(message):
	global nick
	cht[message.from_user.id] = [False]
	for i in chat:
		if i == message.from_user.id:
			cht[message.from_user.id][0] = True
	if cht[message.from_user.id][0] == True:
		for i in chat:
			bot.send_message(i, nick[message.chat.id]+': ')
			bot.send_voice(i, message.voice.file_id)
		cht[message.chat.id][0] = False	
	else:	
		bot.send_message(message.from_user.id, 'я тебя не понял) напиши /help')


@bot.message_handler(content_types=['photo'])
def start(message):
	global nick
	cht[message.from_user.id] = [False]
	for i in chat:
		if i == message.from_user.id:
			cht[message.from_user.id][0] = True
	if cht[message.from_user.id][0] == True:
		for i in chat:
			if message.caption == None:
				bot.send_photo(i, message.photo[0].file_id, nick[message.chat.id]+': ')
			else:	
				bot.send_photo(i, message.photo[0].file_id, nick[message.chat.id]+': '+str(message.caption))
		cht[message.chat.id][0] = False	
	else:	
		bot.send_message(message.from_user.id, 'я тебя не понял) напиши /help')

@bot.message_handler(content_types=['text'])		
def start(message): 
	global log, chat
	if message.text == '/start' or message.text == '/help':
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.add(callback_button1)
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBmxpfuLhBNVf8Sy2R4Jrlhx7MOeiTQAAClAADwZxgDOp3kvJEPX0ZHgQ')
		bot.send_message(message.from_user.id, 'для начала войдите в меню и там войдите или зарегистрируйтесь, потом вы можете пойти в анонимный чат или посмотреть погоду(бот в стадии разработки и это даже не 1 версия)',
			reply_markup=keyboard);

	elif message.text == '/menu':
		keyboard = types.InlineKeyboardMarkup()
		log[message.chat.id] = [False]
		for i in logn:
			if i == message.chat.id:
				log[message.chat.id][0] = True
		if log[message.from_user.id][0] == True:
			callback_button1 = types.InlineKeyboardButton(text="выход", callback_data="log")
			log[message.chat.id][0] = False
		else:	
			callback_button1 = types.InlineKeyboardButton(text="вход", callback_data="log")
		callback_button2 = types.InlineKeyboardButton(text="регистрация", callback_data="reg")
		callback_button3 = types.InlineKeyboardButton(text="чат", callback_data="chat")
		callback_button4 = types.InlineKeyboardButton(text="погода", callback_data="weather")
		callback_button5 = types.InlineKeyboardButton(text="курс", callback_data="stonk")
		keyboard.row(callback_button1, callback_button2)
		keyboard.row(callback_button3)
		keyboard.row(callback_button4)
		keyboard.row(callback_button5)
		bot.send_message(message.chat.id, 'Меню', reply_markup=keyboard)

	elif message.text == '/chat':
		cht1[message.chat.id] = [False]
		for i in chat:
			if i == message.chat.id:
				cht1[message.chat.id][0] = True
		if cht1[message.chat.id][0] == True:
			chat.remove(message.chat.id)
			keyboard = types.InlineKeyboardMarkup()
			callback_button4 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
			keyboard.row(callback_button4)
			bot.send_message(message.chat.id, 'вы вышли из чата', reply_markup=keyboard)
			cht1[message.chat.id] = [False]	
		else:	
			bot.send_message(message.chat.id, 'я тебя не понял)')			
	else:
		cht[message.from_user.id] = [False]
		for i in chat:
			if i == message.from_user.id:
				cht[message.from_user.id][0] = True
		if cht[message.from_user.id][0] == True:
			for i in chat:
				bot.send_message(i, nick[message.from_user.id]+': '+message.text);
			cht[message.from_user.id][0] = False	
		else:	
			bot.send_message(message.from_user.id, 'я тебя не понял) напиши /help');	


def get_login(message):
	global name_pass
	name_pass[message.chat.id] = [str(message.text), '']
	bot.send_message(message.chat.id, 'ок, дальше введите пароль');
	bot.register_next_step_handler(message, get_pass);

def get_pass(message):	
	global name_pass
	name_pass[message.chat.id][1] = str(message.text) 
	b = logins.check_user(name_pass[message.chat.id][0], name_pass[message.chat.id][1])
	if b == 0:
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="попробовать еще раз", callback_data="log")
		callback_button2 = types.InlineKeyboardButton(text="зарегистрироваться", callback_data="reg")
		keyboard.row(callback_button1)
		keyboard.row(callback_button2)
		bot.send_message(message.chat.id, 'не верный логин или пароль введите /log или \nзарегистрируйтесь /reg', 
			reply_markup=keyboard);
	elif b == 1:
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(message.chat.id, 'вы успешно вошли', reply_markup=keyboard)
		logn.append(message.chat.id)
		b = 0	
	print(logn)
	del name_pass[message.chat.id]

def get_reg_login(message):
	global name_pass
	name_pass[message.from_user.id] = ['', '']
	name_pass[message.from_user.id][0] = str(message.text)
	bot.send_message(message.from_user.id, 'ок, напишите пароль')
	bot.register_next_step_handler(message, get_reg_password);

def get_reg_password(message):
	global name_pass
	name_pass[message.from_user.id][1] = str(message.text)
	logins.add_user(name_pass[message.from_user.id][0], name_pass[message.from_user.id][1])
	keyboard = types.InlineKeyboardMarkup()
	callback_button1 = types.InlineKeyboardButton(text="меню", callback_data="menu")
	keyboard.row(callback_button1)
	bot.send_message(message.from_user.id, 'ты успешно зарегистрироавлся, можешь войти через /menu', 
		reply_markup=keyboard)
	del name_pass[message.from_user.id]

def get_nick(message):
	global nick
	nick[message.from_user.id] = str(message.text)
	
	keyboard = types.InlineKeyboardMarkup()
	callback_button1 = types.InlineKeyboardButton(text="начать chatitsa:DD", callback_data="chat")
	keyboard.add(callback_button1)
	bot.send_message(message.from_user.id, 'ты успешно сделал себе ник', reply_markup=keyboard)
	print(nick)
def get_city(message):
	weathers.get(message.text, message.chat.id)	
	keyboard = types.InlineKeyboardMarkup()
	callback_button1 = types.InlineKeyboardButton(text="меню", callback_data="menu")
	keyboard.add(callback_button1)
	bot.send_message(message.from_user.id, 'Такая погода', reply_markup=keyboard)	

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.data == "yes":
		bot.send_message(call.message.chat.id, 'копка сработала, поздравляю')
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok:D")
		bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEBm35fuSFREMD3uScetruj4h6tlPuAwAACkgADwZxgDJfRP7BLhoVkHgQ')
	elif call.data == "no":
		bot.send_message(call.message.chat.id, 'копка не сработала, поздравляю')
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok:D")
		bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEBm4JfuSFd39ErV3M32vLMUa8mPUQbDwACiwADwZxgDNnGqDS9YJ2FHgQ')
	elif call.data == "chat":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		cht1[call.message.chat.id] = [False]
		for i in chat:
			if i == call.message.chat.id:
				cht1[call.message.chat.id][0] = True
		if cht1[call.message.chat.id][0] == True:
			chat.remove(call.message.chat.id)
			bot.send_message(call.message.chat.id, 'вы вышли из чата')
			cht1[call.message.chat.id] = [False]	
		else:	
			cht[call.message.chat.id] = [False]
			for i in logn:
				if i == call.message.chat.id:
					cht[call.message.chat.id][0] = True
			if cht[call.message.chat.id][0] == True:
				if (call.message.chat.id in nick) == True:
					chat.append(call.message.chat.id)
					bot.send_message(call.message.chat.id, 'вы вошли в чат, чтобы выйти напиши /chat')
				elif (call.message.chat.id in nick) == False:
					bot.send_message(call.message.chat.id, 'напишите свой ник для чата(поменять пока что нельзя поэтому подумай, можно смайлики)');
					bot.register_next_step_handler(call.message, get_nick)
			else:			
				keyboard = types.InlineKeyboardMarkup()
				callback_button1 = types.InlineKeyboardButton(text="Войти", callback_data="log")
				callback_button2 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
				keyboard.row(callback_button1)
				keyboard.row(callback_button2)
				bot.send_message(call.message.chat.id, 'Вы не вошли еще', reply_markup=keyboard)

	elif call.data == "log":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		log[call.message.chat.id] = [False]
		for i in logn:
			if i == call.message.chat.id:
				log[call.message.chat.id] = [True]
		if log[call.message.chat.id][0] == True:
			logn.remove(call.message.chat.id)
			keyboard = types.InlineKeyboardMarkup()
			callback_button1 = types.InlineKeyboardButton(text="меню", callback_data="menu")
			keyboard.add(callback_button1)
			bot.send_message(call.message.chat.id, 'Вы успешно вышли', reply_markup=keyboard)
			log[call.message.chat.id][0] = False
		else:	
			bot.send_message(call.message.chat.id, 'Введите логин')
			bot.register_next_step_handler(call.message, get_login)

	elif call.data == "reg":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		log[call.message.chat.id] = [False]
		for i in logn:
			if i == call.message.chat.id:
				log[call.message.chat.id][0] = True
		if log[call.message.chat.id][0] == True:
			keyboard = types.InlineKeyboardMarkup()
			callback_button1 = types.InlineKeyboardButton(text="меню", callback_data="menu")
			keyboard.add(callback_button1)
			bot.send_message(call.message.chat.id, 'вы уже вошли какой регаться', reply_markup=keyboard)	
			del log[call.message.chat.id]
		else:	
			bot.send_message(call.message.chat.id, 'хорошо, введите логин для своего пользователя')
			bot.register_next_step_handler(call.message, get_reg_login)		

	elif call.data == "menu":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		log[call.message.chat.id] = [False]
		for i in logn:
			if i == call.message.chat.id:
				log[call.message.chat.id][0] = True
		if log[call.message.chat.id][0] == True:
			callback_button1 = types.InlineKeyboardButton(text="выход", callback_data="log")
			log[call.message.chat.id][0] = False
		else:	
			callback_button1 = types.InlineKeyboardButton(text="вход", callback_data="log")
		callback_button2 = types.InlineKeyboardButton(text="регистрация", callback_data="reg")
		callback_button3 = types.InlineKeyboardButton(text="чат", callback_data="chat")
		callback_button4 = types.InlineKeyboardButton(text="погода", callback_data="weather")
		callback_button5 = types.InlineKeyboardButton(text="курс", callback_data="stonk")
		keyboard.row(callback_button1, callback_button2)
		keyboard.row(callback_button3)
		keyboard.row(callback_button4)
		keyboard.row(callback_button5)
		bot.send_message(call.message.chat.id, 'Меню', reply_markup=keyboard)

	elif call.data == "weather":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		bot.send_message(call.message.chat.id, 'Напишите город, в котором вы хотите узнать температуру')
		bot.register_next_step_handler(call.message, get_city);

	elif call.data == "stonk":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Доллар", callback_data="money_d")
		callback_button2 = types.InlineKeyboardButton(text="Евро", callback_data="money_e")
		callback_button3 = types.InlineKeyboardButton(text="Гривна", callback_data="money_g")
		callback_button4 = types.InlineKeyboardButton(text="Тенге", callback_data="money_t")
		callback_button5 = types.InlineKeyboardButton(text="Биткоин", callback_data="money_btc")
		callback_button6 = types.InlineKeyboardButton(text="Эфириум", callback_data="money_eth")
		keyboard.row(callback_button1, callback_button2)
		keyboard.row(callback_button3, callback_button4)
		keyboard.row(callback_button5, callback_button6)
		bot.send_message(call.message.chat.id, 'выберите валюту',
			reply_markup=keyboard);
	elif call.data == "money_d":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(call.message.chat.id, 'Простите но это займет некоторое время :((')
		money = parser.get('dollar')
		bot.send_message(call.message.chat.id, 'Доллар стоит: '+money+' руб', reply_markup=keyboard)	

	elif call.data == "money_e":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(call.message.chat.id, 'Простите но это займет некоторое время :((')
		money = parser.get('eur')
		bot.send_message(call.message.chat.id, 'Евро стоит: '+money+' руб', reply_markup=keyboard)

	elif call.data == "money_g":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(call.message.chat.id, 'Простите но это займет некоторое время :((')
		money = parser.get('grivn')
		bot.send_message(call.message.chat.id, 'Гривна стоит: '+money+' руб', reply_markup=keyboard)

	elif call.data == "money_t":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(call.message.chat.id, 'Простите но это займет некоторое время :((')
		money = parser.get('tenge')
		bot.send_message(call.message.chat.id, 'Тенге стоит: '+money+' руб', reply_markup=keyboard)

	elif call.data == "money_btc":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(call.message.chat.id, 'Простите но это займет некоторое время :((')
		money = parser.get('btc')
		bot.send_message(call.message.chat.id, 'Биткоин стоит: '+money+' руб', reply_markup=keyboard)	

	elif call.data == "money_eth":
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
		bot.answer_callback_query(call.id)
		keyboard = types.InlineKeyboardMarkup()
		callback_button1 = types.InlineKeyboardButton(text="Меню", callback_data="menu")
		keyboard.row(callback_button1)
		bot.send_message(call.message.chat.id, 'Простите но это займет некоторое время :((')
		money = parser.get('eth')
		bot.send_message(call.message.chat.id, 'Эфириум стоит: '+money+' руб', reply_markup=keyboard)								
				
				
bot.polling(none_stop=True, interval=0)