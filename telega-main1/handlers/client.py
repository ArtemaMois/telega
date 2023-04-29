from aiogram import types, Dispatcher
from create_bot import dp, bot 
import connect_db
from keyboards import client_kb, admin_kb

User_name = ['i_temchik', 'Nikitabll', 'kaliuzhny']

#@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    if message.from_user.username == User_name:
        await message.answer( 'Задание ', reply_markup=admin_kb.button_case_admin)
        await message.delete()
    else:
        await message.answer(f'{message.from_user.first_name}, что хотел?', reply_markup=client_kb.kb_client)


#@dp.message_handler(commands=['First_name'])
async def get_first_name(message: types.Message):
    await message.answer('@'+ f'{message.from_user.username}')

#@dp.message_handler(commands=['My_case'])
async def my_case_command(message : types.Message):
    await message.reply('Введите ваш User name')



#@dp.message_handler(commands=['All_case'])
async def command_all_case(message : types.Message):
    await message.answer(message.from_user.id, connect_db.sql_readall())


def register_hanlders_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(get_first_name, commands=['First_name'])
    dp.register_message_handler(my_case_command, commands=['My_case'])
    dp.register_message_handler(command_all_case, commands=['All_case'])
