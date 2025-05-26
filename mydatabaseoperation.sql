-- let's create a database and the table to store the data from the nike's csv file--
CREATE DATABASE nikedatabase;
-- i need to find the way to store the csv data into this database 
SET sql_safe_updates=0;

use nikedatabase;
DROP TABLE IF EXISTS nikepricetable;
CREATE TABLE nikepricetable (
    title VARCHAR(500),
    subtitle VARCHAR(500),
    price VARCHAR(6),
    image VARCHAR(500),
    tag VARCHAR(50),
    price_range VARCHAR(50)

);
select count(subtitle) from nikepricetable where nikepricetable.subtitle like '%Running%';
-- HERE I HAVE PRICE COMING FROM CSV IN STRING CONVERT IT TO INTEGER
-- remove $ from the string 
DROP TABLE IF EXISTS nikedescriptiontable;
CREATE TABLE nikedescriptiontable (
    title VARCHAR(500),
    stylecode VARCHAR(500),
    description VARCHAR(1000),
    color VARCHAR(100)
); 
SELECT * FROM nikedescriptiontable;	
select count(*) from nikedescriptiontable;	

select * FROM nikepricetable;
 
 