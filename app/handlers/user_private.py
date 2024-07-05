from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.kbds import reply
from app.yoomoney.pay_yoomoney import create_payment_link

user_private_router = Router()



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
async def paypal(message:Message):
    amount = 2
    label = f"payment_{message.from_user.id}"
    description = "Оплата 2 рублей"
    
    payment_link = create_payment_link(amount, label, description)
    if payment_link:
        await message.answer(f"Для оплаты 2 рублей перейдите по ссылке: {payment_link}")
    else:
        await message.answer("Ошибка при создании ссылки на оплату. Попробуйте позже.")

@user_private_router.message(F.text == "image")
async def image(message:Message):
    await message.answer_photo(photo="", caption="ваще фото")


@user_private_router.message(F.text == "Exel A2")
async def exel(message:Message):
    await message.answer('')

  






