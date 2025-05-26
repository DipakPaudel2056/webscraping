# 🕷️🕸️ Web scraping
## overview
Enough of learning let's get something done for the next 8 days. Here i will be planning, writing down my thought processes and my way of working day be day. In 8 days for next 3 hours a day I must lock myself in my room for this particular project.
### What i will be doing?
1. I will brainstorm and scrape some of the web-pages.
2. I will clean the scrapped data with my learning of excel as well as pandas.
3. I will store those cleaned data in SQL programatically.
4. I will visualize the data extracting valuable insights using python's matplotlib.

# 🔏 Day-1
- ✅ Brainstorm for project Idea
- ✅ Understanding of beautifulsoup
- ✅ Finding page to scrape the data 
- ✅ Project initiation

So I read couple of blogs that it is difficult to run crawler in big company's site because of their anti-bot system. However, let's setup every thing and try Nike's shoes section scraping.

I have no idea so far how does it work. However let's get started with it. So for that, i am gonna have to start new file app.py --> my main project file i guess. and install the dependecies. So for now let's just get request and beautifulsoup and will see from there.

Well, i have scraped html bit no way this makes any sense at this moment.

At first i thought the html soup object i was printing in console is what i have to deal with however it is not. we can actually parse as the browser what we see in the browser.

to windup todays lesson lets create a csv file programmatically and add the  findings in there. and also the url seems pretty dynamic we have to figureout the way to store it somewhere dynamically.

Well done for scraping data from nike's store, for now the data seems pretty clean. it is just the basic process will figure out the task for tomorrow.

# 🔏 Day-2
For now i have only page loaded and i can only scrape 25 data however in the nike page they have 547 data i did some google check and i can actually scrape all those if i could deal with the pagination. 
- ✅ scrape all data dealing with pagination.
    let's begin working.
    i used pytest playwright to simulate the scrolling effect using different times for sleep hopefully it will run on infinite scroll of the nike product page.
    unfortunately 😔. it doesnot seem working even putting the sleep value of 60 so, i may have to find different approach for this. 
    will work on it on Day-3.
    😁😁 the content i got from the playwright page is then converted to html parser to be able to work with beautiful soup.
    1. managed to scrape more data then yesterday.
    2. still i havenot hit the page bottom, i ran the bot for sometime and found it was 29000 so i hardcoded that value, i must fix it tomorrow.
    3. time to sleep

- ✅ check for potential cleaning in excel.
    Since it is just 3 columns of data scrapped there is no error so far.
- ✔️ instantiate the mysql server to store these findings

# 🔏 Day-3
- ✔️ instantiate the mysql server to store these findings
- ✅ with just title and subtitle the data looks very repititive get some more details from the scraper
    - lets's get tag such as best seller, just in, sustainable material as well
    - Now the next task is to simulate to click each link and get into the product and find the available sizes, colors and description
    i am able to simulate and get the description, and colors however i struggled over an hour to find the solution for the available sizes. will work on it tomorrow.
    I will run it untill i get the scroll height > 29000 today and see what it shows in both files and will work on new findings tomorrow.


# 🔏 Day-4 
✅ instantiate the mysql server to store these findings
I have successfully connected and programmatically saved the data from csv to the database and also done some modification.
- ❌ fix the issue with the shoe sizes label in product page: </br>
This is just a simple project so let's focus on other stuff than getting stuck in the sizes this time.
- ✔️ Do some python leetcodes

# 🔏 Day-5
- ✔️  try some manupulation on this samll set of data using python
    1. In  my project app.py is mainly responsible for extracting the data from nike website using beautiful soup.
    2. manupulation.py is responsible for cleaning the dataset we just extracted to store in the database.
    3. storetodatabase.py is responsible for converting and storing the data in the database table using python sql connector.
    4. Today's target is to build some simple chart using matplotlib as well. 
I havenot done much with the data itself, changed the data type and stored them clean in the database.
Price functionality is handeled at the front rather than sending to the database.

Before doing some visualization in matplotb, why not explore the data in excel first, 
- i want to find the chart showing relation between price-range and count
- i want to find the chart showing relation between subtitle and price and 

- ✅ Do some python leetcodes


