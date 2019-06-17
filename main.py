import telebot;
bot = telebot.TeleBot('891787770:AAFqRNEuDZSQuoN1qJUwF8B5gLyr_Sej9CE');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.find("толстый") !=-1:
        bot.send_message(message.from_user.id, "Сам жрешь много!!!!")

    if message.text.find("але") != -1:
        bot.send_message(message.from_user.id, "Иди на хуй со своим алебежем!!!")

    if message.text.find("отел") != -1:
        bot.send_message(message.from_user.id, "Иди на хуй со своим hotel'ежем!!!")


    bot.send_message(message.from_user.id, "Иди на хуй")


bot.polling(none_stop=True, interval=0)

