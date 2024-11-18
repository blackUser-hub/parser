import feedparser
import asyncio
from datetime import datetime, timedelta
from func import *
from newspaper import Article
from asyncio import WindowsSelectorEventLoopPolicy
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
import feedparser
import asyncio
from func import send_news_with_category
from asyncio import WindowsSelectorEventLoopPolicy
from newspaper import Article

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# RSS URL для The New York Times
max_length = 100

# Список обработанных ссылок
nyt_buis = []
eco_f = []
eco_bu = []
wp_bu = []
nyt_t = []
nyp_t = []
nyp_p = []
nyp_m = []
eco_t = []

async def fetch_rss(url, retries=3):
    for _ in range(retries):
        try:
            return feedparser.parse(url)
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
            await asyncio.sleep(5)
    return None

async def Eco_buissnes():
    print('Eco_buissnes')
    RSS_URL = "https://www.economist.com/business/rss.xml"
    feed = await fetch_rss(RSS_URL)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
    
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
    feed = await fetch_rss(RSS_URL)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
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

async def NYT_bus():
    print('NYT_bus')
    RSS_URL = "https://nypost.com/business/feed/"
    feed = await fetch_rss(RSS_URL)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
        summary = summarize(entry.link)
        res = f"""
❗️{title}❗️

{description}

{summary}

[ССЫЛКА]({entry.link})

Категория : Экономика
@goyskiyclub || @goynewsbot
"""
        if entry.title not in nyt_buis:
            if len(nyt_buis) >= max_length:
                nyt_buis.pop(0)
            nyt_buis.append(entry.title)
            await send_news_with_category(res, "economics")

async def NYT_tech():
    print('NYT_tech')
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'
    feed = await fetch_rss(url)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
        summary = summarize(entry.link)
        res = f"""
❗️{title}❗️

{description}

{summary}

[ССЫЛКА]({entry.link})

Категория : Технологии
@goyskiyclub || @goynewsbot
"""
        if entry.title not in nyt_t:
            if len(nyt_t) >= max_length:
                nyt_t.pop(0)
            nyt_t.append(entry.title)
            await send_news_with_category(res, "digital")

async def NYP_tech():
    print('NYP_tech')
    url = 'https://nypost.com/tech/feed/'
    feed = await fetch_rss(url)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
        summary = summarize(entry.link)
        res = f"""
❗️{title}❗️

{description}

{summary}

[ССЫЛКА]({entry.link})

Категория : Технологии
@goyskiyclub || @goynewsbot
"""
        if entry.title not in nyp_t:
            if len(nyp_t) >= max_length:
                nyp_t.pop(0)
            nyp_t.append(entry.title)
            await send_news_with_category(res, "digital")

async def NYP_politcs():
    print('NYP_politcs')
    url = 'https://nypost.com/politics/feed/'
    feed = await fetch_rss(url)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
        summary = summarize(entry.link)
        res = f"""
❗️{title}❗️

{description}

{summary}

[ССЫЛКА]({entry.link})

Категория : Технологии
@goyskiyclub || @goynewsbot
"""
        if entry.title not in nyp_p:
            if len(nyp_p) >= max_length:
                nyp_p.pop(0)
            nyp_p.append(entry.title)
            await send_news_with_category(res, "politics")

async def NYP_media():
    print('NYP_media')
    url = 'https://nypost.com/media/feed/'
    feed = await fetch_rss(url)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
        summary = summarize(entry.link)
        res = f"""
❗️{title}❗️

{description}

{summary}

[ССЫЛКА]({entry.link})

Категория : Технологии
@goyskiyclub || @goynewsbot
"""
        if entry.title not in nyp_m:
            if len(nyp_m) >= max_length:
                nyp_m.pop(0)
            nyp_m.append(entry.title)
            await send_news_with_category(res, "politics")

async def Eco_tech():
    print('Eco_tech')
    RSS_URL = "https://www.economist.com/business/rss.xml"
    feed = await fetch_rss(RSS_URL)
    if feed:
        entry = feed.entries[0]
                
        title = await translate_to_russian(entry.title)
        description = await translate_to_russian(entry.description)
    
        res = f"""
❗️{title}❗️

{description}

[ССЫЛКА]({entry.link})

Категория: Технологии

@goyskiyclub || @goynewsbot
"""
        if entry.title not in eco_t:
            if len(eco_t) >= max_length:
                eco_t.pop(0)
            eco_t.append(entry.title)
            await send_news_with_category(res, "digital")

async def rss_main():
    while True:
        print('Парсер запустился...')
        await asyncio.gather(
            NYT_bus(),
            Eco_finance(),
            Eco_buissnes(),
            asyncio.sleep(90),
            NYT_tech(),
            NYP_media(),
            NYP_politcs(),
            asyncio.sleep(90),
            Eco_tech(),
        )
        await asyncio.sleep(90)
