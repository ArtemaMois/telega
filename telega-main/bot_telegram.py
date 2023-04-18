from aiogram import executor

from create_bot import dp
async def on_startup(_):
    print('Бот сейчас онлайн')

from heandlers import admin
from heandlers import client
from heandlers import other


admin.register_handlers_admin(dp)
client.register_handlders_client(dp)
other.register_handlders_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)