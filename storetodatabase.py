# store the nikeprice csv and nikedetail csv into database
# let's try programatically since it seems really hard to work in database itself 
import csv
import mysql.connector

databaseconn = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="",
    database="nikedatabase"
)
if databaseconn.is_connected():
    cursor = databaseconn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("connected to database",record)
    # get the rows of the data from the csv file
    with open('nikeprice.csv','r') as file:
        csv_data = csv.reader(file)
        header = next(csv_data)
        for row in csv_data:
            placeholders = ', '.join(['%s']*len(row))
            columns = ', '.join(header)
            query = f"INSERT INTO nikepricetable ({columns}) VALUES ({placeholders})"
            cursor.execute(query,row)
        
    # add description data into the database
    with open("nikedetailed.csv",'r') as file:
        csv_data = csv.reader(file)
        header = next(csv_data)
        for row in csv_data:
            placeholders = ', '.join(['%s']*len(row))
            columns = ', '.join(header)
            query = f"INSERT INTO nikedescriptiontable ({columns}) VALUES ({placeholders})"
            cursor.execute(query,row)
        
    databaseconn.commit()
    print("nike price data successfully added to database")


cursor.close()
databaseconn.close()