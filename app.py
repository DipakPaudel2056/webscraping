# let's code the scraper
import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.nike.com/au/w/mens-shoes-nik1zy7ok"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # now i have got the soup let's try to get select only necessary tags from here
    # lets tag a div and 
    allshoes = soup.css.select('.product-card')
    for shoe in allshoes:
        shoenametag = shoe.find('div',class_='product-card__title')
        shoesubtitletag = shoe.find('div',class_='product-card__subtitle')
        shoepricetag = shoe.find('div',class_='product-price')
        shoename = shoenametag.text.strip()
        shoesubtitle = shoesubtitletag.text.strip()
        shoeprice =shoepricetag.text.strip()
        
        print(shoesubtitle)
        print(shoename)
        print(shoeprice)
        print('---')
    
if __name__ == '__main__':
    scrape()