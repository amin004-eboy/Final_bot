from telegram.ext import Updater, Dispatcher, Filters, MessageHandler, CommandHandler, CallbackQueryHandler
from func import *
updater = Updater(token=TOKEN, workers = 5)
dispatcher = updater.dispatcher