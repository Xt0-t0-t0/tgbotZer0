import telebot 
from cnfing import tocin
from ailogic import get_class

bot = telebot.TeleBot(tocin)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет я Zer0, скоро я тебя удивлю!
""")


# Обработка всех остальных сообщений с типом контента 'текст' (по умолчанию content_types = ['текст'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = get_class(file_name)
    bot.reply_to(message, result[0])


bot.infinity_polling()



