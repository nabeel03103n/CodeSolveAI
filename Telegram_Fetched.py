import telebot
from telebot import types
from FetchAndTrain import Fetch

MAIN_FUNCTION = ""

bot = telebot.TeleBot("6391937928:AAEqfMyR-xCRVzWeNvWJlxdt1qU_2D3vaSk")

@bot.message_handler(commands=['start', 'help','hi','hello'])
def app_selector(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    wikipediaBtn = types.InlineKeyboardButton('Wikipedia',callback_data='wikipedia')
    PythonDocsBtn = types.InlineKeyboardButton('Python Docs',callback_data='python_docs')
    CodeSolveAIBtn = types.InlineKeyboardButton('CodeSolveAI',callback_data='codesolveai')
    GithubBtn = types.InlineKeyboardButton('Github',callback_data='github')
    markup.add(wikipediaBtn,PythonDocsBtn,CodeSolveAIBtn,GithubBtn)
    bot.reply_to(message,"Select an App",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def funcs(callback):
    global MAIN_FUNCTION
    if callback.data == 'wikipedia':
        bot.reply_to(callback.message, "You selected Wikipedia")
        MAIN_FUNCTION = "wikipedia"
    elif callback.data == 'python_docs':
        bot.reply_to(callback.message, "You selected Python Docs")
        MAIN_FUNCTION = "pythondocs"

    elif callback.data == 'codesolveai':
        bot.reply_to(callback.message, "You selected CodeSolveAI")
        MAIN_FUNCTION = "codesolveai"

    elif callback.data == 'github':
        bot.reply_to(callback.message, "You selected Github")
        MAIN_FUNCTION = "GitHub"


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        if MAIN_FUNCTION == "codesolveai":
            bot.reply_to(message,Fetch.FetchAndTrainStackOverFlow(message.text))
        elif MAIN_FUNCTION == "pythondocs":
            bot.reply_to(message,Fetch.PythonOrg(message.text))
        elif MAIN_FUNCTION == "GitHub":
            bot.reply_to(message,"This application is still under maintainance")
        elif MAIN_FUNCTION == "wikipedia":
            result = Fetch.FetchWikipedia(message.text)
            bot.reply_to(message,result)
            Fetch.speaker(result)
            bot.send_audio(chat_id=message.chat.id,audio=open("text_for_telegram.mp3",'rb'))


    except:
            bot.reply_to(message,"Bad Gataway\n\n For this you should use other apps")
            app_selector(message)

bot.infinity_polling()