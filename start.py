import asyncio
from main import bot_main
from rss_pars import rss_main




async def main():
    # Запускаем обе задачи параллельно
    await asyncio.gather(
        bot_main(),
        rss_main(),
    )

if __name__ == "__main__":
    asyncio.run(main())