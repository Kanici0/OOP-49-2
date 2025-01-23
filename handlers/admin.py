from aiogram import Dispatcher
from db.products import send_products, send_first_product, next_product

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(send_products, commands=['send_products'])
    dp.register_message_handler(send_first_product, commands=['send_first_product'])
    dp.register_callback_query_handler(next_product, lambda c: c.data.startswith('next_product'))
