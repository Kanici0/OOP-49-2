
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons

class FSM_store(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()

# Начало диалога
async def start_fsm_store(message: types.Message):
    await FSM_store.name.set()
    await message.answer('Введите название товара:')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await FSM_store.next()
    sizes = ["XL", "3XL", "L", "M", "S"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*sizes)
    await message.answer('Выберите размер:', reply_markup=keyboard)

# Ловим размер и переходим к категории
async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_store.next()
    await message.answer('Введите категорию товара:', reply_markup=types.ReplyKeyboardRemove())

# Ловим категорию и переходим к стоимости
async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSM_store.next()
    await message.answer('Введите стоимость товара:')

# Ловим стоимость и переходим к фото
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSM_store.next()
    await message.answer('Отправьте фото товара:')

# Ловим фото и предлагаем подтвердить данные
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await FSM_store.next()
        await message.answer('Проверьте правильность данных:')
        await message.answer_photo(photo=data['photo'],
                                   caption=f'Название товара - {data["name"]}\n'
                                           f'Размер - {data["size"]}\n'
                                           f'Категория - {data["category"]}\n'
                                           f'Стоимость - {data["price"]}\n',
                                   reply_markup=buttons.submit)

# Подтверждение данных
async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            # Сохранение данных в базе данных или других действиях
            await message.answer('Товар добавлен в базу данных', reply_markup=buttons.remove_keyboard)
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()
    else:
        await message.answer('Выберите "да" или "нет"')

# Отмена действия
async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard)

# Регистрация обработчиков
def register_handlers_fsm_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_store, commands='store')
    dp.register_message_handler(load_name, state=FSM_store.name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_store.submit)
