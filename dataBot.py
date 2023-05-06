from aiogram import Bot
from aiogram.dispatcher import Dispatcher 

import os

Bot = Bot(token=os.getenv('token'))
dispatcher = Dispatcher(Bot)