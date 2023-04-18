from aiogram import types, Dispatcher
from create_bot import bot
from client_kb import kb_client
import client_kb
from connect_db import output
import psycopg2
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class Out(StatesGroup):
    user_name = State()


async def commands_help(message: types.Message):
    await message.reply(client_kb.HELP, reply_markup=kb_client)

#@dp.message_handler(commands=['start'])
async def commands_start(message : types.Message, state: FSMContext):
    await state.set_state(Out.user_name)
    await message.reply("Введите фамилию")

async def load_user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = message.text
    answer = output(data['user_name'])
    await state.finish()
    await message.answer(answer)


#@dp.message_handler(commands=['My_case'])
async def my_case_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Никита, здесь задания из бд, индивидуальные')



#@dp.message_handler(commands=['All_case'])
async def command_all_case(message : types.Message):
    await bot.send_message(message.from_user.id,'Никита, здаесь все задания, либо бд с заданиями')



def register_handlders_client(dp : Dispatcher):
    dp.register_message_handler(commands_help, commands=['help'])
    dp.register_message_handler(commands_start, commands=['start', 'help'], state=None)
    dp.register_message_handler(load_user_name, state=Out.user_name)
    dp.register_message_handler(my_case_command, commands=['My_case'])
    dp.register_message_handler(command_all_case, commands=['All_case'])
