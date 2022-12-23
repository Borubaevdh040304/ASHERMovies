import telebot
from decouple import config


token = config('TOKEN')

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('link')
button2 = telebot.types.KeyboardButton('transition')
keyboard.add(button1, button2)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет выбери кнопку')
    bot.send_photo(message.chat.id,'https://www.mos.ru/upload/newsfeed/newsfeed/GL(188851).jpg')
    bot.register_next_step_handler(message,reply_to_button)
    
# @bot.(commands=['photo'])
# def get_photo(message):
# bot.send_photo(message.chat.id,'https://www.mos.ru/upload/newsfeed/newsfeed/GL(188851).jpg')

@bot.message_handler(func=lambda x:True)
def reply_to_button(message):
    if message.text == 'link':
        bot.send_message(message.chat.id, 'http://127.0.0.1:8000/admin/')
    elif message.text == 'transition':
        bot.send_message(message.chat.id, 'http://127.0.0.1:8000/docs/')
    else:
        bot.send_message(message.id,'Click on the button')
        bot.register_next_step_handler(message,reply_to_button)

bot.polling(none_stop=True, interval=0)


