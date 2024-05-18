import telebot
from FetchAndTrain import Fetch

bot = telebot.TeleBot("6391937928:AAEqfMyR-xCRVzWeNvWJlxdt1qU_2D3vaSk")

@bot.message_handler(commands=['start', 'help','hi','hello'])
def send_welcome(message):
	bot.reply_to(message, "Select an App\n\n1.Wikipedia\n2.Python Docs\n3.CodeSolveAI\n4.Github")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	try:
		try:
			StackOverFlow = Fetch.FetchAndTrainStackOverFlow(message.text)
			GeekForGeeks = Fetch.FetchAndTrainGeeksForGeeks(message.text)
			Exceptions = Fetch.exceptions(message.text)
			if StackOverFlow != False:
				bot.reply_to(message,StackOverFlow)
			elif GeekForGeeks != False:
				bot.reply_to(message,GeekForGeeks)
			else:
				# bot.reply_to(message,"Can't find a perfect solution")
				bot.reply_to(message,Exceptions)
		except:
			message.text += "stackoverflow geeksforgeek"
			bot.reply_to(message,"Searching")
			StackOverFlow = Fetch.FetchAndTrainStackOverFlow(message.text)
			# GeekForGeeks = Fetch.FetchAndTrainGeeksForGeeks(message.text)
			if StackOverFlow != False:
				bot.reply_to(message,StackOverFlow)
			# elif GeekForGeeks != False:
				# bot.reply_to(message,GeekForGeeks)
			else:
				bot.reply_to(message,Exceptions)
	except:
			# bot.reply_to(message,"Can't find a perfect solution")
			bot.reply_to(message,Exceptions)


bot.infinity_polling()


