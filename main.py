#region import
import telebot
from telebot import types
import time
import random
bot = telebot.TeleBot('5675224712:AAHzlV4fvZC24b5nFdWYV5AgY7iXS8V23Vw')
#endregion import

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup()

    # region Оформляем кнопки que1-que15
    if call.data == 'que1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Осень')
        btn2 = types.InlineKeyboardButton('Весна')
        btn3 = types.InlineKeyboardButton('Лето')
        markup.add(btn1, btn2, btn3)
        message_text = 'Викторина будет идти по хранологии событий. И так, мы начинаем с детства. Первый вопрос:\n*В детстве ты с мамой ездил в Москву. В какое время года это было?*'
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Один')
        btn2 = types.KeyboardButton('Два')
        btn3 = types.KeyboardButton('Три')
        btn4 = types.KeyboardButton('Четыре')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Сколько раз в сутки подзаводят куранты Спасской башни Кремля?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Романист')
        btn2 = types.KeyboardButton('Драматург')
        btn3 = types.KeyboardButton('Поэт')
        btn4 = types.KeyboardButton('Эссеист')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто 1-м получил Нобелевскую премию по литературе?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)


    if call.data == 'que4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('М')
        btn2 = types.KeyboardButton('Н')
        btn3 = types.KeyboardButton('О')
        btn4 = types.KeyboardButton('П')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "С какой буквы начинаются слова, опубликованные в 16-м томе последнего издания Большой советской энциклопедии?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Фонвизин')
        btn2 = types.KeyboardButton('Державин')
        btn3 = types.KeyboardButton('Радищев')
        btn4 = types.KeyboardButton('Карамзин')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто из перечисленных был пажом во времена Екатерины II?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Гафний')
        btn2 = types.KeyboardButton('Кобальт')
        btn3 = types.KeyboardButton('Бериллий')
        btn4 = types.KeyboardButton('Теллур')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Какой химический элемент назван в честь злого подземного гнома?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Тбилиси')
        btn2 = types.KeyboardButton('Ереван')
        btn3 = types.KeyboardButton('Баку')
        btn4 = types.KeyboardButton('Минск')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "В какой из этих столиц бывших союзных республик раньше появилось метро?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('3')
        btn2 = types.KeyboardButton('4')
        btn3 = types.KeyboardButton('5')
        btn4 = types.KeyboardButton('6')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Сколько морей омывают Балканский полуостров?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)




#region start
@bot.message_handler(commands=['start'])
def start(message):

    if message.chat.id != 1208542295:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Видео')
        btn2 = types.KeyboardButton('Приколы')
        btn3 = types.KeyboardButton('Викторина')
        markup.add(btn1, btn2, btn3)
        first_name = message.from_user.first_name
        bot.send_message(message.chat.id, f'Привет, {first_name}! Это бот-викторина, предназначенный для Сергея Алексеевича Казакова.'
                                          f' Ты, конечно, тоже можешь принять участие, но главного приза не будет((((')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Видео')
        btn2 = types.KeyboardButton('Приколы')
        btn3 = types.KeyboardButton('Викторина')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, parse_mode='Markdown', disable_web_page_preview=True,
                         reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Видео')
        btn2 = types.KeyboardButton('Приколы')
        btn3 = types.KeyboardButton('Викторина')
        markup.add(btn1, btn2, btn3)
        bot.send_message(1208542295,
                         f'Папа, с Днём рождения❤! В этом боте ты сможешь посмотреть видео и приколы пожелания. '
                         f'А также пройти викторину, в конце которой ты получишь ГЛАВНЫЙ ПРИЗ😉!')
#endregion start









#region buttons
@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()


    # region Видео
    if get_message_bot == "Видео":
        bot.send_message(message.chat.id, 'Хорошо. Сейчас ты увидишь видео, которое сгенерировала галерея айфона.\n' 
        'Это видео будет наполнено положительными эмоциями и случайно снятыми смешными видео. \n Приятного просмотра!'
                                          , parse_mode='Markdown')
        bot.send_video(message.chat.id, (open('BSF/dr.mp4', 'rb')))

    #endregion Видео


    #region пикчи
    elif get_message_bot == "Приколы":
        bot.send_message(message.chat.id, 'Ты можешь лицезреть приколы с твоими любимыми персонажами и на тему твоего мировосприятия.\n Приятного просмотра!'
                                          , parse_mode='Markdown')
        bot.send_photo(message.chat.id, (open('BSF/Брин.jpg', 'rb')))
        bot.send_photo(message.chat.id, (open('BSF/Матроскин.jpg', 'rb')))
        bot.send_photo(message.chat.id, (open('BSF/Уик.jpg', 'rb')))
        bot.send_photo(message.chat.id, (open('BSF/кот2.jpg', 'rb')))
    #endregion пикчи

    # region quiz
    elif get_message_bot == "Викторина":
            bot.send_message(message.chat.id, f'Папа, сейчас тебе предстоит пройти викторину по главным событиям твоей жизни, в конце которой ты получишь ГЛАВНЫЙ ПРИЗ!'
                                              f'\n*Желаю удачи☺!*',
                             parse_mode='Markdown')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton('Осень', callback_data='que_1')
            btn2 = types.InlineKeyboardButton('Лето', callback_data='que_2')
            btn3 = types.InlineKeyboardButton('Весна', callback_data='que_3')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f'Викторина будет идти по хранологии событий. И так, мы начинаем с детства. Первый вопрос:'
                                              f'\n*В детстве ты с мамой ездил в Москву. В какое время года это было?*',
                             parse_mode='Markdown', reply_markup=markup)


            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton('Редко, раз в год', callback_data='zi_1')
            btn2 = types.InlineKeyboardButton('2-4 раза в год', callback_data='zi_2')
            btn3 = types.InlineKeyboardButton('Довольно часто, раз в 1-2 месяца', callback_data='zi_3')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f'Второй вопрос:\n*Как часто ты уезжаешь в поездки?*',
                             parse_mode='Markdown', reply_markup=markup)

            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton('Редко, раз в год', callback_data='que_1')
            btn2 = types.InlineKeyboardButton('2-4 раза в год', callback_data='que_2')
            btn3 = types.InlineKeyboardButton('Довольно часто, раз в 1-2 месяца', callback_data='poh_3')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f'Третий вопрос:\n*Готов ли ты брать животное с собой в поездки?*',
                             parse_mode='Markdown', reply_markup=markup)


#endregion buttons











if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)