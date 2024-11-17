import feedparser
import asyncio
from datetime import datetime, timedelta
from func import *

# RSS URL для The New York Times
max_length = 100

# Список обработанных ссылок
ny_buis = []
eco_f = []
eco_bu = []
wp_bu =[]

# не работает он че то
# async def Wash_bu():
#     print('Wash_bu')
#     RSS_URL = "https://feeds.washingtonpost.com/rss/business"
#     feed = feedparser.parse(RSS_URL)
#     for entry in feed.entries:
            
#         title = translate_to_russian(entry.title)
#         description = translate_to_russian(entry.description)
#         res = f"""
# ❗️{title}❗️

# {description}

# [ССЫЛКА]({entry.link})

# Категория: Экономика

# @goyskiyclub || @goynewsbot
# """
#         if entry.title not in wp_bu:
#             if len(wp_bu) >= max_length:
#                 wp_bu.pop(0)
#             wp_bu.append(entry.title)
#             await send_news_with_category(res, "economics")
            

async def Eco_buissnes():
    print('Eco_buissnes')
    RSS_URL = "https://www.economist.com/business/rss.xml"
    feed = feedparser.parse(RSS_URL)
    entry = feed.entries[0]
            
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
            
        

async def Eco_finance():
    print('Eco_finance')
    RSS_URL = "https://www.economist.com/finance-and-economics/rss.xml"
    feed = feedparser.parse(RSS_URL)
    entry = feed.entries[0]
            
    title = translate_to_russian(entry.title)
    description = translate_to_russian(entry.description)
    res = f"""
❗️{title}❗️

{description}

[ССЫЛКА]({entry.link})

Категория: Экономика

@goyskiyclub || @goynewsbot
"""
    if entry.title not in eco_f:
        if len(eco_f) >= max_length:
            eco_f.pop(0)
        eco_f.append(entry.title)
        await send_news_with_category(res, "economics")

async def NYT_tech():
    print('NYT_tech')
    RSS_URL = "https://nypost.com/business/feed/"
    feed = feedparser.parse(RSS_URL)
    print(feed)
    entry = feed.entries[0]
            
    title = translate_to_russian(entry.title)
    description = translate_to_russian(entry.description)
    res = f"""
❗️{title}❗️

{description}

[ССЫЛКА]({entry.link})

Категория : Экономика

@goyskiyclub || @goynewsbot
"""
    if entry.title not in ny_buis:
        if len(ny_buis) >= max_length:
            ny_buis.pop(0)
        ny_buis.append(entry.title)
        await send_news_with_category(res, "economics")




            
        
async def rss_main():
    while True:
        print('парсер запустился хз')
        await NYT_tech()
        await Eco_finance()
        await Eco_buissnes()
        await asyncio.sleep(60)