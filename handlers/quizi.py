import asyncio
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import random

async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='button1')
    keyboard.add(button)
    question = 'RM or Barcelona'
    answer = ['RM', 'Barcelona', 'Оба']
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button2 = InlineKeyboardButton('Далее', callback_data='button2')
    keyboard.add(button2)
    question = 'Dota2 or CS.GO'
    answer = ['Dota2', 'CS.GO']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="Ехх ты",
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button3 = InlineKeyboardButton('Далее', callback_data='button3')
    keyboard.add(button3)
    question = 'MARVEL or ANIME'
    answer = ['MARVEL', 'Оба', 'ANIME']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Неправильный выбор ...',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_4(call: types.CallbackQuery):
    button4 = InlineKeyboardButton('Далее', callback_data='button4')
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button4)
    question = 'Saske or Kaneki'
    answer = ['Saske', 'Оба', 'Kaneki']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Жалко что ты не р ...',
        open_period=60,
        reply_markup=keyboard
    )


async def game_dice(message: types.Message):
    games = ['⚽️', '🎰', '🏀', '🎯', '🎳', '🎲']
    user_dice = await bot.send_dice(chat_id=message.chat.id, emoji=games[5])  # '🎲' - символ кости
    bot_dice = await bot.send_dice(chat_id=message.chat.id, emoji=games[5])


    user_value = user_dice.dice.value
    bot_value = bot_dice.dice.value
    await asyncio.sleep(4)
    if user_value > bot_value:
        await message.answer("Вы выиграли!")
    elif user_value < bot_value:
        await message.answer("Бот выиграл!")
    else:
        await message.answer("Ничья!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text=['button1'])
    dp.register_callback_query_handler(quiz_3, text=['button2'])
    dp.register_callback_query_handler(quiz_4, text=['button3'])
    dp.register_message_handler(game_dice, commands=['game'])
