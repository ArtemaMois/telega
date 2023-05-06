from aiogram import types
from aiogram.dispatcher import Dispatcher 
from db import editDB

async def getUser(message):
    data = message.split('\n')
    return {
        'user': data[1].replace(' ', ''),
        'case': data[2] 
    }

async def getID(message):
    data = message.split()
    if (len(data) > 1):
        return int(data[1])
    return 0

async def setCase(message: types.Message):
    if (message.from_user.id == 1848416424):
        caseData = await getUser(message.text)
        result = editDB.setData(caseData['user'], caseData['case'])
        await message.reply(result)

async def deleteCase(message: types.Message):
    if (message.from_user.id == 1848416424):
        if await getID(message.text) > 0:
            await message.reply(editDB.removeData(await getID(message.text)))
            return
        await message.reply(editDB.removeData())



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(setCase, commands=['add'])
    dp.register_message_handler(deleteCase, commands=['delete'])