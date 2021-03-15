import telebot
from dotenv import dotenv_values

PATH_TO_TOKEN = '.env'

def get_token(path_to_token):
    my_env_variables = dotenv_values(path_to_token)
    return my_env_variables['TOKEN']


token = get_token(PATH_TO_TOKEN)
bot = telebot.TeleBot(token = token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()