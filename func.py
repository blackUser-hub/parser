from aiogram import Dispatcher, Bot
from database import get_all_user_ids

API_TOKEN = "8054346845:AAHNITZO28TM-RGTnDoWrCXHuc6VY-Ir8jU"  # Замените на токен вашего бота

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()



async def send_news_to_user(text:str):
    user_list = get_all_user_ids()
    for user in user_list:
        try: 
            await bot.send_message(user,)