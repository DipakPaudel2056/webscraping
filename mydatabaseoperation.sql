-- let's create a database and the table to store the data from the nike's csv file--
CREATE DATABASE nikedatabase;
-- i need to find the way to store the csv data into this database 
SET sql_safe_updates=0;

use nikedatabase;
CREATE TABLE nikepricetable (
    title VARCHAR(500),
    subtitle VARCHAR(500),
    price VARCHAR(6),
    image VARCHAR(500),
    tag VARCHAR(50)
);
select COUNT(*) from nikepricetable;
-- HERE I HAVE PRICE COMING FROM CSV IN STRING CONVERT IT TO INTEGER
-- remove $ from the string 
ALTER TABLE nikepricetable ADD COLUMN price_int INT;
UPDATE nikepricetable 
SET 
    nikepricetable.price_int = REPLACE(price, '$', '')
WHERE
    nikepricetable.price LIKE '$%';

CREATE TABLE nikedescriptiontable (
    title VARCHAR(500),
    stylecode VARCHAR(500),
    description VARCHAR(1000),
    color VARCHAR(100)
); 
SELECT * FROM nikedescriptiontable;	
select count(*) from nikedescriptiontable;	

-- find a way to insert the data from csv into these tables
-- SET GLOBAL local_infile = 1;
--  LOAD DATA INFILE 'C:\Users\paude\OneDrive\Desktop\datascience\webscraping\nikeprice.csv'
--  INTO TABLE nikepricetable
--  FIELDS TERMINATED BY ','
--  ENCLOSED BY '"'
--  LINES TERMINATED BY '\n'
--  IGNORE 1 ROWS;
--  
--  THIS APPROACH WILL ONLY WORK IF WE HAVE THE CSV FILE STORED IN THE DATABASE ITSELF HOWEVER I dont want to do that so i will do it programatically
 
 