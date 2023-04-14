from aiogram import types, Dispatcher
from create_bot import dp
import json, string


# @dp.message_handler()
async def echo_send(message:types.Message):
    if message.text == 'Привет':


        await message.answer('И тебе привет!')

def register_hanlders_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)