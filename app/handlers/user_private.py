import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.kbds import reply
from yoomoney import Quickpay
from dotenv import load_dotenv
user_private_router = Router()


load_dotenv()
YOOMONEY_TOKEN = os.getenv("YOOMONEY_TOKEN")
YOOMONEY_RECEIVER = os.getenv("YOOMONEY_ID")


@user_private_router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, I'm AI bot", 
                         reply_markup=reply.start_kb.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Введите дату или выберете один из пунктов",
    ))

@user_private_router.message(F.text == "Ленина 1")
async def point_map(message:Message):
    await message.answer('вот ваша адресс: https://yandex.by/maps/157/minsk/house/Zk4YcwJnSU0PQFtpfXVxc3lkZA==/?indoorLevel=1&ll=27.557088%2C53.902570&z=16.81')

@user_private_router.message(F.text == "yoomoney")
async def pay(message:Message):
    quickpay = Quickpay(receiver='{YOOMONEY_ID}',
        quickpay_form='shop',
        targets='mav_test',
        paymentType='SB',
        sum=2.00,
        label='123')
    await message.answer(f"{quickpay.redirected_url}")
 

@user_private_router.message(F.text == "image")
async def image(message:Message):
    await message.answer_photo(photo="", caption="ваще фото")


@user_private_router.message(F.text == "Exel A2")
async def exel(message:Message):
    await message.answer('')

  






