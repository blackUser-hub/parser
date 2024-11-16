from aiogram import Bot, Dispatcher
from telethon import TelegramClient, events
from aiogram.methods import send_message
from func import *
import asyncio
import config 


def telegram_parser(send_message_func=None, loop=None):
    # Параметры из my.telegram.org
    api_id = config.api_id
    api_hash = config.api_hash

    # Список каналов для отслеживания
    channels = [
        'https://t.me/rian_ru',
        'https://t.me/TheEconomisto',
        'https://t.me/goyskiyclub'
    ]

    # Сессия клиента telethon
    session = 'gazp'
    client = TelegramClient(session, api_id, api_hash, loop=loop)

    @client.on(events.NewMessage(chats=channels))  # Подписка на события новых сообщений из списка каналов
    async def handler(event):
        # Отправка постов из отслеживаемых каналов
        if send_message_func is None:
            await send_news_without_category(event.raw_text)
        else:
            # Здесь можно указать канал, в который будут пересылаться сообщения (например, @prime1)
            # await send_message_func(f'@prime1\n{event.raw_text}')
            pass

    return client

async def tg_start():
    client = telegram_parser()
    await client.start()  # Используем await для асинхронного вызова start
    await client.run_until_disconnected()  # Используем await для асинхронного вызова run_until_disconnected



asyncio.run(tg_start())