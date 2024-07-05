from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text="Ленина 1"),
    KeyboardButton(text="yoomoney"),
    KeyboardButton(text="image"),
    KeyboardButton(text="Exel A2"),
)
start_kb.adjust(2,2)