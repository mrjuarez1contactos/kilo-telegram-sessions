import telebot
import os
from dotenv import load_dotenv

# Carga variables de entorno
load_dotenv()

# Token directo para evitar fallos de lectura
TOKEN = '8548624508:AAFHsIMNXUdsMn2Zuiy5M3a72xi6b3dF_No'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '¡SISTEMA ACTIVO! Hola Marco, Kilo Claw está escuchando desde la nube.')

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.file_name.endswith('.csv'):
        bot.reply_to(message, 'He recibido tu archivo CSV de Cube ACR. ¡Pronto podré procesarlo!')
    else:
        bot.reply_to(message, 'Por favor, envía un archivo con extensión .csv')

if __name__ == '__main__':
    print('Iniciando bot en modo Polling...')
    # El bot se queda encendido esperando mensajes reales
    bot.infinity_polling() 
