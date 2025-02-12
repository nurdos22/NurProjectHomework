from distutils.dist import command_re

from aiogram import  Dispatcher
from bot_config import bot
from handler.complaint_dialog import register_review_handlers

from aiogram.types import (

    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,

)




async def start_handler(message: Message):
    user = message.from_user
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='📍 Наш адрес', url='https://maps.app.goo.gl/reTtd5yrCAeBBKpP9'),
            InlineKeyboardButton(text='🌐 Наш сайт', url='https://www.youtube.com/watch?v=YOJFt_gRsGQ&list=RDAn0eyZQNHrs&index=5&ab_channel=GlassCage'),
            InlineKeyboardButton(text='📸 Instagram ', url='https://www.instagram.com/'),
            InlineKeyboardButton(text='🍕 Меню ', callback_data="menu"),


        ],


        [
            InlineKeyboardButton(text='Оставить отзыв', callback_data="review"),
        ]
    ])

    await message.answer(f'Здравствуйте  {user.first_name}, добро пожаловать '
                         f'на наш ресторан "NUR" ',  reply_markup=kb)

menu_items = [
    {"name": "Пепперони", "price": "600 с", "photo": "https://example.com/pepperoni.jpg"},
    {"name": "Шаурма", "price": "210 с", "photo": "https://example.com/shawarma.jpg"},
    {"name": "Цезарь с курицей", "price": "500 с", "photo": "https://example.com/caesar.jpg"}
]

async def send_menu(callback_query: CallbackQuery):
    await callback_query.answer()
    menu_text = "🍽️ Наше меню:\n" + "\n".join(
        [f" {item['name']} - {item['price']}" for item in menu_items]
    )
    await bot.send_message(callback_query.from_user.id, menu_text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_callback_query_handler(send_menu, lambda c: c.data == "menu")
    register_review_handlers(dp)
