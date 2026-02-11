import telebot
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '¡Hola Marco! Kilo Claw Automation está ONLINE. Envíame un archivo .csv de Cube ACR para procesarlo.')

if __name__ == '__main__':
    print('Bot iniciado...')
    bot.polling()
