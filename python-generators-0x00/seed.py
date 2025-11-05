import mysql.connector
import csv
import uuid

def connect_db():
    """Connects to the MySQL server."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='root'  
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='root', 
        password='root', 
        database='ALX_prodev'
    )

def create_table(connection):
    """Creates the user_data table if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    """Inserts data into the user_data table from a CSV file."""
    cursor = connection.cursor()
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
           
            user_id = str(uuid.uuid4())
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s);
            """, (user_id, row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()



def stream_data(connection):
    """Generator that streams rows from the user_data table one by one."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    
    for row in cursor:
        yield row  
    
    cursor.close()
    connection.close()
    
    