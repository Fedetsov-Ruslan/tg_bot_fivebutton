import os
from aiogram import Router, F
from aiogram.types import Message, InputFile, FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.kbds import reply
from app.sheet import sheet
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
    # создание ссылки к оплате
    quickpay = Quickpay(receiver='{YOOMONEY_ID}',
        quickpay_form='shop',
        targets='mav_test',
        paymentType='SB',
        sum=2.00,
        label='123')
    await message.answer(f"Ссылка на оплату: {quickpay.redirected_url}")
 

@user_private_router.message(F.text == "image")
async def image(message:Message):
    photo_path = "static/first_fon.jpg"  # загружаем картинку из static
    photo = FSInputFile(photo_path) 
    await message.answer_photo(photo, caption="This is Rik and Morty")


@user_private_router.message(F.text == "Exel A2")
async def exel(message:Message):
    data = sheet.get_sheet_data(range_name='Лист1!A2')
    await message.answer(f'Данные ячейки: {data}')


@user_private_router.message(F.text)
async def chec_date_complite(message:Message):
    all_date = message.text
    try:
        # валиадация даты. Сначала разбиваем на число, месяц год, затем проверям на правильность ввода данных
        date = all_date.split(".")
        if len(date) == 3:
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
            if month < 1 or month > 12:
                raise ValueError
            if day < 1 or day > 31:
                raise ValueError
            if month in (4, 6, 9, 11) and day == 31:
                raise ValueError
            if month == 2:
                if day > 29 or (day == 29 and not (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
                    raise ValueError
            values = [[all_date]]  # Оборачиваем в список, так как append ожидает список списков
            result = sheet.append_sheet_data(values, range_name="Лист1!B:B")
            await message.answer('Дата верна')
        else:
            await message.answer("Неверная дата")
            
            
    except:
        await message.answer("Неверная дата")

    

  






