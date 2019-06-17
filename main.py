import telebot
bot = telebot.TeleBot('813537832:AAHv4gM-545wNaGAcukzlUlYb57do1AT-2Y')


@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    if message.text.lower().find("толстый") != -1:
        bot.send_message(message.chat.id, "Сам жрешь много!!!!")

    elif message.text.lower().find("але") != -1:
        bot.send_message(message.chat.id, "Иди на хуй со своим алебежем!!!")

    elif message.text.lower().find("отел") != -1:
        bot.send_message(message.chat.id, "Иди на хуй со своим hotel'ежем!!!")
    else:
        bot.send_message(message.chat.id, "Иди на хуй")


bot.polling(none_stop=True, interval=0)
