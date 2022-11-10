from tech_news.database import (
    search_news,
)


# Requisito 6
def search_by_title(title):
    # search = '/.*' + title + '.*/i'
    query = {"title": {"$regex": title, "$options": 'i'}}
    news = search_news(query)
    news_by_title = []
    for notice in news:
        news_by_title.append((notice['title'], notice['url']))
# retornar uma lista de tuplas com as notícias encontradas
#     [
#   ("Título1_aqui", "url1_aqui"),
#   ("Título2_aqui", "url2_aqui"),
#     ]
    return news_by_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
