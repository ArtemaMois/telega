from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token='5991815765:AAF3qmOBi0HJW5XNx-xaqaOpICtloCnXepI')
dp=Dispatcher(bot, storage=storage)