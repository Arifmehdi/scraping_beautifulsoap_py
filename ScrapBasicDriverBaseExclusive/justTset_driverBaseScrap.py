import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
import mysql.connector
from mysql_connector import get_mysql_connection

# ... (your existing code)

# Creating a MySQL connection
conn = get_mysql_connection()
cursor = conn.cursor()

# Check if the table exists, and if not, create it
table_name = 'tmp_inventories'  # Replace with your actual table name
cursor.execute(f"SHOW TABLES LIKE '{table_name}'")

if not cursor.fetchone():
    # Table does not exist, create it
    create_table_query = """
    CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        dealer_id INT,
        city VARCHAR(255),
        make VARCHAR(255),
        dealer_name VARCHAR(255),
        dealer_address VARCHAR(255),
        details_url TEXT,
        img_url TEXT,
        title VARCHAR(255),
        type VARCHAR(255),
        price INT,
        miles VARCHAR(255),
        engine_details TEXT,
        transmission VARCHAR(255),
        mileage VARCHAR(255),
        vin VARCHAR(255),
        stock VARCHAR(255),
        star INT,
        created_at DATETIME
    )
    """.format(table_name=table_name)

    cursor.execute(create_table_query)
    conn.commit()

# ... (your existing code)

# Writing data to MySQL
for item_dict in result_list:
    # Assuming 'your_table' is the name of your MySQL table
    query = """
    INSERT INTO `{table_name}`
    (dealer_id, city, make, dealer_name, dealer_address, details_url, img_url, title,
    type, price, miles, engine_details, transmission, mileage, vin, stock, star, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """.format(table_name=table_name)

    values = (
        item_dict['dealer_id'], item_dict['city'], item_dict['make'], item_dict['dealer_name'],
        item_dict['dealer_address'], item_dict['details_url'], item_dict['img_url'],
        item_dict['title'], item_dict['type'], item_dict['price'], item_dict['miles'],
        item_dict['engine_details'], item_dict['transmission'], item_dict['mileage'],
        item_dict['vin'], item_dict['stock'], item_dict['star'], item_dict['created_at']
    )

    cursor.execute(query, values)

    # Optional: Pause between each insertion
    time.sleep(10)

# Committing the changes and closing the database connection
conn.commit()
cursor.close()
conn.close()

print('Data inserted into MySQL successfully')