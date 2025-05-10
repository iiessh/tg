import telebot

API_TOKEN = '7672525416:AAFOwY_EOdnwLP5c9PLFljSKV9MYorK7T1U'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Здравствуйте! Пожалуйста, введите ваше ФИО.")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Спасибо, {name}! Теперь пришлите фото чека.")
    bot.register_next_step_handler(message, get_photo)

def get_photo(message):
    if message.content_type == 'photo':
        bot.send_message(message.chat.id, "Спасибо, чек получен!")
    else:
        bot.send_message(message.chat.id, "Это не фото. Попробуйте ещё раз.")
        bot.register_next_step_handler(message, get_photo)

bot.polling()
