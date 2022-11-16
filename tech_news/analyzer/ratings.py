from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    sorted_news = sorted(news, key=lambda i: i['comments_count'], reverse=True)
    top_news = []
    for notice in sorted_news[:5]:
        top_news.append((notice['title'], notice['url']))
    return top_news


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = {}
    for new in news:
        name = new['category']
        categories[name] = categories.get(name, 0) + 1
    list_categories = [(v, k) for k, v in categories.items()]
    # ordena por quantidades em ordem decrescente e na sequencia por
    # ordem alfabetica de categoria, a seguir cria lista apenas com nomes
    top_5_tuples = sorted(list_categories, key=lambda x: (-x[0], x[1]))
    top_5 = [x[1] for x in top_5_tuples]
    return top_5[:5]
