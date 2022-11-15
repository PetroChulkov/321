import telebot
from telebot import types # для указание типов

bot = telebot.TeleBot('')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет")
    btn2 = types.KeyboardButton("Стикер")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Привет"):
        bot.send_message(message.chat.id, text="Здорова, {0.first_name}!".format(message.from_user))
    elif(message.text == "Стикер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Верх")
        btn2 = types.KeyboardButton("Низ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Нажми на кнопку", reply_markup=markup)
    elif (message.text == "Верх"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGUsljZsF4gG9Hji4CO8WL86o_IMP-AQACEwAD82PELEa2umP0z2LtKwQ")

    elif message.text == "Низ":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGUstjZsF7R0MaKFA3iJcOJmYPGP2TDgACFAAD82PELDe9XbRJXFcrKwQ")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Привет")
        button2 = types.KeyboardButton("Стикер")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Кнопки для кого были придуманы?!")




bot.polling(none_stop=True)




