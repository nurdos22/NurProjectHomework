from aiogram import  Dispatcher
from aiogram.types import Message




async def send_photo(message: Message):
    with open('../images/m5.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption='m5 F 90 competition')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_photo, commands=['pic'])