import pyowm
import telebot
bot = telebot.TeleBot('1409123204:AAFIRTO6q5ylxam-f8ANCODsq4n2CJIvnd4')

token = '1b697c0eb4524ed4a5777b807b1c035c'
owm = pyowm.OWM(token, language = "RU")
class weathers:
	def get(city, chatid):
		try:
			plase = owm.weather_at_place(city)
			w = plase.get_weather()	
			temp = w.get_temperature('celsius')['temp']
			status = w.get_detailed_status()
			bot.send_message(chatid, 'Сейчас в '+city+'e: '+str(temp)+' градусов, погода: '+ status)
		except:
			bot.send_message(chatid, 'Прости, я не смог найти такого города:((((')


