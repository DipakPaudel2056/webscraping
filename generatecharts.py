from matplotlib import pyplot as plt
import numpy as np
# before generating the bar graph as created in the excel sheet i must be able to create a pivot table using pandas
import pandas as pd
# since we are working in nikeprice.csv
df = pd.read_csv("nikeprice.csv",encoding = "unicode_escape")
# created aggregated table
pricerangevscount = df.groupby(['price_range'])['title'].count().reset_index().rename(columns={"title":"count"})
xaxis = pricerangevscount['price_range'].tolist()
yaxis = pricerangevscount['count'].tolist()

def generatepricechart():
    print("generating charts")
    plt.figure(figsize=(10,8))
    plt.bar(range(len(xaxis)),yaxis)
    plt.title("price range vs number of shoes")
    plt.xlabel("affordable scale")
    plt.ylabel("number of shoes")
    ax = plt.subplot()
    ax.set_xticks(range(len(xaxis)))
    ax.set_xticklabels(xaxis)
    plt.savefig("nike_price_finding.png")
    print("chart generation complete")

    
generatepricechart()