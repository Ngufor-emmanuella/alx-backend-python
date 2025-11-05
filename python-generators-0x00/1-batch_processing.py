import mysql.connector

def connect_to_database():
    """Connects to the MySQL ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def stream_users_in_batches(batch_size):
    """Generator that streams rows from the user_data table in batches."""
    connection = connect_to_database()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM user_data;")
    
    while True:
        batch = cursor.fetchmany(batch_size)  # Fetch a batch of rows
        if not batch:
            break  # Exit the loop if no more rows are left
        yield batch  # Yield the current batch
    
    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user[3] > 25]  # Assuming age is the 4th column
        yield filtered_users  # Yield the filtered users

# Example usage
if __name__ == "__main__":
    for users in batch_processing(5):  # Process in batches of 5
        print(users)  # Print the filtered users