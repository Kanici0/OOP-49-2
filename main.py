from aiogram import executor
import logging
from config import bot, Admins, dp
from handlers import commands,quizi,echo,__init__
async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бок включен!')


commands.register_commands(dp)
quizi.register_handlers(dp)

echo.register_handlers(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)