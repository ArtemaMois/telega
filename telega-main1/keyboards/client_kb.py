from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/My_case')
b2 = KeyboardButton('/All_case')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2) 
