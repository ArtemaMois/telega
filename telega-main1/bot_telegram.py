from aiogram.utils import executor
from create_bot import dp



async def on_startup(_):
    print('Бот сейчас онлайн')


from handlers import admin
from handlers import client
from handlers import other


admin.register_handlers_admin(dp)
client.register_hanlders_client(dp)
other.register_hanlders_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)