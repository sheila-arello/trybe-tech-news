# Requisito 1
def fetch(url):
    headers = {'user-agent': 'Fake user-agent'}
    try:
        response = requests.get(url, headers=headers, timeout=wait)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
