from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import logging
import os

token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

Admins = [5154278138]

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(admin, "Bot has started successfully!")

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Your tg id - {message.from_user.id}\n')

@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'images.th.jpg')

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='Это мем')
        await message.answer_photo(photo=photo_path)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
