import pandas as pd
# let's get the csv data of nikeprice.csv
def nikepriceclean():
    pricedataframe = pd.read_csv("nikeprice.csv",encoding='unicode_escape')
# check for the empty cells and print result
    pricedataframe['title'] = pricedataframe['title'].astype("string")
    pricedataframe['tag'] = pricedataframe['tag'].astype("string")
    pricedataframe['subtitle'] = pricedataframe['subtitle'].astype("string")
    pricedataframe['image'] = pricedataframe['image'].astype("string")

    def check_empty(dataframe):
        return dataframe.isnull().sum().sum()
    print("Total empty cells",check_empty(pricedataframe))
    
    # what if we add new column saying price range, that have cheap affordable and expensive values based on price 
    # price less than 100 is cheap
    # price less than 200 is affordable
    # price greater than 200 is expensive
    
# so far we are managing the $ issue in the database but with pandas we can do it here
    currency_converter = lambda x : int(x.split('$')[-1]) if isinstance(x,str) else x
    pricedataframe['price'] = pricedataframe['price'].apply(currency_converter)
    affordablity = lambda x : "cheap" if x < 100 else  "affordable" if 200 > x > 100 else "expensive"
    pricedataframe['price_range'] = pricedataframe['price'].apply(affordablity)

# pricedataframe['price'] = pricedataframe['price']
# since we have done that let's also convert the type of title, subtitle, image and tag as well
    pricedataframe.to_csv('nikeprice.csv',index=False)

# let's try to extract more data from nikedetailed
def cleannikedetail():
    df = pd.read_csv("nikedetailed.csv",encoding='unicode_escape')
    # one thing i want to do here is seperate the color with , rather than /
    splitincomma = lambda x : x.replace("/",",")
    df['color'] = df['color'].apply(splitincomma)
    df.to_csv('nikedetailed.csv',index=False)

