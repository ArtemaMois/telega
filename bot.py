from aiogram.utils import executor
from dataBot import dispatcher

from handlers import admin, user

admin.register_handlers_admin(dispatcher)
user.register_handlers_user(dispatcher)


executor.start_polling(dispatcher, skip_updates=True)