import time
import sqlite3
import functools

query_cache = {}

def with_db_connection(func):
    """Decorator to manage database connections."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open a database connection
        conn = sqlite3.connect('users.db')
        try:
            # Pass the connection to the function
            return func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed after the function call
            conn.close()
    return wrapper

def cache_query(func):
    """Decorator to cache query results based on the SQL query string."""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if the query result is already cached
        if query in query_cache:
            print("Using cached result.")
            return query_cache[query]
        
        # Call the original function to get the result
        result = func(conn, query, *args, **kwargs)
        
        # Cache the result
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(users)
print(users_again)