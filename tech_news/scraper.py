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


# web_links = soup.select('a')
# actual_web_links = [web_link['href'] for web_link in web_links]
# Requisito 4
def scrape_noticia(html_content):
    page = BeautifulSoup(html_content, "html.parser")
    url = page.find("link", {"rel": "canonical"})['href']
    tags = page.find_all("a", {"rel": "tag"})
    tag_list = sorted(list(set([tag.text for tag in tags])))
    sumary = page.find("div", class_="entry-content").find("p").text
    header_news = page.find("div", {"class": "entry-header-inner"})
    category = header_news.find("span", class_="label").text
    title = header_news.find("h1", class_="entry-title").text
    writer = header_news.find("span", class_="author").text
    timestamp = header_news.find("li", class_="meta-date").text

    # comments_count - número de comentários que a notícia recebeu.
    # Se a informação não for encontrada, salve este atributo como 0 (zero)
    # summary - o primeiro parágrafo da notícia. entry-content

    data_news = {
                "url": url,
                "title": title.strip(),
                "writer": writer,
                "category": category,
                "timestamp": timestamp,
                "tags": tag_list,
                "comments_count": 0,
                "summary": sumary.strip(),
              }
    return data_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     url = "https://blog.betrybe.com/"
#     html_content = fetch(url)
#     print(scrape_next_page_link(html_content))
#     print(scrape_noticia(fetch("https://blog.betrybe.com/ferramentas/r-studio/")))

# <div class="post-comments post-comments-simple" id="comments">
