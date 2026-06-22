import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler

bot = Bot(token="8806058737:AAHEXyrvvCOxeqnFl28WDnwDSugnKOmmg6s")
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# Post yuborish funksiyasi
async def send_post(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

@dp.message(Command("reja"))
async def schedule_command(message: types.Message):
    # Foydalanuvchi: "/reja 10 Hi" deb yozsa, 10 soniyadan keyin Hi yuboradi
    args = message.text.split()
    seconds = int(args[1])
    text = " ".join(args[2:])
    
    scheduler.add_job(send_post, 'date', run_date=asyncio.get_event_loop().time() + seconds, args=[message.chat.id, text])
    await message.answer(f"Post {seconds} soniyadan keyin yuboriladi.")

async def main():
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())