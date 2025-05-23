# let's code the scraper
import requests
from bs4 import BeautifulSoup
import asyncio 
from playwright.async_api import async_playwright

# to write in csv file
import csv

def scrape():
    url = "https://www.nike.com/au/w/mens-shoes-nik1zy7ok"
    async def scroll_to_bottom(page):
        prev_height = None
        while True:
            current_height = await page.evaluate("""()=>{window.scrollBy(0,window.innerHeight);return document.body.scrollHeight;}""")
            if current_height == prev_height:
                break
            prev_height = current_height
            await page.wait_for_timeout(4000)
            
    async def scrape_infinite_scroll(url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url,timeout=60000)
            await scroll_to_bottom(page)
            content = await page.content()
            await browser.close()
            soup = BeautifulSoup(content, 'html.parser')
    # # now i have got the soup let's try to get select only necessary tags from here
            allshoes = soup.find_all('div',class_='product-card')
            with open('nikeprice.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title','subtitle','price','image'])
                for shoe in allshoes:
                    shoenametag = shoe.find('div',class_='product-card__title')
                    shoesubtitletag = shoe.find('div',class_='product-card__subtitle')
                    shoepricetag = shoe.find('div',class_='product-price')
                    shoeimagetag = shoe.find('img')
                    shoename = shoenametag.text.strip()
                    shoesubtitle = shoesubtitletag.text.strip()
                    shoeprice =shoepricetag.text.strip()
                    shoeimgsrc = shoeimagetag['src']
                    writer.writerow([shoename,shoesubtitle,shoeprice,shoeimgsrc])
                    print([shoename,shoesubtitle,shoeprice])
    asyncio.run(scrape_infinite_scroll(url))
    
    
if __name__ == '__main__':
    scrape()