import telebot

API_TOKEN = '7672525416:AAFOwY_EOdnwLP5c9PLFljSKV9MYorK7T1U'  # вставьте токен, полученный от BotFather
bot = telebot.TeleBot(API_TOKEN)

# Список разрешённых user_id (для защиты)
ALLOWED_IDS = [383400607]  # замените на реальные Telegram ID пользователей

@bot.message_handler(commands=['start'])
def start_handler(message):
    # Проверяем, разрешен ли пользователь
    if message.from_user.id not in ALLOWED_IDS:
        bot.send_message(message.chat.id, "Извините, у вас нет доступа к боту.")
        return
    bot.send_message(message.chat.id, "Здравствуйте! Я запрошу у вас ФИО, а потом фото чека.")
    bot.send_message(message.chat.id, "Пожалуйста, введите ФИО:")
    bot.register_next_step_handler(message, process_name)

def process_name(message):
    full_name = message.text.strip()
    if not full_name:
        bot.send_message(message.chat.id, "Вы не ввели ФИО. Попробуйте ещё раз:")
        bot.register_next_step_handler(message, process_name)
        return
    # Сохраняем ФИО (в данном простом примере просто пересылаем далее или используем по необходимости)
    # Далее запрашиваем фотографию чека
    bot.send_message(message.chat.id, f"Спасибо, {full_name}. Теперь отправьте, пожалуйста, фото чека об оплате:")
    bot.register_next_step_handler(message, process_photo)

def process_photo(message):
    if message.content_type == 'photo':
        # Получаем file_id последней (наиболее крупной) фотографии
        file_id = message.photo[-1].file_id
        # Здесь можно, например, сохранить file_id или переслать файл администратору
        bot.send_message(message.chat.id, "Фото чека получено. Спасибо!")
    else:
        bot.send_message(message.chat.id, "Это не фотография. Пожалуйста, отправьте именно фото чека:")
        bot.register_next_step_handler(message, process_photo)

# Обработчик для любых других сообщений (по желанию)
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.send_message(message.chat.id, "Отправьте /start для начала.")

bot.polling()  # запускаем бота в режиме опроса (polling):contentReference[oaicite:7]{index=7}
