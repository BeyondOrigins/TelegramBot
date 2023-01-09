from imports import *

kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="/help")]
    ],
    resize_keyboard=True
)

estimate_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Одобрить✅",
                             callback_data="post_accepted"),
            InlineKeyboardButton(text="Отколнить❌",
                                callback_data="post_rejected")
        ]
    ],
    
)