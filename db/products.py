import aiosqlite
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import Bot, Dispatcher

# Создание клавиатуры с кнопкой "далее"
def get_next_button(offset):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Далее", callback_data=f"next_product_{offset + 1}"))
    return keyboard

async def send_products(dp: Dispatcher, bot: Bot, admin: int):
    async with aiosqlite.connect('db/store.sqlite3') as db:
        async with db.execute("""
            SELECT s.*, sd.*, c.*
            FROM store s
            INNER JOIN store_detail sd ON s.product_id = sd.product_id
            INNER JOIN collections c ON s.product_id = c.productid
        """) as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                await bot.send_message(chat_id=admin, text=f"Product: {row['name_product']}, Size: {row['size']}, Price: {row['price']}, Category: {row['category']}, Collection: {row['collection']}")

async def send_first_product(dp: Dispatcher, bot: Bot, admin: int):
    async with aiosqlite.connect('db/store.sqlite3') as db:
        async with db.execute("""
            SELECT s.*, sd.*, c.*
            FROM store s
            INNER JOIN store_detail sd ON s.product_id = sd.product_id
            INNER JOIN collections c ON s.product_id = c.productid
            LIMIT 1 OFFSET 0
        """) as cursor:
            row = await cursor.fetchone()
            if row:
                await bot.send_message(chat_id=admin, text=f"Product: {row['name_product']}, Size: {row['size']}, Price: {row['price']}, Category: {row['category']}, Collection: {row['collection']}", reply_markup=get_next_button(0))

# Обработчик для кнопки "далее"
async def next_product(callback_query: CallbackQuery):
    message = callback_query.message
    offset = int(callback_query.data.split('_')[-1])
    async with aiosqlite.connect('db/store.sqlite3') as db:
        async with db.execute("""
            SELECT s.*, sd.*, c.*
            FROM store s
            INNER JOIN store_detail sd ON s.product_id = sd.product_id
            INNER JOIN collections c ON s.product_id = c.productid
            LIMIT 1 OFFSET ?
        """, (offset,)) as cursor:
            row = await cursor.fetchone()
            if row:
                await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f"Product: {row['name_product']}, Size: {row['size']}, Price: {row['price']}, Category: {row['category']}, Collection: {row['collection']}", reply_markup=get_next_button(offset))
            else:
                await bot.answer_callback_query(callback_query.id, text="No more products!")
