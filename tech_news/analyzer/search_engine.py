from datetime import date


from tech_news.database import (
    search_news,
)


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": 'i'}}
    news = search_news(query)
    news_by_title = []
    for notice in news:
        news_by_title.append((notice['title'], notice['url']))
    return news_by_title


# Requisito 7
def search_by_date(date_str):
    try:
        timestamp = date.fromisoformat(date_str).strftime('%d/%m/%Y')
        query = {"timestamp": timestamp}
        news = search_news(query)
        news_by_date = []
        for notice in news:
            news_by_date.append((notice['title'], notice['url']))
        return news_by_date
    except Exception:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
