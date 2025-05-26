from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def generatepricechart():
    df = pd.read_csv("nikeprice.csv",encoding = "unicode_escape")
    # created aggregated table
    pricerangevscount = df.groupby(['price_range'])['title'].count().reset_index().rename(columns={"title":"count"})
    xaxis = pricerangevscount['price_range'].tolist()
    yaxis = pricerangevscount['count'].tolist()
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

    
