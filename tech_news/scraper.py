import requests
import re
import time
from bs4 import BeautifulSoup
from tech_news.database import (
    create_news,
)


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
    data_links = page.find_all("a", {"class": "cs-overlay-link"})
    for link in data_links:
        if link.get("href") is not None:
            lista.append(link.get("href"))
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
    comments = page.find("div", {"id": "comments"})
    if not comments:
        comments_count = 0
    else:
        txt = comments.find("h5").text.strip()
        comments_count = int(re.findall('[0-9]+', txt)[0])
    data_news = {
                "url": url,
                "title": title.strip(),
                "writer": writer,
                "category": category,
                "timestamp": timestamp,
                "tags": tag_list,
                "comments_count": comments_count,
                "summary": sumary.strip(),
              }
    return data_news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    html_content = fetch(url)
    links = scrape_novidades(html_content)
    while amount > len(links):
        next_page = scrape_next_page_link(html_content)
        html_content = fetch(next_page)
        links += scrape_novidades(html_content)
    noticias = [scrape_noticia(fetch(link)) for link in links[:amount]]
    create_news(noticias)
    return noticias
