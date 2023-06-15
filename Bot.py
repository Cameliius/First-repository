import telebot
import random

token = '5974118032:AAE8XoXRLYnByuj9AAb_rSbnKrOVWGqb4Hg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Стихотворение")
    button2 = telebot.types.KeyboardButton("Факт")
    button3 = telebot.types.KeyboardButton("Котик")
    button4 = telebot.types.KeyboardButton("Во что поиграть?")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 9))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


genre = ''


@bot.message_handler(commands=['game'])
def send_game(message):
    msg = bot.send_message(message.from_user.id,
                           'Выберите жанр, который вам по душе:''\n''Хоррор''\n''Стратегия''\n''Приключения')
    bot.register_next_step_handler(msg, message_input_step)


@bot.message_handler(content_type=['text'])
def message_input_step(message):
    global genre
    genre = message.text

    games_horror = ['Fran Bow', 'Sally Face', 'Bandy', 'Hollow Knight', 'Doki Doki Literary Club']
    games_strategy = ['Cult of Lamb', 'Genshin impact', 'Dota 2', 'For the King', 'Splay the Spire']
    games_adventures = ['Genshin impact', 'Litle nightmares', 'Litle nightmares 2', 'The Forest', 'Cyberpunk 2077']

    if genre == 'Хоррор':
        use_game = random.choice(games_horror)
    elif genre == 'Стратегия':
        use_game = random.choice(games_strategy)
    else:
        use_game = random.choice(games_adventures)
    bot.send_message(message.from_user.id, use_game)


@bot.message_handler(content_types=['text'])
def anwer(message):
    if message.text == 'Стихотворение':
        send_poem(message)
    if message.text == 'Котик':
        send_cat(message)
    if message.text == 'Во что поиграть?':
        send_game(message)


bot.polling()
