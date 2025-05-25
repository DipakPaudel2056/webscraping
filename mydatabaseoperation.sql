-- let's create a database and the table to store the data from the nike's csv file--
CREATE DATABASE nikedatabase;
-- i need to find the way to store the csv data into this database 
use nikedatabase;
CREATE table nikepricetable (
title varchar(500),
subtitle varchar(500),
price int,
imagesrc varchar(500),
tag varchar(50)) ;

CREATE TABLE nikedescriptiontable (
    title VARCHAR(500),
    stylecode VARCHAR(500),
    description VARCHAR(1000),
    color VARCHAR(100)
); 