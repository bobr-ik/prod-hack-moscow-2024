from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters.callback_data import CallbackData

start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text='Новый счёт', callback_data='new'), InlineKeyboardButton(text='Новая группа', callback_data='new_group')],
        [InlineKeyboardButton(text='Мои финансы', web_app=WebAppInfo(url='https://158.160.85.97/'))]
        
    ], resize_keyboard=True
)
