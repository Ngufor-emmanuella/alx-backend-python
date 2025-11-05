import mysql.connector

def connect_to_database():
    """Connects to the MySQL ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def stream_user_ages():
    """Generator that yields user ages from the user_data table one by one."""
    connection = connect_to_database()
    cursor = connection.cursor()
    
    cursor.execute("SELECT age FROM user_data;")  # Fetch only the age column
    for (age,) in cursor:  # Unpack the tuple directly
        yield age  # Yield each age
    
    cursor.close()
    connection.close()

def calculate_average_age():
    """Calculates the average age of users."""
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age  # Sum the ages
        count += 1  # Count the number of users
    
    if count == 0:
        return 0  # Avoid division by zero if no users found
    return total_age / count  # Calculate average

# Example usage
if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")  # Print the average age