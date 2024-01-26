import requests
from bs4 import BeautifulSoup
from config import URL, HEADERS

def sort_products_price(products) -> list[list]:
    return sorted(products, key=lambda x: x[2])
    

def scraping_mercado_livre() -> list[list]: 
    products = []
    response = requests.get(URL, headers=HEADERS)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.find_all("div", class_="ui-search-result__wrapper")
    
    for card in cards:
        price_str = card.find("span", class_="andes-money-amount__fraction").string
        if price_str.find('.') > 0:
            price_str = price_str.replace('.', '')
        price = float(price_str)
        if card.find("span", class_="ui-search-reviews__rating-number") and price < 1200:
            rating_str = card.find("span", class_="ui-search-reviews__rating-number").string
            rating = float(rating_str)
            if rating > 4.5:
                title = card.find("h2", class_="ui-search-item__title").string
                link = card.find('a', href=True)
                url = link['href']
                card_id_product = card.find("div", class_="andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16")
                id_product = card_id_product.get("id").replace(":", "")
                processed = 0
                products.append([id_product, title, price, rating, url, processed])
    
    return sort_products_price(products)

  