# let's code the scraper
import requests
from bs4 import BeautifulSoup
import asyncio 
from playwright.async_api import async_playwright
from manupulation import nikepriceclean, cleannikedetail
from storetodatabase import storetodatabase
from generatecharts import generatepricechart

# to write in csv file
import csv

def scrape():
    url = "https://www.nike.com/au/w/mens-shoes-nik1zy7ok"
    async def scroll_to_bottom(page):
        while True:
            current_height = await page.evaluate("""()=>{window.scrollBy(0,window.innerHeight);return document.body.scrollHeight;}""")
            await page.wait_for_timeout(6000)
            if current_height >= 25000:
                break
            print(current_height)
    # created new file to store the detailed information 
    with open('nikedetailed.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title','stylecode','description','color'])
        file.close()
    allproductpageurllist = []
    def move_to_product_page(productpageurl):
        # here i want to scrape the data from individual page and store in the new csv file according to product
        # since it is only one page i hope classic requests will work to make the soup and extract the data
        response = requests.get(productpageurl,timeout=2000)
        # let's make the soup from response.text
        soup = BeautifulSoup(response.text,'html.parser')
        productdescription = soup.find(attrs={'data-testid':'product-description'}).text.strip() or soup.find('div',class_='description-text')
        colordescription = soup.find(attrs={'data-testid':'product-description-color-description'}).text.strip().split(":")[1] or ''
        stylecode =soup.find(attrs={'data-testid':'product-description-style-color'}).text.strip().split(':')[1] or ''
        product_title =soup.find('h1',{'data-testid':'product_title'}).text.strip() or ''
        # let's begin writing this information into new excel file i would also get the title of the shoes
        with open('nikedetailed.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([product_title,stylecode,productdescription,colordescription])
            file.close()
            
    async def scrape_infinite_scroll(url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url,timeout=60000)
            await scroll_to_bottom(page)
            content = await page.content()
            await browser.close()
            soup = BeautifulSoup(content, 'html.parser')
            allshoes = soup.find_all('div',class_='product-card')
            with open('nikeprice.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title','subtitle','price','image','tag'])
                for shoe in allshoes:
                    # let's find the a tag here in this div which will navigate us to next page
                    nextpageurltag = shoe.find('a',class_='product-card__link-overlay')
                    shoenametag = shoe.find('div',class_='product-card__title')
                    shoesubtitletag = shoe.find('div',class_='product-card__subtitle')
                    shoepricetag = shoe.find('div',class_='product-price')
                    shoetagtag = shoe.find('div',class_='product-card__messaging accent--color') or None
                    shoeimagetag = shoe.find('img')
                    shoename = shoenametag.text.strip()
                    shoesubtitle = shoesubtitletag.text.strip()
                    shoeprice =shoepricetag.text.strip()
                    nextpageurl = nextpageurltag['href']
                    if shoetagtag:
                        shoetag = shoetagtag.text.strip()
                    else:
                        shoetag = None
                    shoeimgsrc = shoeimagetag['src']
                    writer.writerow([shoename,shoesubtitle,shoeprice,shoeimgsrc,shoetag])
                    if shoetag != 'Available in SNKRS':
                        allproductpageurllist.append(nextpageurl)
    asyncio.run(scrape_infinite_scroll(url))
    
    for page in allproductpageurllist:
        move_to_product_page(page)
    # do some manupulation
    nikepriceclean()
    cleannikedetail()
    #store to database
    storetodatabase()
    #display chart
    generatepricechart()
    

    
if __name__ == '__main__':
    scrape()