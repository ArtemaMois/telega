from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



button_load = KeyboardButton('/Add')
button_delete = KeyboardButton('/Delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)

button_case_admin.row(button_load, button_delete)
