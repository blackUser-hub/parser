import asyncio
from threading import Thread
from main import bot_main
from rss_pars import rss_main
from asyncio import WindowsSelectorEventLoopPolicy

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# Запуск бота в отдельном потоке
def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot_main())

# Запуск парсера в отдельном потоке
def start_rss_parser():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(rss_main())

if __name__ == "__main__":
    # Создаем потоки для каждой задачи
    bot_thread = Thread(target=start_bot)
    rss_thread = Thread(target=start_rss_parser)

    # Запускаем потоки
    bot_thread.start()
    rss_thread.start()

    # Дожидаемся завершения потоков
    bot_thread.join()
    rss_thread.join()
