import telebot

import DB_func
from DB_func import *
from telebot import types

com = {'ITeam': 0,'ATeam': 0}
oprcom = ''

bot = telebot.TeleBot('8163330425:AAHfVz_zXQXsX0H7OzWPUL5UlL1h665QEy0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать в телеграм бот для более удобной и успешной работы!')
    begining(message)


@bot.message_handler(commands=['button'])
def begining(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Добавить баллы')
    but2 = types.KeyboardButton('Все команды в телеграм боте')
    markup.add(but1, but2)
    bot.send_message(message.chat.id, 'Выбирите то что вам требуется', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def cross(message):
    conn = sqlite3.connect("TEAMS.db")
    if message.text == 'Добавить баллы':
        add_points(message, DB_func.db_to_dict(conn))
    elif message.text == 'Все команды в телеграм боте':
        all_commands(message)
    elif message.text in DB_func.db_to_dict(conn).keys():
        adding(message, DB_func.db_to_dict(conn))
    elif message.text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        adding_points_to_command(conn,message)
    elif message.text == 'Назад':
        begining(message)
    else:
        bot.send_message(message.from_user.id, 'Попробуйте ещйё раз, неверная команда')


def adding_points_to_command(conn,message):
    global oprcom
    name = oprcom
    points_to_add = int(message.text)
    cursor = conn.cursor()
    cursor.execute("SELECT points FROM commands WHERE team_name = ?", (name,))
    result = cursor.fetchone()[0]
    if name:
        pr_points = int(result)
        new_points = pr_points + points_to_add
        cursor.execute("UPDATE commands SET points = ? WHERE team_name = ?", (new_points, name))
        conn.commit()
    else:
        print(f"Team '{name}' not found.")
    bot.send_message(message.from_user.id, f'Вы успешно добавили {message.text} балла/ов')
    begining(message)


def adding(message, list):
    global oprcom
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for comand, points in list.items():
        print(comand, points)
        if comand == message.text:
            oprcom = comand
            for i in range(1, 11):
                item = types.KeyboardButton(i)
                markup.add(item)
            item2 = types.KeyboardButton('Назад')
            markup.add(item2)
            bot.send_message(message.from_user.id, 'Выбирите колличество баллов, которые хотите добавить',
                             reply_markup=markup)


def add_points(message, list):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for comand in list.keys():
        item = types.KeyboardButton(comand)
        markup.add(item)
    item2 = types.KeyboardButton('Назад')
    markup.add(item2)
    bot.send_message(message.from_user.id, 'Выбирите команду, которой хотите добавить баллы', reply_markup=markup)


def all_commands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton('Назад')
    markup.add(but)
    bot.send_message(message.from_user.id,
                     'Этот бот умеет:\n1. Добавлять баллы командам (кнопка "Добавить баллы")\n2. Связываться с админами и организаторами (кнопка "Помощь")',
                     reply_markup=markup)




bot.polling(none_stop=True, interval=0)