import feedparser
import asyncio
from datetime import datetime, timedelta
from func import *

# RSS URL для The New York Times
max_length = 10

# Список обработанных ссылок
ny_tec = []
eco_f = []
eco_bu = []
wp_bu =[]

async def Wash():
    RSS_URL = "https://www.economist.com/business/rss.xml"
    feed = feedparser.parse(RSS_URL)
    entry  = feed.entries[0]
    
            
    title = translate_to_russian(entry.title)
    description = translate_to_russian(entry.description)
    res = f"""
❗️{title}❗️

{description}

[ССЫЛКА]({entry.link})

Категория: Экономика

@goyskiyclub || @goynewsbot
"""
    if entry.title not in eco_bu:
        if len(eco_bu) >= max_length:
                eco_bu.pop(0)
        eco_bu.append(entry.title)
        await send_news_with_category(res, "economics")
            
        
async def rss_main():
    while True:
        await Wash()
        await asyncio.sleep(60)

asyncio.run(rss_main())
