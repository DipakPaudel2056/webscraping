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
            if current_height >= 25000:
                break
            prev_height = current_height
            await page.wait_for_timeout(4000)
            print(prev_height,current_height)
            
    async def scrape_infinite_scroll(url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url,timeout=60000)
            await scroll_to_bottom(page)
            content = await page.content()
            await browser.close()
            # response = requests.get(url)
            # response.raise_for_status()
            soup = BeautifulSoup(content, 'html.parser')
    # # now i have got the soup let's try to get select only necessary tags from here
            allshoes = soup.find_all('div',class_='product-card')
            with open('nikeprice.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title','subtitle','price'])
                for shoe in allshoes:
                    shoenametag = shoe.find('div',class_='product-card__title')
                    shoesubtitletag = shoe.find('div',class_='product-card__subtitle')
                    shoepricetag = shoe.find('div',class_='product-price')
                    shoename = shoenametag.text.strip()
                    shoesubtitle = shoesubtitletag.text.strip()
                    shoeprice =shoepricetag.text.strip()
                    writer.writerow([shoename,shoesubtitle,shoeprice])
                    print([shoename,shoesubtitle,shoeprice])
    asyncio.run(scrape_infinite_scroll(url))
    
    # response = requests.get(url)
    # response.raise_for_status()
    # soup = BeautifulSoup(response.text, 'html.parser')
    # # now i have got the soup let's try to get select only necessary tags from here
    # allshoes = soup.css.select('.product-card')
    # with open('nikeprice.csv','w',newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['title','subtitle','price'])
    #     for shoe in allshoes:
    #         shoenametag = shoe.find('div',class_='product-card__title')
    #         shoesubtitletag = shoe.find('div',class_='product-card__subtitle')
    #         shoepricetag = shoe.find('div',class_='product-price')
    #         shoename = shoenametag.text.strip()
    #         shoesubtitle = shoesubtitletag.text.strip()
    #         shoeprice =shoepricetag.text.strip()
    #         writer.writerow([shoename,shoesubtitle,shoeprice])
    
if __name__ == '__main__':
    scrape()