from imports import *
import config, keyboards

bot = Bot(config.TOKEN) # создание экземлпяра класса Bot
dp = Dispatcher(bot) # создание диспетчера

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
                           reply_markup=keyboards.kb)

# комманда /help
@dp.message_handler(commands=['help'])
async def help_command(message : types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.from_user.id,
                           text=config.HELP_COMMAND_TEXT)

# обработчик сообщений
@dp.message_handler()
async def on_message(message : types.Message):
    if message.chat.type == "private":
        await bot.send_message(chat_id=message.from_user.id,
                               text="Запись рассматривается, ждите")
        await bot.send_message(chat_id=config.ARCHITECTOR,
                               text=message.text,
                               reply_markup=keyboards.estimate_kb) # отправить запись автору канала

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("post"))
async def callback_processing(callback : types.CallbackQuery):
    if callback == "post_accepted":
        await bot.send_message(chat_id=callback.message.from_user.id,
                               text="Партия одобрять! Запись принята")
        await bot.send_message(chat_id=config.CHANNEL_ID,
                               text=callback.message.text)
    else:
        await bot.send_message(chat_id=callback.message.from_user.id,
                               text="Партия не одобрять! Запись отклонена")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)