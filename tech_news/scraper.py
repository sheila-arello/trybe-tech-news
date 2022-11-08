import requests
import time
from bs4 import BeautifulSoup
# from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {'user-agent': 'Fake user-agent'}
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    page = BeautifulSoup(html_content, "html.parser")
    lista = []
    data_links = page.find_all("article")
    for link in data_links:
        link.find("a").get("href")
        if link.find("a").get("href") is not None:
            lista.append(link.find("a").get("href"))
    lista = lista[1:]
    return lista


# Requisito 3
def scrape_next_page_link(html_content):
    page = BeautifulSoup(html_content, "html.parser")
    data = page.find("a", {"class": "next page-numbers"})
    if not data:
        next_page = None
    else:
        next_page = data.get("href")
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    pass
#     html_page = fetch(url)
#     header_news = html_page.find("div", {"class": "entry-header-inner"})
#     category = header_news.find("span", class_= "label").text
#     title = header_news.find("h1", class_= "entry-title").text

#     writer = header_news.find("span", class_= "author").text
#     # tags = quote.find("div", class_="tags").find_all("a")
#     # tag_list = [tag.text for tag in tags]
#     # single_quote = [text, author, tag_list]
#     data_news = {
#                 "url": url,
#                 "title": title,
#                 "writer": writer,
#                 "category": category,
#               }
#     return data_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     url = "https://blog.betrybe.com/"
#     html_content = fetch(url)
#     print(scrape_next_page_link(html_content))
