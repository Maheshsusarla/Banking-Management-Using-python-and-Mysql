import mysql.connector

conn=mysql.connector.connect(
    host="lost-name",
    user="user-name",
    password="your password",
    database="your_databasename"
)

cursor = conn.cursor()

# cursor.execute("select * from customers")

cursor.execute(""" 
create table if not exists customers(
acc_num int primary key ,
name varchar(100),
pin int,
balance float
)
""")

conn.commit()