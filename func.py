from time import sleep
from telegram import KeyboardButton , ReplyKeyboardMarkup
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from sql_lite import *
from const import *


def user_inf(update,context):
    user_id = update.message.chat_id
    text = update.message.text
    f_n = update.message.from_user.first_name
    return  user_id, text, f_n


def start(update , context):
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    user_id, text, first_name = user_inf(update, context)
    cursor.execute(reg_in_table.format(user_id, first_name))
    conn.commit()


def get_phone(update, context):
    user_id = update.callback_query.from_user.id
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    l = cursor.execute(phone_in_table.format(user_id)).fetchall()
    l = l[0][0]
    b = [KeyboardButton(text=num_quest , request_contact=True)]
    context.bot.send_message(text=num_quest, reply_markup=ReplyKeyboardMarkup([b]), chat_id=user_id)


def update_phone_in_table(update , context):
    number = update.contact.phone_number
    user_id = update.message.from_user.username
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    l = cursor.execute(update_phone_in_table.format(user_id)).fetchall()
    l = l[0][0]
    cursor.execute(update_phone_in_table.format(number, user_id))
    conn.commit()


def select_group(update , context) :

def update_group_in_table(update, context):

def select_time(update, context):

def update_time_in_table(update, context):
