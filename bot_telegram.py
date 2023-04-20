from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



async def on_startup(_):
    print('Бот сейчас онлайн')
    sqlite_db.sql_start()




# ---------------------------------------------Админские кнопки  --------------------------------------------------------



button_load = KeyboardButton('/Add')
button_delete = KeyboardButton('/Delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)

button_case_admin.row(button_load, button_delete)


# ---------------------------------------------Админская часть с кнопками -----------------------------------------------

User_name = 'i_temchik'

class FSMAdmin(StatesGroup):
    name = State()
    description = State()
    usname = State()
    body_message = []



@dp.message_handler(commands=['add'], state=FSMContext)
async def cm_start(message : types.Message, state = FSMAdmin):
    if message.from_user.username == User_name :
        body_message = (message.text).split("\n")
        str_body_message = " ".join(body_message[2:])
        await message.answer(f'Получатель:{body_message[1]}\n Задание кейса: {str_body_message}')
    
    await sqlite_db.sql_add_command()
    await state.finish()



@dp.message_handler(state="*", commands=['отмена'])
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.reply('ОК')



@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace("del ", ""))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)     

@dp.message_handler(commands=['Удалить'])
async def delete_item(message: types.Message):
    if message.from_user.username == User_name:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_message(message.from_user.id,f'ТЕМА:   {ret[0]}\nОписание: \n{ret[1]}\nUsername получателя: {ret[2]}')
            await bot.send_message(message.from_user.id, text='^-^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))


def register_handlers_admin(dp : Dispatcher):

    dp.register_message_handler(cm_start, commands = ['Add'], state=FSMAdmin)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    # dp.register_message_handler(load_name, content_types=['name'], state=FSMAdmin.name)
    # dp.register_message_handler(load_description, state=FSMAdmin.description)
    # dp.register_message_handler(load_description, state=FSMAdmin.usname)
    dp.register_message_handler(delete_item, commands=['Delete'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case = True), state="*")




# ----------------------------------------Клиентская часть с кнопками ----------------------------------------------------



b1 = KeyboardButton('/My_case')
b2 = KeyboardButton('/All_case')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2) 


# ---------------------------------------- Общие кнопки (для всех) ------------------------------------------------------

@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    if message.from_user.username == User_name:
        await message.answer( 'Задание ', reply_markup=admin_kb.button_case_admin)
        await message.delete()
    else:
        await message.answer(f'{message.from_user.first_name}, что хотел?', reply_markup=kb_client)



@dp.message_handler(commands=['First_name'])
async def get_first_name(message: types.Message):
    await message.answer(f'{message.from_user.username}')

@dp.message_handler(commands=['My_case'])
async def my_case_command(message : types.Message):
    await message.reply('Введите ваш User name')



@dp.message_handler(commands=['All_case'])
async def command_all_case(message : types.Message):
    await sqlite_db.sql_read(message)






def register_hanlders_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(my_case_command, commands=['My_case'])
    dp.register_message_handler(command_all_case, commands=['All_case'])


















executor.start_polling(dp, skip_updates=True, on_startup=on_startup)