from aiogram import  Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


# @dp.message_handler(commands =['start'])
async def start_handler(message: types.Message):
    user = message.from_user
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Your website', url='https://www.pinterest.com/')
        ]
    ])
    await message.answer(f'hello {user.first_name}', reply_markup=kb)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
