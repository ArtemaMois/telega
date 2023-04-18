from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from connect_db import update_db, database, new_row
import psycopg2

class FSMAdmin(StatesGroup):
    user_name = State()
    name = State()
    description = State()
    status = State()
    update_name = State()
    update_keys = State()
    update_description = State()
    update_state = State()
    

#try:
#    connection = psycopg2.connect(dbname = "keys_bot", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
#    curr = connection.cursor()
#    print("Подключено к дб!")
#except:
#    print("error!")

#'INSERT INTO keyses(name_id) VALUES (%s)', (data["name"],)
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message, state: FSMContext):
    await state.set_state(FSMAdmin.user_name)
    await message.reply("Загрузи фамилию")


async def load_sername(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sername'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите название кейса")


#@dp.message_handler(content_types=['name'], state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        

       

    await FSMAdmin.next()
    await message.reply("Введи описание")

#@dp.message_handler(state=FSMAdmin.description)
async def load_description(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите статус кейса")

async def load_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['state'] = message.text
        new_row(user_id, data['sername'], data['name'], data['description'], data['state'])
    await state.finish()


async def update(message: types.Message, state: FSMContext):
    await state.set_state(FSMAdmin.update_name)
    await message.answer("Введите фамилию, данные которого хотите изменить")

async def update_name(message: types.Message, state: FSMContext):
    async with state.proxy() as updata:
        updata['update_name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите новое название кейса")

async def update_keys(message: types.Message, state: FSMContext):
    async with state.proxy() as updata:
        updata['update_keys'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите новое описание кейса")

async def update_description(message: types.Message, state: FSMContext):
    async with state.proxy() as updata:
        updata['update_description'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите новый статус кейса")

async def update_state(message: types.Message, state: FSMContext):
    async with state.proxy() as updata:
        updata['update_state'] = message.text
        update_db(updata['update_name'], updata['update_keys'], updata['update_description'], updata['update_state'])
    await state.finish()
    await message.reply("Успешно изменены данные!")


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands = ['Загрузить'], state=None)
    dp.register_message_handler(load_sername, state=FSMAdmin.user_name)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_state, state=FSMAdmin.status)
    dp.register_message_handler(update, commands = ['Заменить'], state=None)
    dp.register_message_handler(update_name, state=FSMAdmin.update_name)
    dp.register_message_handler(update_keys, state=FSMAdmin.update_keys)
    dp.register_message_handler(update_description, state=FSMAdmin.update_description)
    dp.register_message_handler(update_state, state=FSMAdmin.update_state)