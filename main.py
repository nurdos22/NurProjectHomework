import asyncio
from bot_config import bot, dp, types, database
from handler import start, pic, other_message, my_info, random, complaint_dialog, Set_commands

async def echo_handler(message: types.message):
    text = message.text
    await message.answer(text)

async def main():
    start.register_handlers(dp)
    Set_commands.register_handlers(dp)
    pic.register_handlers(dp)
    my_info.register_handlers(dp)
    random.register_handlers(dp)
    complaint_dialog.register_review_handlers(dp)





    other_message.register_handlers(dp)
    database.create_tables()
    await Set_commands.set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())