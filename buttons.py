from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Стартовая клавиатура
start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
    KeyboardButton('/store'),
    KeyboardButton('/mem'),
    KeyboardButton('/quiz'),
    KeyboardButton('/reply_webapp'),
    KeyboardButton('/inline_webapp'),
    KeyboardButton('/registration'))




submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(
    KeyboardButton('да'),
    KeyboardButton('нет')
)


remove_keyboard = ReplyKeyboardRemove()
