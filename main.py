from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove
import config

bot = Bot(config.TOKEN) # создание экземлпяра класса Bot
dp = Dispatcher(bot) # создание диспетчера

kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="/help")]
    ],
    resize_keyboard=True
)

async def on_startup(*args, **kwargs):
    print("DEBUGGED SUCCESSFULLY")

# команда /start
@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    await message.delete()
    await bot.send_sticker(chat_id=message.from_user.id,
                     sticker=config.START_STICKER_ID)
    await bot.send_message(chat_id=message.from_user.id,
                           text=config.START_COMMAND_TEXT,
                           parse_mode="HTML",
                           reply_markup=kb)

# комманда /help
@dp.message_handler(commands=['help'])
async def help_command(message : types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.from_user.id,
                           text=config.HELP_COMMAND_TEXT)

# обработчик сообщений
@dp.message_handler()
async def on_message(message : types.Message):
    if message.from_user.type == "private":
        await bot.send_message(chat_id=message.from_user.id,
                               text="Запись рассматривается, ждите")
        await bot.send_message(chat_id=config.ARCHITECTOR) # отправить запись автору канала

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)