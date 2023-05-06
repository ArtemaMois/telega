from aiogram import types
from aiogram.dispatcher import Dispatcher 
from db import editDB

async def getID(message):
    data = message.split()
    if (len(data) > 1):
        return data[1]
    return 0

async def formatData(text):
    result = ''
    for element in text:
        for data in element:
            result += str(data) + '\n'
        result += '----------' + '\n'
    return result

async def getdata(message: types.Message):
    if (await getID(message.text) != 0):
        id = await getID(message.text)
        result = await formatData(editDB.getData(id))
        if (result == ''): await message.reply(f'Кейса с id = {id} в таблице не существует')
        else: await message.reply(result)
        return
    result = await formatData(editDB.getData())
    if (result == ''): await message.reply('Таблица пуста')
    else: await message.reply(result)

async def help(message: types.Message):
    await message.answer(text='Команды:\n /help - вывод доступных команд \n ' +
                   '/print @упоминание - вывод кейсов \n\n'
                    'АДМИН : \n\n' +
                    '/add \n @упоминание \n кейс \n Добавление кейса участнику \n' +
                    '/delete #id - удаление кейса или всей таблицы')
async def start(message: types.Message):
    await message.answer('Начинаем работу \n /help - список команд')

def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(getdata, commands=['print'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(start, commands=['start'])