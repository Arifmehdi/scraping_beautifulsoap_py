import mysql.connector
import os


# Global variables
connection = None
cursor = None
# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306'
    )

# Initialize the global connection and cursor
connection = create_connection()
cursor = connection.cursor()

def create_database():

    database = "carscrapper03"

    try:
        # Check if the database exists
        cursor.execute(f"SHOW DATABASES LIKE '{database}'")
        database_exists = cursor.fetchone()

        if not database_exists:
            # Create the database if not exists
            cursor.execute(f"CREATE DATABASE `{database}`")
            print('\n'f"Database '{database}' created successfully.")
        else:
            print('\n'f"Database '{database}' already exists.")

    except mysql.connector.Error as err:
            print('\n'f"Error: {err}")
    # finally:
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
    return 'Success'


def create_table(table_name):

    database = "carscrapper03"

    try:
        # Switch to the created or existing database
        cursor.execute(f"USE `{database}`")

        # Check if the table exists, and if not, create it
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Your table creation query goes here
            create_table_query = f"""
                CREATE TABLE `{table_name}` (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    quantity INT,
                    dealer_location VARCHAR(255) NOT NULL
                )
            """
            cursor.execute(create_table_query)
            print('\n'f"'{table_name}' table created successfully.")
        else:
            print('\n'f"'{table_name}' table already exists.")

        # Commit the changes
        connection.commit()

    except mysql.connector.Error as err:
        print('\n'f"Error: {err}")

    return 'Hurrah!'

def drop_database_and_tables():
    connection = create_connection()
    cursor = connection.cursor()
    database = "carscrapper03"

    try:
        # Drop the entire database along with its tables
        cursor.execute(f"DROP DATABASE IF EXISTS `{database}`")
        print('\n'f"'{database}' Database and its tables dropped successfully.")

    except mysql.connector.Error as err:
        print('\n'f"Error: {err}")

    # finally:
    #     # Close the cursor and connection
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()

# # Get user input
print('Create [1]')
print('Drop   [2]')
userData = input('\n''Choose An Action: ')


if userData:
    userData = int(userData)

    if userData == 1:
        print('Create Database [1]')
        print('Create Table    [2]')
        userData02 = input('\n''Choose An Action: ')

        if userData02:
            userData02 = int(userData02)
            if userData02 == 1:
                create_database()
            elif userData02 == 2:
                table_name_input = input('Enter Table Name: ')
                table_name = table_name_input if table_name_input else 'tmp_inventories'
                create_table(table_name)
            else:
                print('Invalid action. Choose a valid option.')
        else:
            print('Input cannot be null or empty. Choose a proper action.')
        # create_database_and_table()
    elif userData == 2:
        drop_database_and_tables()
    else:
        print('Invalid action. Choose a valid option.')
    # Manually clear the screen (print empty lines)
    # print('\n' * 50)
else:
    print('Input cannot be null or empty. Choose a proper action.')