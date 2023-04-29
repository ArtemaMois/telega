from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
import connect_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID = []
User_name = ['i_temchik', 'Nikitabll', 'kaliuzhny']

class FSMAdmin(StatesGroup):
    name = State()
    description = State()
    usname = State()
    body_message = []

@dp.message_handler(commands=['moderator'], is_chat_admin = True)
async def make_changes_command(message : types.Message):
    global ID 
    ID.append(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Чего надо???', reply_markup=admin_kb.button_case_admin)

#__________________________________________________---------------------------________________________________________________________________

@dp.message_handler(commands=['add'], state=FSMContext)
async def cm_start(message : types.Message, state = FSMAdmin):
    if message.from_user.username in User_name :
        body_message = (message.text).split("\n")
        str_body_message = " ".join(body_message[2:])
        await message.answer(f'Получатель:{body_message[1]}\n Задание кейса: {str_body_message}')
    
    await connect_db.database()
    await state.finish()



#@dp.message_handler(state="*", commands=['отмена'])
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.reply('ОК')

  

#@dp.message_handler(commands=['Delete'])
async def delete_item(message: types.Message):
    if message.from_user.username in User_name:
        read = connect_db.sql_readall()
        for ret in read:
            await bot.send_message(message.from_user.id,f'ТЕМА:   {ret[0]}\nОписание: \n{ret[1]}\nUsername получателя: {ret[2]}')
            await bot.send_message(message.from_user.id, text='^-^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[0]}', callback_data=f'del {ret[0]}')))


def register_handlers_admin(dp : Dispatcher):

    dp.register_message_handler(cm_start, commands = ['Add'], state=FSMAdmin)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case = True), state="*")
    # dp.register_message_handler(load_name, content_types=['name'], state=FSMAdmin.name)
    # dp.register_message_handler(load_description, state=FSMAdmin.description)
    # dp.register_message_handler(load_description, state=FSMAdmin.usname)
    dp.register_message_handler(delete_item, commands=['Delete'])
    
