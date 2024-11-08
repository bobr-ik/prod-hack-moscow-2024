from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text='Управление счетами', callback_data='new')]
    ], resize_keyboard=True
)