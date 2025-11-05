#!/usr/bin/python3

import seed

# Step 1: Connect to MySQL server
connection = seed.connect_db()
if connection:
    # Step 2: Create the database
    seed.create_database(connection)
    
    # Step 3: Close the initial connection
    connection.close()
    print("Connection successful")

    # Step 4: Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    if connection:

        print("Streaming user data:")
        for user in seed.stream_data(connection):
            print(user)
        # Step 5: Create the table
        seed.create_table(connection)
        
        # Step 6: Insert data from CSV
        seed.insert_data(connection, 'user_data.csv')

        # Step 7: Verify the database
        cursor = connection.cursor()
        cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present")

        # Step 8: Fetch and print the first 5 rows
        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)
        cursor.close()