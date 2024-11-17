from aiogram import Dispatcher, Bot
from database import *
from translatepy import Translator
from g4f.client import Client
from g4f.cookies import set_cookies

set_cookies(".bing.com", {
  "_U": "cookie value"
})

set_cookies(".google.com", {
  "__Secure-1PSID": "cookie value"
})


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
    # try:
    #     result = translator.translate(text, "Russian")
    #     return result.result
    # except Exception as e:
    #     print(f"Ошибка перевода: {e}")
    #     return "Ошибка перевода"
    client = Client()
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[{"role": "user", "content": f"{text}. Переведи этот текст на русский язык. В твоем ответе должен содержаться только переведенный текст и ничего больше"}],
        no_sandbox=True
    )
    return response.choices[0].message.content

print(translate_to_russian('Japanese autoparts company Takata files bankruptcy in light of ‘largest and most complex safety recall’ in US history'))
