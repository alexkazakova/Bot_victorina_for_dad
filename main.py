# region import
import telebot
from telebot import types
import time
import random

bot = telebot.TeleBot("5675224712:AAHzlV4fvZC24b5nFdWYV5AgY7iXS8V23Vw")
# endregion import

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
BUTTON = {}

LIST_OF_TRUE_ANSWER = [
    'Вы продолжаете двигаться в правильном направлении!',
    'Отлично! Так держать!',
    'Прекрасно! Вы на верном пути!',
    'Хорошая работа! Продолжайте в том же духе!',
    'Вы отлично справляетесь! Продолжайте!',
    'Отлично! Вы уверенно продвигаетесь вперед!',
    'Вы просто супер! Мы продолжаем двигаться дальше!',
    'Прекрасный ответ! Следующим шагом будет...',
    'Мне нравится ваша работа! Продолжайте в том же духе!',
    'Хорошая работа! Следующий вопрос...',
    'Отличный ответ! Давайте перейдем к следующему вопросу!',
    'Вы продолжаете поражать меня своими знаниями!',
    'Это был легкий вопрос для вас! Следующий шаг...',
    'Вы готовы к новым вызовам!',
    'Великолепно! Так держать!',
    'Я в восторге от вашей работ! Продолжайте в том же духе!',
    'Вы справляетесь невероятно хорошо! Так держать!',
    'Вы просто молодец! Следующим шагом будет...',
    'Прекрасная работа! Вы продолжаете двигаться дальше!',
    'Я впечатлен вашими знаниями! Продолжайте так же!'
]

LIST_OF_FALSE_ANSWER = [
    'Неудачный ответ. Давайте перейдем к следующему вопросу.',
    'К сожалению, это неправильный ответ. Следующий вопрос...',
    'Неверный ответ. Попробуйте следующий вопрос!',
    'Это неправильный ответ, но следующий вопрос будет проще!',
    'К сожалению, это неправильный ответ. Давайте перейдем дальше.',
    'Неправильно. Но у вас есть еще шанс. Следующий вопрос...',
    'Попробуйте еще раз. Следующий вопрос будет легче!',
    'Неравильно. Но вы можете восстановиться на следующем вопросе!',
    'К сожалению, это неправильный ответ. Следующим шагом будет...',
    'Это неправильный ответ, но не расстраивайтесь. Давайте перейдем к следующему вопросу.',
    'Увы, это неправильный ответ. Следующий вопрос может вас удивить!',
    'Неправильно. Но не отчаивайтесь, следующий вопрос будет проще!',
    'К сожалению, вы не угадали. Давайте перейдем к следующему вопросу.',
    'Это неправильный ответ. У вас есть еще много шансов на успех!',
    'Не получилось. Но не расстраивайтесь, следующий вопрос уже близко!',
    'К сожалению, вы ошиблись. Но не беда, следующий вопрос...',
    'Это неправильный ответ. Попробуйте лучше на следующем вопросе!',
    'Неудачный ответ. Но следующий вопрос будет проще!',
    'К сожалению, это неверный ответ. Но не отчаивайтесь, следующий вопрос...',
    'Неправильно. Но вы можете исправиться на следующем вопросе!'
]

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup()

    # region Обработали que1 вопрос
    if call.data in ("que1_1", "que1_2", "que1_3"):
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][0].message_id)
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][1].message_id)
        BUTTON[call.message.chat.id] = [0, 0]

        if call.data == "que1_1":
            # bot.send_photo()
            bot_message_id1 = bot.send_message(call.message.chat.id, f"{random.choice(LIST_OF_TRUE_ANSWER)}\nМое пояснение")
        else:
            # bot.send_photo()
            bot_message_id1 = bot.send_message(call.message.chat.id, f"{random.choice(LIST_OF_FALSE_ANSWER)}\nМое пояснение")

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Рязань', callback_data="que2_1")
        btn2 = types.InlineKeyboardButton('Джалибат', callback_data="que2_2")
        btn3 = types.InlineKeyboardButton('Ташкент', callback_data="que2_3")
        markup.add(btn1, btn2, btn3)
        message_text = "Куда была твоя самая первая поездка?"
        bot_message_id2 = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
        BUTTON[call.message.chat.id] = [bot_message_id1, bot_message_id2]
    # endregion Обработали que1 вопрос

    # region Обработали que2 вопрос
    elif call.data in ("que2_1", "que2_2", "que2_3"):
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][0].message_id)
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][1].message_id)
        BUTTON[call.message.chat.id] = [0, 0]

        if call.data == "que2_2":
            # bot.send_photo()
            bot_message_id1 = bot.send_message(call.message.chat.id, f"{random.choice(LIST_OF_TRUE_ANSWER)}\nМое пояснение")
        else:
            # bot.send_photo()
            bot_message_id1 = bot.send_message(call.message.chat.id, f"{random.choice(LIST_OF_FALSE_ANSWER)}\nМое пояснение")

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Золотые серьги', callback_data="que3_1")
        btn2 = types.InlineKeyboardButton('Цепочка', callback_data="que3_2")
        btn3 = types.InlineKeyboardButton('Браслет', callback_data="que3_3")
        markup.add(btn1, btn2, btn3)
        message_text = "Какое ювелирное украшение ты украл у бабушки, чтобы подарить девочке на Дент рождения?"
        bot_message_id2 = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
        BUTTON[call.message.chat.id] = [bot_message_id1, bot_message_id2]
    # endregion Обработали que2 вопрос

    # region Обработали que4 вопрос
    elif call.data in ("que3_1", "que3_2", "que3_3"):
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][0].message_id)
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][1].message_id)
        BUTTON[call.message.chat.id] = [0, 0]

        if call.data == "que3_1":
            # bot.send_photo()
            bot_message_id1 = bot.send_message(call.message.chat.id, f"{random.choice(LIST_OF_TRUE_ANSWER)}\nМое пояснение")
        else:
            # bot.send_photo()
            bot_message_id1 = bot.send_message(call.message.chat.id, f"{random.choice(LIST_OF_FALSE_ANSWER)}\nМое пояснение")

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('«Преступление и наказание»', callback_data="que4_1")
        btn2 = types.InlineKeyboardButton('«Обломов»', callback_data="que4_2")
        btn3 = types.InlineKeyboardButton('«Идиот»', callback_data="que4_3")
        markup.add(btn1, btn2, btn3)
        message_text = "Про какое произведение в школьные годы ты написал в сочинении на тему «моя любимая книга»?"
        bot_message_id2 = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
        BUTTON[call.message.chat.id] = [bot_message_id1, bot_message_id2]
    # endregion Обработали que4 вопрос


    #
    # if call.data == 'que4':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('На пиво')
    #     btn2 = types.InlineKeyboardButton('На телефон')
    #     btn3 = types.InlineKeyboardButton('На сотовую связь')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "На что ты потратил все свои деньги в Воронеже?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que5':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Шапка и куртка')
    #     btn2 = types.InlineKeyboardButton('Подарок маме')
    #     btn3 = types.InlineKeyboardButton('Магнитофон')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Что ты купил на первую зарплату?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que6':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Друг')
    #     btn2 = types.InlineKeyboardButton('Военные')
    #     btn3 = types.InlineKeyboardButton('МЧСники')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "С кем ты в студенческие годы снимал квартиру?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que7':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('В феврале 2003 года')
    #     btn2 = types.InlineKeyboardButton('В конце января 2003 года')
    #     btn3 = types.InlineKeyboardButton('В феврале 2004')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Когда ты устроился в милицию?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que8':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('В Тайланд')
    #     btn2 = types.InlineKeyboardButton('В Египет')
    #     btn3 = types.InlineKeyboardButton('В Казахстан')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Куда была ваша с мамой первая совместная поездка?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que9':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Понятно, Майя борщ поела, я себе бутеры сделал')
    #     btn2 = types.InlineKeyboardButton('Ура')
    #     btn3 = types.InlineKeyboardButton('Оля, это точно не сын?')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Когда у тебя родилась дочь, какая была твоя первая фраза?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que10':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('11 мая 2010 года')
    #     btn2 = types.InlineKeyboardButton('10 мая 2010 года')
    #     btn3 = types.InlineKeyboardButton('11 мая 2009 года')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Когда вы с мамой расписались?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que11':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Папа, переодетый в Деда Мороза')
    #     btn2 = types.InlineKeyboardButton('Чудо')
    #     btn3 = types.InlineKeyboardButton('Клубника')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Какой ваш самый изобретательный подарок для дочки?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que12':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Причал Ярового')
    #     btn2 = types.InlineKeyboardButton('Мамайка, Сочи')
    #     btn3 = types.InlineKeyboardButton('Хинкальня в Новосибирске')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Где ваше с мамой главное романтическое место?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que13':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Волгоград')
    #     btn2 = types.InlineKeyboardButton('Самара')
    #     btn3 = types.InlineKeyboardButton('Сукко')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Какой самый первый город мы посмотрели во время нашей поездки по России в 2019 году?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    #
    # if call.data == 'que14':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    #     btn1 = types.InlineKeyboardButton('Да!')
    #     btn2 = types.InlineKeyboardButton('Конечно')
    #     btn3 = types.InlineKeyboardButton('Безусловно')
    #     markup.add(btn1, btn2, btn3)
    #     message_text = "Ты счастлив?"
    #     bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    # region Показали, где спрятан подарок
    elif call.data in ("que16_1", "que16_2", "que16_3"):
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][0].message_id)
        bot.delete_message(call.message.chat.id, BUTTON[call.message.chat.id][1].message_id)
        BUTTON[call.message.chat.id] = [0, 0]

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Получить подарок', callback_data="get_gift")
        markup.add(btn1)
        message_text = "Какой-то текст по типу: спасибо, что прошел мою викторину, получи подарок: "
        bot_message_id2 = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
        BUTTON[call.message.chat.id] = [bot_message_id1, bot_message_id2]

    elif call.data == "get_gift":
        bot.send_message(call.message.chat.id, 'Вот твой подарок')
    # endregion Показали, где спрятан подарок


# region Команда: start
@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.id != 1208542295:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Видео")
        btn2 = types.KeyboardButton("Приколы")
        btn3 = types.KeyboardButton("Викторина")
        markup.add(btn1, btn2, btn3)
        first_name = message.from_user.first_name
        bot.send_message(
            message.chat.id,
            f"Привет, {first_name}! Это бот-викторина, "
            f"предназначенный для Сергея Алексеевича Казакова."
            f" Ты, конечно, тоже можешь принять участие, "
            f"но главного приза не будет((((",
            parse_mode="Markdown",
            reply_markup=markup,
        )

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Видео")
        btn2 = types.KeyboardButton("Приколы")
        btn3 = types.KeyboardButton("Викторина")
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            1208542295,
            f"Папа, с Днём рождения❤! В этом боте ты "
            f"сможешь посмотреть видео и приколы пожелания. "
            f"А также пройти викторину, в конце которой ты получишь ГЛАВНЫЙ ПРИЗ😉!",
            parse_mode="Markdown",
            reply_markup=markup,
        )


# endregion Команда: start


@bot.message_handler(content_types=["text"])
def mess(message):
    get_message_bot = message.text.strip()

    # region Кнопка: Видео
    if get_message_bot == "Видео":
        bot.send_message(
            message.chat.id,
            "Хорошо. Сейчас ты увидишь видео, которое сгенерировала галерея айфона.\n"
            "Это видео будет наполнено положительными эмоциями "
            "и случайно снятыми смешными видео. \n Приятного просмотра!",
            parse_mode="Markdown",
        )
        bot.send_video(message.chat.id, (open("BSF/dr.mp4", "rb")))

    # endregion Кнопка: Видео

    # region Кнопка: пикчи
    elif get_message_bot == "Приколы":
        bot.send_message(
            message.chat.id,
            "Ты можешь лицезреть приколы с твоими любимыми "
            "персонажами и на тему твоего мировосприятия.\n Приятного просмотра!",
            parse_mode="Markdown",
        )
        bot.send_photo(message.chat.id, (open("BSF/Брин.jpg", "rb")))
        bot.send_photo(message.chat.id, (open("BSF/Матроскин.jpg", "rb")))
        bot.send_photo(message.chat.id, (open("BSF/Уик.jpg", "rb")))
        bot.send_photo(message.chat.id, (open("BSF/кот2.jpg", "rb")))
    # endregion Кнопка: пикчи

    # region Кнопка: quiz
    elif get_message_bot == "Викторина":
        bot_message_id1 = bot.send_message(message.chat.id,
                          f"Папа, сейчас тебе предстоит пройти викторину по главным "
                          f"событиям твоей жизни, в конце которой ты получишь ГЛАВНЫЙ ПРИЗ!"
                          f"\n*Желаю удачи☺!*", parse_mode="Markdown")

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Осень", callback_data="que1_1")
        btn2 = types.InlineKeyboardButton("Лето", callback_data="que1_2")
        btn3 = types.InlineKeyboardButton("Весна", callback_data="que1_3")
        markup.add(btn1, btn2, btn3)
        bot_message_id2 = bot.send_message(message.chat.id,
                                          f"Викторина будет идти по хранологии событий. И так, мы начинаем с детства. Первый вопрос:"
                                          f"\n*В детстве ты с мамой ездил в Москву. В какое время года это было?*",
                                          parse_mode="Markdown", reply_markup=markup)
        BUTTON[message.chat.id] = [bot_message_id1, bot_message_id2]
    # endregion Кнопка: quiz


if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)
