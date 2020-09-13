#Create items Table

CREATE TABLE items 
(ID int Serial PRIMARY KEY,ITEM varchar(255) NOT NULL,PRICE int);

#inserting values 

insert into items (item, price)
values 
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

#displaying values 

select * from items

select * from items where price > 80

select * from items where price < 30


#Create customers Table

Create TABLE customers (customer_ID SERIAL PRIMARY KEY,first_name varchar(255),last_name varchar(255));

#inserting values 

insert into customers (first_name,last_name)
values ('Greg','Jones'),('Sandra','Jones'),('Scott','Scott'),('Melanie','Jonson');

#displaying values 

select * from customers

select * from customers where first_name = 'Smith'

select * from customers where first_name != 'Craig'