from aiogram import types, Dispatcher
from create_bot import dp, bot  
from keyboards import kb_client

import os, json, string


@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,'Твое задание', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС,напиши ему https://t.me/Func_Admin_bot')

@dp.message_handler(commands=['My_case'])
async def my_case_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Никита, здесь задания из бд, индивидуальные')


@dp.message_handler(commands=['All_case'])
async def command_all_case(message : types.Message):
    await bot.send_message(message.from_user.id,'Никита, здаесь все задания, либо бд с заданиями')



def register_hanlders_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(my_case_command, commands=['My_case'])
    dp.register_message_handler(command_all_case, commands=['All_case'])
