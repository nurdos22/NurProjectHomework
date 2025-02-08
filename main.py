import asyncio
from bot_config import dp, types
from handler import start, pic, my_info, random

async def echo_handler(message: types.message):
    text = message.text
    await message.answer(text)

async def main():
    start.register_handlers(dp)
    pic.register_handlers(dp)
    my_info.register_handlers(dp)
    random.register_handlers(dp)

    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())