import mysql.connector

def connect_to_database():
    """Connects to the MySQL ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def stream_users():
    """Generator that streams rows from the user_data table one by one."""
    connection = connect_to_database()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM user_data;")
    
    for row in cursor:
        yield row  # Yield each row one at a time
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    for user in stream_users():
        print(user)  # Print each user row