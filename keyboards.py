from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Средняя Игра', callback_data='medium')],
        [InlineKeyboardButton(text='Большая Игра', callback_data='big')],
        [InlineKeyboardButton(text='Очень большая Игра', callback_data='mega')],
        [InlineKeyboardButton(text='Другие приложения', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', url="http://ya.ru")],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]
    ]
)