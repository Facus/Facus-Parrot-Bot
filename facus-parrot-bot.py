############################################################
#	Facus Parrot Bot
#	A bot for Telegram
############################################################


#TeleBot API --> https://github.com/eternnoir/pyTelegramBotAPI
import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Start? *Croaaack*")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Help? *Pripriiipip*")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text + " *Croaaaak!*")

bot.polling()
