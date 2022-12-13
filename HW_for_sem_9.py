import telebot
from random import randint


bot = telebot.TeleBot("", parse_mode=None)
calc = False
game = False
win_number = 0
steps = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "/game \n/count")

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.
@bot.message_handler(commands=['game'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я загадал число от 1 до 1000, попробуй его угадать")
    global game
    global win_number
    game = True
    win_number = randint(1, 1000)

# Задача 1. Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9
@bot.message_handler(commands=['count'])
def send_welcome(message):
    global calc
    calc = True
    bot.send_message(message.chat.id, "Введите выражение в формате: X + Y * Z")



@bot.message_handler(content_types=['text'])
def message_listener(message):
    global game
    global calc
    global steps
    if game:
        if message.text.isdigit():
            message_number = int(message.text)
            if message_number == win_number:
                game = False
                bot.send_message(message.chat.id,
                                 f'Верно! Я загадывал число {win_number}. Тебе понадобилось {steps} ходов')
                steps = 0
            elif message_number > win_number:
                steps += 1
                bot.send_message(message.chat.id, 'Меньше')
            elif message_number < win_number:
                steps += 1
                bot.send_message(message.chat.id, 'Больше')
        else:
            print('Нужно ввести число')
    elif calc:
        message_list = message.text.split()

        result = int(message_list[2]) * int(message_list[4]) + int(message_list[0])
        bot.send_message(message.chat.id, f'Получилось {result}')
        calc = False


bot.infinity_polling()