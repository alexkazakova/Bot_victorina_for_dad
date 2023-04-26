#region import
import telebot
from telebot import types
import time
import random
bot = telebot.TeleBot('5786666775:AAEA47o0fdkwSoVPEd99TKu4jEAJCBTThkc')
#endregion import

Users = {}
GIFT = [0, 100, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000, 200000, 400000, 800000, 1500000, 3000000]
n = 15  # диапазон рандома вопросов

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️


@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup()

    # region Оформляем кнопки que1-que15
    if call.data == 'que1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Рязань')
        btn2 = types.InlineKeyboardButton('Джалибат')
        btn3 = types.InlineKeyboardButton('Ташкент')
        markup.add(btn1, btn2, btn3)
        message_text = "Куда была твоя самая первая поездка?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Золотые серьги')
        btn2 = types.InlineKeyboardButton('Цепочка')
        btn3 = types.InlineKeyboardButton('Браслет')
        markup.add(btn1, btn2, btn3)
        message_text = "Какое ювелирное украшение ты украл у бабушки, чтобы подарить девочке на Дент рождения?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('«Преступление и наказание»')
        btn2 = types.InlineKeyboardButton('«Обломов»')
        btn3 = types.InlineKeyboardButton('«Идиот»')
        markup.add(btn1, btn2, btn3)
        message_text = "Про какое произведение в школьные годы ты написал в сочинении на тему «моя любимая книга»?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)


    if call.data == 'que4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('На пиво')
        btn2 = types.InlineKeyboardButton('На телефон')
        btn3 = types.InlineKeyboardButton('На сотовую связь')
        markup.add(btn1, btn2, btn3)
        message_text = "На что ты потратил все свои деньги в Воронеже?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Шапка и куртка')
        btn2 = types.InlineKeyboardButton('Подарок маме')
        btn3 = types.InlineKeyboardButton('Магнитофон')
        markup.add(btn1, btn2, btn3)
        message_text = "Что ты купил на первую зарплату?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Друг')
        btn2 = types.InlineKeyboardButton('Военные')
        btn3 = types.InlineKeyboardButton('МЧСники')
        markup.add(btn1, btn2, btn3)
        message_text = "С кем ты в студенческие годы снимал квартиру?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('В феврале 2003 года')
        btn2 = types.InlineKeyboardButton('В конце января 2003 года')
        btn3 = types.InlineKeyboardButton('В феврале 2004')
        markup.add(btn1, btn2, btn3)
        message_text = "Когда ты устроился в милицию?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('В Тайланд')
        btn2 = types.InlineKeyboardButton('В Египет')
        btn3 = types.InlineKeyboardButton('В Казахстан')
        markup.add(btn1, btn2, btn3)
        message_text = "Куда была ваша с мамой первая совместная поездка?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que9':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Понятно, Майя борщ поела, я себе бутеры сделал')
        btn2 = types.InlineKeyboardButton('Ура')
        btn3 = types.InlineKeyboardButton('Оля, это точно не сын?')
        markup.add(btn1, btn2, btn3)
        message_text = "Когда у тебя родилась дочь, какая была твоя первая фраза?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que10':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('11 мая 2010 года')
        btn2 = types.InlineKeyboardButton('10 мая 2010 года')
        btn3 = types.InlineKeyboardButton('11 мая 2009 года')
        markup.add(btn1, btn2, btn3)
        message_text = "Когда вы с мамой расписались?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que11':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Папа, переодетый в Деда Мороза')
        btn2 = types.InlineKeyboardButton('Чудо')
        btn3 = types.InlineKeyboardButton('Клубника')
        markup.add(btn1, btn2, btn3)
        message_text = "Какой ваш самый изобретательный подарок для дочки?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que12':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Причал Ярового')
        btn2 = types.InlineKeyboardButton('Мамайка, Сочи')
        btn3 = types.InlineKeyboardButton('Хинкальня в Новосибирске')
        markup.add(btn1, btn2, btn3)
        message_text = "Где ваше с мамой главное романтическое место?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que13':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Волгоград')
        btn2 = types.InlineKeyboardButton('Самара')
        btn3 = types.InlineKeyboardButton('Сукко')
        markup.add(btn1, btn2, btn3)
        message_text = "Какой самый первый город мы посмотрели во время нашей поездки по России в 2019 году?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que14':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton('Да!')
        btn2 = types.InlineKeyboardButton('Конечно')
        btn3 = types.InlineKeyboardButton('Безусловно')
        markup.add(btn1, btn2, btn3)
        message_text = "Ты счастлив?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    # endregion que1-15

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


@bot.message_handler(content_types=['text'])
def mess(message):
    if get_message_bot == 'Викторина':
        Users[message.chat.id] = [[], 0]
        print(Users[message.chat.id])
        while True:
            temp = random.randint(1, n)
            if temp not in Users[message.chat.id][0]:
                Users[message.chat.id][0].append(temp)
                print(Users[message.chat.id])
                break
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Начать игру", callback_data='que' + str(temp)))
    bot.send_message(message.chat.id, 'Добро пожаловать в игру\n *"Кто хочет стать миллионером"!*', parse_mode='Markdown', reply_markup=markup)


    get_message_bot = message.text.strip()

    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    if get_message_bot == 'Рязань' or 'Ташкент':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ :(\n Твоя первая поездка была в Джалибат. Ты поехал вместе с бабушкой в команровку')

    elif get_message_bot == 'Джалибат':
        bot.send_message(message.chat.id, 'Это правильный ответ!\nТвоя первая поездка была в Джалибат. Ты поехал вместе с бабушкой в команровку')
    # que6 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que7 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Браслет' or 'Цепочка':
        bot.send_message(message.chat.id, f'Ответ неверный:(\n Ты "позаимствовал" у бабушки золотые серёжки с рубином и подарил их девочке на День рождения')

    elif get_message_bot == 'Золотые серьги':
        bot.send_message(message.chat.id, 'Это правильный ответ!')


    # que7 -------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
    # que8 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == '3':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '4':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '5':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que8 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que8 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Шея':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Уста':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Палец':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que9 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que10 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Шапка':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Болезнь':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш:  рублей', reply_markup=markup)

    elif get_message_bot == 'Печка':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que10 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que11 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == '«Пионеры»':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '«Последний из могикан»':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '«Зверобой»':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que11 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que12 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Драгуны':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Уланы':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Кирасиры':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que12 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que13 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Валентин':
        Users[message.chat.id] = []
        l = len(Users[message.chat.id])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Евгений':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Георгий':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que13 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que14 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Висбаден':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Цербст':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Штеттин':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que14 -------------------------------------------------------------------------------------------------------------------------------------------------------------

    # endregion Обработка правильных и неправильных ответов que1-que15
#endregion buttons
'''










if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)