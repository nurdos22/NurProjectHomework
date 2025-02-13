from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot_config import database

class Complaint(StatesGroup):
    name = State()
    instagram = State()
    rate = State()
    comments = State()

async def start_dialog_callback(callback: CallbackQuery):

    await callback.message.answer("Как вас зовут?")
    await Complaint.name.set()


async def stop_dialog(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за потраченное время")


async def start_dialog_command(message: Message):
    await message.answer("Как вас зовут?")
    await Complaint.name.set()


async def process_insta(message: Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["name"] = message.text
        await Complaint.instagram.set()
        await message.answer("Ваш логин в инсте?")
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}. Пожалуйста, повторите попытку")

async def process_rate(message: Message, state: FSMContext):
    if not message.text.isdigit() or not (1 <= int(message.text) <= 5):
        await message.answer("Пожалуйста, введите число от 1 до 5.")
        return
    async with state.proxy() as data:
        data["instagram"] = message.text
    await Complaint.rate.set()
    await message.answer("Поставьте нам оценку от 1 до 5")


async def process_text(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["rate"] = message.text
    await Complaint.comments.set()
    await message.answer("Дополнительные комментарии/жалобы?")


async def process_thanks(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["comments"] = message.text
    data = await state.get_data()


    database.add_complaint(data)
    await message.answer("Спасибо за отзыв!")
    await state.finish()
def register_review_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog_callback, lambda c: c.data == "review")
    dp.register_message_handler(
        stop_dialog, Text(equals=("стоп", "stop"), ignore_case=True), state="*"
    )
    dp.register_message_handler(start_dialog_command, commands=['review'])
    dp.register_message_handler(process_insta, state=Complaint.name)
    dp.register_message_handler(process_rate, state=Complaint.instagram)
    dp.register_message_handler(process_text, state=Complaint.rate)
    dp.register_message_handler(process_thanks, state=Complaint.comments)
