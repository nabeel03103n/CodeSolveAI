import telebot
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from FetchAndTrain import Fetch




bot = telebot.TeleBot("6391937928:AAEqfMyR-xCRVzWeNvWJlxdt1qU_2D3vaSk")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello I am here to solve your programming questions")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, Fetch.FetchAndTrainGoogle(message.text))

bot.infinity_polling()


