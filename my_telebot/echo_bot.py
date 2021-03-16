import telebot
from dotenv import dotenv_values

PATH_TO_TOKEN = '.env'

def get_token(path_to_token):
    my_env_variables = dotenv_values(path_to_token)
    return my_env_variables['TOKEN']


token = get_token(PATH_TO_TOKEN)
bot = telebot.TeleBot(token = token)
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('/start', '/help', '/settings', 'i love you')

@bot.message_handler(commands=['start', 'help', 'settings'])
def send_welcome(message):
	bot.reply_to(message, "Hello! how are you?", reply_markup=keyboard)

"""
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
"""

@bot.message_handler(content_types = ['text'])
def send_text(message):
    if message.text.lower() == 'i love you':
        bot.send_message(message.chat.id, 'I love You to', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'I not understend you.', reply_markup=keyboard)

print('Bot start!')
bot.polling()