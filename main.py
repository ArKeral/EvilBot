import telebot;
bot = telebot.TeleBot('891787770:AAFqRNEuDZSQuoN1qJUwF8B5gLyr_Sej9CE');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Иди на хуй")


bot.polling(none_stop=True, interval=0)

