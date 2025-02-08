from aiogram import  Dispatcher, types
from aiogram.types import Message



async def send_photo(message: types.Message):
    with open('images/m5.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption='m5 f 90 competition')


def pic_handlers(dp: Dispatcher):
    dp.register_message_handler(send_photo, commands=['pic'])