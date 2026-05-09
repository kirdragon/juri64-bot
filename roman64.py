import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot=Bot(token="8786369717:AAFDpPlwh8VCqzKnS2gzmJeaIwzuVeWQnCA")
print ("zov")
dp=Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")
async def main():
    dp.message.register(cmd_test2, Command("test2"))
    await dp.start_polling(bot)
@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Обычный Юрий")
@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это "особенный" юрий')
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🏀")
if __name__== "__main__":
    asyncio.run(main()) 
