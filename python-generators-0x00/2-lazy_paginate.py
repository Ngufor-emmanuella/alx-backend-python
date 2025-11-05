import mysql.connector

def connect_to_database():
    """Connects to the MySQL ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def paginate_users(page_size, offset):
    """Fetches a page of users from the user_data table."""
    connection = connect_to_database()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (page_size, offset))
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return rows

def lazy_paginate(page_size):
    """Generator that lazily fetches paginated user data."""
    offset = 0
    
    while True:
        page = paginate_users(page_size, offset)  # Fetch the next page
        if not page:  # If no more rows, stop the generator
            break
        yield page  # Yield the current page
        offset += page_size  # Increment offset for the next page

# Example usage
if __name__ == "__main__":
    for users in lazy_paginate(5):  # Fetch users in pages of 5
        print(users)  # Print the current page of users