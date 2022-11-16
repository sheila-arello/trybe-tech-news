import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)


# Requisito 12
def analyzer_menu():
    menu = (
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )
    print(menu)
    option = input('Opção escolhida: ')
    if option.isnumeric():
        if int(option) < 8:
            value = switch_options(int(option))
            print(value)
            return value
    print("Opção inválida", file=sys.stderr)


def switch_options(argument):
    switcher = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a tag:",
        4: "Digite a categoria:",
    }
    value = None
    if argument == 7:
        value = "Encerrando script"
        print(value)
        SystemExit()
    if argument == 6:
        value = top_5_categories()
    if argument == 5:
        value = top_5_news()
    if argument >= 0 and argument < 5:
        value = input(switcher.get(argument))
        if argument == 0:
            value = get_tech_news(int(value))
        if argument == 1:
            value = search_by_title(value)
        if argument == 2:
            value = search_by_date(value)
        if argument == 3:
            value = search_by_tag(value)
        if argument == 4:
            value = search_by_category(value)
    return value
