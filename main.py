import asyncio
import logging
from db.main_db import create_tables
from aiogram import executor
from bot_config import bot, dp, types
from handler import (
    start,
    other_message,
    complaint_dialog,
    store_fsm,
    my_info,
    random,
    send_products,
    Set_commands,
    pic
)



# async def on_startup(_):
#     database.create_tables()
#     await Set_commands.set_commands(bot)
#     for admin in ADMINS:
#         await bot.send_message(chat_id=admin, text='Бот включен!')
#
#
# async def on_shutdown(_):
#     for admin in ADMINS:
#         await bot.send_message(chat_id=admin, text='Бот выключен!')

async def main():

    start.register_handlers(dp)
    Set_commands.register_handlers(dp)
    send_products.register_handlers(dp)
    pic.register_handlers(dp)
    my_info.register_handlers(dp)
    random.register_handlers(dp)
    complaint_dialog.register_review_handlers(dp)
    store_fsm.register_store_handlers(dp)
    other_message.register_handlers(dp)


if __name__ == '__main__':
    asyncio.run(main())

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True,
#                            on_startup=on_startup,
#                            on_shutdown=on_shutdown)
