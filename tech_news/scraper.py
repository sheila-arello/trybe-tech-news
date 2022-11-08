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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
