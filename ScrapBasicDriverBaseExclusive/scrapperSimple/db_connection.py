import mysql.connector

# make conection toi setup with 
## your credential 
def create_connection():
    # Change the connection details according to your MySQL setup
    config = {
        'user'      : 'root',
        'password'  : '',
        'host'      : 'localhost',
        'port'      : '3306',       #takes from laravel .env
    }

    # Connect to MySQL Server
    connection = mysql.connector.connect(**config)
    return connection



#create database and table if does not exist
def create_database_and_table():
    connection = create_connection()
    cursor = connection.cursor()
    database = "carscrapper03"

    # Create 'carscrapper' database if not exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`")
    connection.database = database


    # Check if the table exists, and if not, create it
    table_name = 'tmp_inventories_03'  # Replace with your actual table name
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")

    if not cursor.fetchone():
        # Table does not exist, create it
        create_table_query = """
        CREATE TABLE {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            dealer_id INT,
            city VARCHAR(255),
            make VARCHAR(255) NOT NULL,
            dealer_name VARCHAR(255) NOT NULL,
            dealer_address VARCHAR(255),
            dealer_location VARCHAR(255),
            details_url TEXT,
            img_url TEXT,
            local_img_url TEXT,
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
        connection.commit()
        cursor.close()
        connection.close()



# behave as a constructor in php 
if __name__ == "__main__":
    create_database_and_table()