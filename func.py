from aiogram import Dispatcher, Bot
from database import *
from translatepy import Translator

API_TOKEN = "8054346845:AAHNITZO28TM-RGTnDoWrCXHuc6VY-Ir8jU"  # Замените на токен вашего бота
translator = Translator()
# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def news_processing(s: str) -> str:
    return s

async def send_news_without_category(news_text:str):

    user_list = get_all_user_ids()
    for user in user_list:
        try: 
            await bot.send_message(user, news_text)
            print('normvso')
        except Exception as e:
            print('НОВОСТЬ НЕ ОТПРАВИЛАСЬ ИЗ-ЗА:', e)



async def send_news_with_category(news_text:str, category:str):
    
    user_list = get_users_by_categories(category=category)
    s = news_processing(news_text)
    for user in user_list:
        try:
            await bot.send_message(user, s,parse_mode='Markdown')
            print('normvse')
        except Exception as e:
            print('НОВОСТЬ НЕ ОТПРАВИЛАСЬ ИЗ-ЗА:', e)

def translate_to_russian(text):
    try:
        result = translator.translate(text, "Russian")
        return result.result
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return "Ошибка перевода"

