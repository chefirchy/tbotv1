import telebot
import time
import configparser


config = configparser.ConfigParser()
config.read('connect.ini')
config_data = config['DEFAULT']

bot = telebot.TeleBot(config_data['token'])


# commands
@bot.message_handler(commands=['start', 'help'])
def handle_command_menu(message):
    print("start/help")


# text
@bot.message_handler(content_types=["text"])
def echo_all(message):
    if message.text.lower() == "hello":
        print("hello")


# run bot
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("Connection Error", e)
        time.sleep(15)
