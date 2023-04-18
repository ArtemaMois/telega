from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/Заменить')
k1 = KeyboardButton('/Загрузить')
k2 = KeyboardButton('/Строка')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1,b2, k1, k2)

HELP = '''Привет, бот автоматизирует работу с кейсами(заданиями) для определённой группы лиц \n
команда /start - выводит информацию по фамилии человека\n
/Загрузить - создаёт нового пользователя\n
/Заменить - меняет кейс пользователя\n
/help - вызывает это ;)\n
Приятного пользования! <3
'''

