from aiogram import Dispatcher, Bot
from database import *
from translatepy import Translator
from g4f.client import Client
from newspaper import Article
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
import google.generativeai as genai
genai.configure(api_key="AIzaSyBv6OBRJr8Dm4PPqNokc0GAeiVjiBjOrlk")

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

translator = Translator()
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
    
    user_list = await get_users_by_categories(category=category)
    s = news_processing(news_text)
    for user in user_list:
        try:
            await bot.send_message(user, s,parse_mode='Markdown')
            print('normvse')
        except Exception as e:
            print('НОВОСТЬ НЕ ОТПРАВИЛАСЬ ИЗ-ЗА:', e)

# def translate_to_russian(text):
#     # try:
#     #     result = translator.translate(text, "Russian")
#     #     return result.result
#     # except Exception as e:
#     #     print(f"Ошибка перевода: {e}")
#     #     return "Ошибка перевода"
#     client = Client()
#     response = client.chat.completions.create(
#         model='gpt-4',
#         messages=[{"role": "user", "content": f"{text}. Переведи этот текст на русский язык. В твоем ответе должен содержаться только переведенный текст и ничего больше"}],
#         no_sandbox=True
#     )
#     return response.choices[0].message.content
async def translate_to_russian(text: str, target_language: str = "Russian") -> str:
    prompt = f"Translate the following text into {target_language}: {text}. Your answer should only contain the translated text"
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content(prompt)
    return response.text.strip()

def summarize(link):
        article = Article(link)
        article.download()  # Загружаем страницу
        article.parse()     # Анализируем содержимое

   
        prompt = f"Create a concise summary of the following text and translate it into Russian. Your response should only include the translated summary: {str(article.text)}. Your answer should only contain the translated text"
        model = genai.GenerativeModel("gemini-1.5-flash")
    
        response = model.generate_content(prompt)
        return response.text.strip()
